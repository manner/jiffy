#include "block_allocation_service_handler.h"

namespace elasticmem {
namespace directory {

block_allocation_service_handler::block_allocation_service_handler(std::shared_ptr<block_allocator> alloc)
    : alloc_(std::move(alloc)) {}

void block_allocation_service_handler::add_blocks(const std::vector<std::string> &block_names) {
  try {
    alloc_->add_blocks(block_names);
  } catch (std::out_of_range& e) {
    throw make_exception(e);
  }
}

void block_allocation_service_handler::remove_blocks(const std::vector<std::string> &block_names) {
  try {
    alloc_->remove_blocks(block_names);
  } catch (std::out_of_range& e) {
    throw make_exception(e);
  }
}
block_allocation_service_exception block_allocation_service_handler::make_exception(const std::out_of_range &e) {
  block_allocation_service_exception ex;
  ex.msg = e.what();
  return ex;
}

}
}