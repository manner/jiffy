#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class response_type(object):
    subscribe = 0
    unsubscribe = 1

    _VALUES_TO_NAMES = {
        0: "subscribe",
        1: "unsubscribe",
    }

    _NAMES_TO_VALUES = {
        "subscribe": 0,
        "unsubscribe": 1,
    }
fix_spec(all_structs)
del all_structs
