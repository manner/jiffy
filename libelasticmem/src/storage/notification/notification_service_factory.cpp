#include <thrift/transport/TSocket.h>

#include "notification_service_factory.h"
#include "notification_service_handler.h"
#include "../../utils/logger.h"

namespace elasticmem {
namespace storage {

using namespace ::apache::thrift;
using namespace ::apache::thrift::transport;
using namespace utils;

notification_service_factory::notification_service_factory(std::vector<std::shared_ptr<subscription_map>> &subs): subs_(subs) {}

notification_serviceIf *notification_service_factory::getHandler(const TConnectionInfo &conn_info) {
  std::shared_ptr<TSocket> sock = std::dynamic_pointer_cast<TSocket>(conn_info.transport);
  LOG(info) << "Incoming connection from " << sock->getSocketInfo();
  return new notification_service_handler(conn_info.output, subs_);
}

void notification_service_factory::releaseHandler(notification_serviceIf *handler) {
  LOG(info) << "Releasing connection";
  handler->unsubscribe(-1, {});
  delete handler;
}

}
}