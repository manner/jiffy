#include <iostream>
#include <jiffy/client/jiffy_client.h>

int main() {
  std::cout << "hi" << std::endl;
  jiffy::client::jiffy_client client("127.0.0.1", 9090, 9091);
  auto file = client.open_or_create_file("/test.txt","local://tmp");
  std::cout << file->seek(0) << std::endl;
  std::string value;
  std::cout << file->read(value, 2) << std::endl;
  std::cout << value << std::endl;


  auto queue = client.open_or_create_fifo_queue("/queue.txt", "local://tmp");
  std::cout << queue->front() << std::endl;

//  file.
}
