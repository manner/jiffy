/**
 * Autogenerated by Thrift Compiler (0.11.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#include "directory_service_types.h"

#include <algorithm>
#include <ostream>

#include <thrift/TToString.h>

namespace jiffy { namespace directory {

int _krpc_perm_optionsValues[] = {
  rpc_replace,
  rpc_add,
  rpc_remove
};
const char* _krpc_perm_optionsNames[] = {
  "rpc_replace",
  "rpc_add",
  "rpc_remove"
};
const std::map<int, const char*> _rpc_perm_options_VALUES_TO_NAMES(::apache::thrift::TEnumIterator(3, _krpc_perm_optionsValues, _krpc_perm_optionsNames), ::apache::thrift::TEnumIterator(-1, NULL, NULL));

std::ostream& operator<<(std::ostream& out, const rpc_perm_options val) {
  std::map<int, const char*>::const_iterator it = _rpc_perm_options_VALUES_TO_NAMES.find(val);
  if (it != _rpc_perm_options_VALUES_TO_NAMES.end()) {
    out << it->second;
  } else {
    out << static_cast<int>(val);
  }
  return out;
}

int _krpc_file_typeValues[] = {
  rpc_none,
  rpc_regular,
  rpc_directory
};
const char* _krpc_file_typeNames[] = {
  "rpc_none",
  "rpc_regular",
  "rpc_directory"
};
const std::map<int, const char*> _rpc_file_type_VALUES_TO_NAMES(::apache::thrift::TEnumIterator(3, _krpc_file_typeValues, _krpc_file_typeNames), ::apache::thrift::TEnumIterator(-1, NULL, NULL));

std::ostream& operator<<(std::ostream& out, const rpc_file_type val) {
  std::map<int, const char*>::const_iterator it = _rpc_file_type_VALUES_TO_NAMES.find(val);
  if (it != _rpc_file_type_VALUES_TO_NAMES.end()) {
    out << it->second;
  } else {
    out << static_cast<int>(val);
  }
  return out;
}

int _krpc_storage_modeValues[] = {
  rpc_in_memory,
  rpc_in_memory_grace,
  rpc_on_disk
};
const char* _krpc_storage_modeNames[] = {
  "rpc_in_memory",
  "rpc_in_memory_grace",
  "rpc_on_disk"
};
const std::map<int, const char*> _rpc_storage_mode_VALUES_TO_NAMES(::apache::thrift::TEnumIterator(3, _krpc_storage_modeValues, _krpc_storage_modeNames), ::apache::thrift::TEnumIterator(-1, NULL, NULL));

std::ostream& operator<<(std::ostream& out, const rpc_storage_mode val) {
  std::map<int, const char*>::const_iterator it = _rpc_storage_mode_VALUES_TO_NAMES.find(val);
  if (it != _rpc_storage_mode_VALUES_TO_NAMES.end()) {
    out << it->second;
  } else {
    out << static_cast<int>(val);
  }
  return out;
}


rpc_replica_chain::~rpc_replica_chain() throw() {
}


void rpc_replica_chain::__set_block_ids(const std::vector<std::string> & val) {
  this->block_ids = val;
}

void rpc_replica_chain::__set_name(const std::string& val) {
  this->name = val;
}

void rpc_replica_chain::__set_metadata(const std::string& val) {
  this->metadata = val;
}

void rpc_replica_chain::__set_storage_mode(const rpc_storage_mode val) {
  this->storage_mode = val;
}
std::ostream& operator<<(std::ostream& out, const rpc_replica_chain& obj)
{
  obj.printTo(out);
  return out;
}


void swap(rpc_replica_chain &a, rpc_replica_chain &b) {
  using ::std::swap;
  swap(a.block_ids, b.block_ids);
  swap(a.name, b.name);
  swap(a.metadata, b.metadata);
  swap(a.storage_mode, b.storage_mode);
}

rpc_replica_chain::rpc_replica_chain(const rpc_replica_chain& other7) {
  block_ids = other7.block_ids;
  name = other7.name;
  metadata = other7.metadata;
  storage_mode = other7.storage_mode;
}
rpc_replica_chain& rpc_replica_chain::operator=(const rpc_replica_chain& other8) {
  block_ids = other8.block_ids;
  name = other8.name;
  metadata = other8.metadata;
  storage_mode = other8.storage_mode;
  return *this;
}
void rpc_replica_chain::printTo(std::ostream& out) const {
  using ::apache::thrift::to_string;
  out << "rpc_replica_chain(";
  out << "block_ids=" << to_string(block_ids);
  out << ", " << "name=" << to_string(name);
  out << ", " << "metadata=" << to_string(metadata);
  out << ", " << "storage_mode=" << to_string(storage_mode);
  out << ")";
}


rpc_file_status::~rpc_file_status() throw() {
}


void rpc_file_status::__set_type(const rpc_file_type val) {
  this->type = val;
}

void rpc_file_status::__set_permissions(const rpc_perms val) {
  this->permissions = val;
}

void rpc_file_status::__set_last_write_time(const int64_t val) {
  this->last_write_time = val;
}
std::ostream& operator<<(std::ostream& out, const rpc_file_status& obj)
{
  obj.printTo(out);
  return out;
}


void swap(rpc_file_status &a, rpc_file_status &b) {
  using ::std::swap;
  swap(a.type, b.type);
  swap(a.permissions, b.permissions);
  swap(a.last_write_time, b.last_write_time);
}

rpc_file_status::rpc_file_status(const rpc_file_status& other10) {
  type = other10.type;
  permissions = other10.permissions;
  last_write_time = other10.last_write_time;
}
rpc_file_status& rpc_file_status::operator=(const rpc_file_status& other11) {
  type = other11.type;
  permissions = other11.permissions;
  last_write_time = other11.last_write_time;
  return *this;
}
void rpc_file_status::printTo(std::ostream& out) const {
  using ::apache::thrift::to_string;
  out << "rpc_file_status(";
  out << "type=" << to_string(type);
  out << ", " << "permissions=" << to_string(permissions);
  out << ", " << "last_write_time=" << to_string(last_write_time);
  out << ")";
}


rpc_data_status::~rpc_data_status() throw() {
}


void rpc_data_status::__set_type(const std::string& val) {
  this->type = val;
}

void rpc_data_status::__set_backing_path(const std::string& val) {
  this->backing_path = val;
}

void rpc_data_status::__set_chain_length(const int32_t val) {
  this->chain_length = val;
}

void rpc_data_status::__set_data_blocks(const std::vector<rpc_replica_chain> & val) {
  this->data_blocks = val;
}

void rpc_data_status::__set_flags(const int32_t val) {
  this->flags = val;
}

void rpc_data_status::__set_tags(const std::map<std::string, std::string> & val) {
  this->tags = val;
}
std::ostream& operator<<(std::ostream& out, const rpc_data_status& obj)
{
  obj.printTo(out);
  return out;
}


void swap(rpc_data_status &a, rpc_data_status &b) {
  using ::std::swap;
  swap(a.type, b.type);
  swap(a.backing_path, b.backing_path);
  swap(a.chain_length, b.chain_length);
  swap(a.data_blocks, b.data_blocks);
  swap(a.flags, b.flags);
  swap(a.tags, b.tags);
}

rpc_data_status::rpc_data_status(const rpc_data_status& other26) {
  type = other26.type;
  backing_path = other26.backing_path;
  chain_length = other26.chain_length;
  data_blocks = other26.data_blocks;
  flags = other26.flags;
  tags = other26.tags;
}
rpc_data_status& rpc_data_status::operator=(const rpc_data_status& other27) {
  type = other27.type;
  backing_path = other27.backing_path;
  chain_length = other27.chain_length;
  data_blocks = other27.data_blocks;
  flags = other27.flags;
  tags = other27.tags;
  return *this;
}
void rpc_data_status::printTo(std::ostream& out) const {
  using ::apache::thrift::to_string;
  out << "rpc_data_status(";
  out << "type=" << to_string(type);
  out << ", " << "backing_path=" << to_string(backing_path);
  out << ", " << "chain_length=" << to_string(chain_length);
  out << ", " << "data_blocks=" << to_string(data_blocks);
  out << ", " << "flags=" << to_string(flags);
  out << ", " << "tags=" << to_string(tags);
  out << ")";
}


rpc_dir_entry::~rpc_dir_entry() throw() {
}


void rpc_dir_entry::__set_name(const std::string& val) {
  this->name = val;
}

void rpc_dir_entry::__set_status(const rpc_file_status& val) {
  this->status = val;
}
std::ostream& operator<<(std::ostream& out, const rpc_dir_entry& obj)
{
  obj.printTo(out);
  return out;
}


void swap(rpc_dir_entry &a, rpc_dir_entry &b) {
  using ::std::swap;
  swap(a.name, b.name);
  swap(a.status, b.status);
}

rpc_dir_entry::rpc_dir_entry(const rpc_dir_entry& other28) {
  name = other28.name;
  status = other28.status;
}
rpc_dir_entry& rpc_dir_entry::operator=(const rpc_dir_entry& other29) {
  name = other29.name;
  status = other29.status;
  return *this;
}
void rpc_dir_entry::printTo(std::ostream& out) const {
  using ::apache::thrift::to_string;
  out << "rpc_dir_entry(";
  out << "name=" << to_string(name);
  out << ", " << "status=" << to_string(status);
  out << ")";
}


directory_service_exception::~directory_service_exception() throw() {
}


void directory_service_exception::__set_msg(const std::string& val) {
  this->msg = val;
}
std::ostream& operator<<(std::ostream& out, const directory_service_exception& obj)
{
  obj.printTo(out);
  return out;
}


void swap(directory_service_exception &a, directory_service_exception &b) {
  using ::std::swap;
  swap(a.msg, b.msg);
}

directory_service_exception::directory_service_exception(const directory_service_exception& other30) : TException() {
  msg = other30.msg;
}
directory_service_exception& directory_service_exception::operator=(const directory_service_exception& other31) {
  msg = other31.msg;
  return *this;
}
void directory_service_exception::printTo(std::ostream& out) const {
  using ::apache::thrift::to_string;
  out << "directory_service_exception(";
  out << "msg=" << to_string(msg);
  out << ")";
}

const char* directory_service_exception::what() const throw() {
  try {
    std::stringstream ss;
    ss << "TException - service has thrown: " << *this;
    this->thriftTExceptionMessageHolder_ = ss.str();
    return this->thriftTExceptionMessageHolder_.c_str();
  } catch (const std::exception&) {
    return "TException - service has thrown: directory_service_exception";
  }
}

}} // namespace
