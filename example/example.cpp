#include <iostream>
#include <jiffy/client/jiffy_client.h>

int main() {
  std::cout << "hi" << std::endl;
  jiffy::client::jiffy_client client("127.0.0.1", 9090, 9091);
//  client.create_file("/test.txt", );
  auto file = client.open_or_create_file("/test.txt", "local://tmp");


  std::cout << "written " << file->write("testtesttesttesttest") << " bytes." << std::endl;
//  file->seek(0);
  std::string value;
//  file->read(value, 2);
  std::cout << value << std::endl;
//  client.close("/test.txt");

  // queue
  auto queue = client.open_or_create_fifo_queue("/queue.txt", "local://tmp");
  queue->enqueue("wow");
//  client.d

//  file.
}
