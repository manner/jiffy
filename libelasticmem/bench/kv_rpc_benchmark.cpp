#include <fstream>
#include <sstream>
#include "../src/storage/service/block_chain_client.h"
#include "../src/utils/time_utils.h"
#include "../src/utils/signal_handling.h"
#include "../src/utils/logger.h"
#include "../src/utils/cmd_parse.h"

using namespace elasticmem::storage;
using namespace elasticmem::utils;
using namespace ::apache::thrift;

static void load_workload(const std::string &workload_path,
                          std::vector<std::pair<int32_t, std::vector<std::string>>> &workload) {
  std::ifstream in(workload_path);
  std::string line;
  while (std::getline(in, line)) {
    std::istringstream iss(line);
    std::vector<std::string> tokens{std::istream_iterator<std::string>{iss},
                                    std::istream_iterator<std::string>{}};
    int32_t cmd_id = -1;
    if (tokens[0] == "get") {
      cmd_id = 0;
    } else if (tokens[0] == "put") {
      cmd_id = 1;
    } else if (tokens[0] == "remove") {
      cmd_id = 2;
    } else if (tokens[0] == "update") {
      cmd_id = 3;
    } else if (tokens[0] == "wait") {
      continue;
    } else {
      throw std::logic_error("Unknown operation " + tokens[0]);
    }
    tokens.erase(tokens.begin());
    workload.emplace_back(cmd_id, tokens);
  }
}

class throughput_benchmark {
 public:
  throughput_benchmark(const std::string &workload_path,
                       const std::vector<std::string> &chain,
                       std::size_t num_ops,
                       std::size_t max_async)
      : num_ops_(num_ops), max_async_(max_async), client_(chain) {
    begin_ = 0.0;
    end_ = 0.0;
    load_workload(workload_path, workload_);
  }

  void run() {
    worker_thread_ = std::thread([&]() {
      std::size_t i = 0;
      std::future<std::string> buf[10];
      begin_ = time_utils::now_us();
      while (i < num_ops_) {
        std::size_t async_limit = std::min(i + max_async_, num_ops_);
        for (std::size_t j = i; j < async_limit; ++j) {
          buf[j - i] = client_.run_command(workload_[j].first, workload_[j].second);
        }
        for (std::size_t j = i; j < async_limit; ++j) {
          buf[j - i].wait();
        }
        i += async_limit;
      }
      end_ = time_utils::now_us();
      fprintf(stderr, "%lf", static_cast<double>(num_ops_) * 1000000.0 / (end_ - begin_));
    });
  }

  void wait() {
    if (worker_thread_.joinable()) {
      worker_thread_.join();
    }
  }

 private:
  std::thread worker_thread_;
  double begin_;
  double end_;
  std::size_t num_ops_;
  std::size_t max_async_;
  std::vector<std::pair<int32_t, std::vector<std::string>>> workload_;
  block_chain_client client_;
};

class latency_benchmark {
 public:
  latency_benchmark(const std::string &workload_path,
                    const std::vector<std::string> &chain,
                    std::size_t num_ops)
      : num_ops_(num_ops), client_(chain) {
    load_workload(workload_path, workload_);
  }

  void run() {
    std::size_t i = 0;
    time_utils::now_us();
    while (i < num_ops_) {
      auto t0 = time_utils::now_us();
      client_.run_command(workload_[i].first, workload_[i].second).get();
      auto t = time_utils::now_us() - t0;
      fprintf(stderr, "%zu %" PRId64 "\n", i, t);
      ++i;
    }
  }

 private:
  std::size_t num_ops_;
  std::vector<std::pair<int32_t, std::vector<std::string>>> workload_;
  block_chain_client client_;
};

int main(int argc, char **argv) {
  signal_handling::install_signal_handler(argv[0], SIGSEGV, SIGKILL, SIGSTOP, SIGTRAP);

  GlobalOutput.setOutputFunction(log_utils::log_thrift_msg);

  cmd_options opts;
  opts.add(cmd_option("chain", 'c', false).set_default("127.0.0.1:9093:9094:9095:9096:0").set_description(
      "Comma separated block chain to benchmark"));
  opts.add(cmd_option("benchmark-type", 'b', false).set_default("throughput").set_description("Benchmark type"));
  opts.add(cmd_option("num-threads", 't', false).set_default("1").set_description("# of benchmark threads to run"));
  opts.add(cmd_option("num-ops", 'n', false).set_default("100000").set_description("# of operations to run"));
  opts.add(cmd_option("max-async", 'm', false).set_default("1000").set_description(
      "Maximum number of unacknowledged requests in flight"));
  opts.add(cmd_option("workload-path", 'w', false).set_default("data").set_description(
      "Path to read the workload from"));

  cmd_parser parser(argc, argv, opts);
  if (parser.get_flag("help")) {
    std::cout << parser.help_msg() << std::endl;
    return 0;
  }

  std::string chain_str;
  std::string benchmark_type;
  std::size_t num_threads;
  std::size_t num_ops;
  std::size_t max_async;
  std::string workload_path;

  try {
    chain_str = parser.get("chain");
    benchmark_type = parser.get("benchmark-type");
    num_threads = static_cast<std::size_t>(parser.get_int("num-threads"));
    num_ops = static_cast<std::size_t>(parser.get_int("num-ops"));
    max_async = static_cast<std::size_t>(parser.get_int("max-async"));
    workload_path = parser.get("workload-path");
  } catch (cmd_parse_exception &ex) {
    std::cerr << "Could not parse command line args: " << ex.what() << std::endl;
    std::cerr << parser.help_msg() << std::endl;
    return -1;
  }

  std::vector<std::string> chain;
  std::stringstream ss(chain_str);
  while (ss.good()) {
    std::string block;
    std::getline(ss, block, ',');
    chain.push_back(block);
  }

  if (benchmark_type == "throughput") {
    std::vector<throughput_benchmark *> benchmark;

    // Create
    for (std::size_t i = 0; i < num_threads; i++) {
      benchmark.push_back(new throughput_benchmark(workload_path, chain, num_ops, max_async));
    }

    // Start
    for (std::size_t i = 0; i < num_threads; i++) {
      benchmark[i]->run();
    }

    // Wait
    for (std::size_t i = 0; i < num_threads; i++) {
      benchmark[i]->wait();
    }

    // Cleanup
    for (std::size_t i = 0; i < num_threads; i++) {
      delete benchmark[i];
    }
  } else if (benchmark_type == "latency") {
    latency_benchmark benchmark(workload_path, chain, num_ops);
    benchmark.run();
  }
}