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


class rpc_perm_options(object):
    rpc_replace = 0
    rpc_add = 1
    rpc_remove = 2

    _VALUES_TO_NAMES = {
        0: "rpc_replace",
        1: "rpc_add",
        2: "rpc_remove",
    }

    _NAMES_TO_VALUES = {
        "rpc_replace": 0,
        "rpc_add": 1,
        "rpc_remove": 2,
    }


class rpc_file_type(object):
    rpc_none = 0
    rpc_regular = 1
    rpc_directory = 2

    _VALUES_TO_NAMES = {
        0: "rpc_none",
        1: "rpc_regular",
        2: "rpc_directory",
    }

    _NAMES_TO_VALUES = {
        "rpc_none": 0,
        "rpc_regular": 1,
        "rpc_directory": 2,
    }


class rpc_storage_mode(object):
    rpc_in_memory = 0
    rpc_in_memory_grace = 1
    rpc_flushing = 2
    rpc_on_disk = 3

    _VALUES_TO_NAMES = {
        0: "rpc_in_memory",
        1: "rpc_in_memory_grace",
        2: "rpc_flushing",
        3: "rpc_on_disk",
    }

    _NAMES_TO_VALUES = {
        "rpc_in_memory": 0,
        "rpc_in_memory_grace": 1,
        "rpc_flushing": 2,
        "rpc_on_disk": 3,
    }


class rpc_file_status(object):
    """
    Attributes:
     - type
     - permissions
     - last_write_time
    """


    def __init__(self, type=None, permissions=None, last_write_time=None,):
        self.type = type
        self.permissions = permissions
        self.last_write_time = last_write_time

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.permissions = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.last_write_time = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('rpc_file_status')
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.permissions is not None:
            oprot.writeFieldBegin('permissions', TType.I32, 2)
            oprot.writeI32(self.permissions)
            oprot.writeFieldEnd()
        if self.last_write_time is not None:
            oprot.writeFieldBegin('last_write_time', TType.I64, 3)
            oprot.writeI64(self.last_write_time)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.type is None:
            raise TProtocolException(message='Required field type is unset!')
        if self.permissions is None:
            raise TProtocolException(message='Required field permissions is unset!')
        if self.last_write_time is None:
            raise TProtocolException(message='Required field last_write_time is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class rpc_data_status(object):
    """
    Attributes:
     - storage_mode
     - persistent_store_prefix
     - data_blocks
    """


    def __init__(self, storage_mode=None, persistent_store_prefix=None, data_blocks=None,):
        self.storage_mode = storage_mode
        self.persistent_store_prefix = persistent_store_prefix
        self.data_blocks = data_blocks

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.storage_mode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.persistent_store_prefix = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.data_blocks = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.data_blocks.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('rpc_data_status')
        if self.storage_mode is not None:
            oprot.writeFieldBegin('storage_mode', TType.I32, 1)
            oprot.writeI32(self.storage_mode)
            oprot.writeFieldEnd()
        if self.persistent_store_prefix is not None:
            oprot.writeFieldBegin('persistent_store_prefix', TType.STRING, 2)
            oprot.writeString(self.persistent_store_prefix.encode('utf-8') if sys.version_info[0] == 2 else self.persistent_store_prefix)
            oprot.writeFieldEnd()
        if self.data_blocks is not None:
            oprot.writeFieldBegin('data_blocks', TType.LIST, 3)
            oprot.writeListBegin(TType.STRING, len(self.data_blocks))
            for iter6 in self.data_blocks:
                oprot.writeString(iter6.encode('utf-8') if sys.version_info[0] == 2 else iter6)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.storage_mode is None:
            raise TProtocolException(message='Required field storage_mode is unset!')
        if self.persistent_store_prefix is None:
            raise TProtocolException(message='Required field persistent_store_prefix is unset!')
        if self.data_blocks is None:
            raise TProtocolException(message='Required field data_blocks is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class rpc_dir_entry(object):
    """
    Attributes:
     - name
     - status
    """


    def __init__(self, name=None, status=None,):
        self.name = name
        self.status = status

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.status = rpc_file_status()
                    self.status.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('rpc_dir_entry')
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.STRUCT, 2)
            self.status.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.name is None:
            raise TProtocolException(message='Required field name is unset!')
        if self.status is None:
            raise TProtocolException(message='Required field status is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class directory_rpc_service_exception(TException):
    """
    Attributes:
     - msg
    """


    def __init__(self, msg=None,):
        self.msg = msg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.msg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('directory_rpc_service_exception')
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRING, 1)
            oprot.writeString(self.msg.encode('utf-8') if sys.version_info[0] == 2 else self.msg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.msg is None:
            raise TProtocolException(message='Required field msg is unset!')
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class rpc_file_metadata(object):
    """
    Attributes:
     - path
     - bytes
    """


    def __init__(self, path=None, bytes=None,):
        self.path = path
        self.bytes = bytes

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.path = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.bytes = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('rpc_file_metadata')
        if self.path is not None:
            oprot.writeFieldBegin('path', TType.STRING, 1)
            oprot.writeString(self.path.encode('utf-8') if sys.version_info[0] == 2 else self.path)
            oprot.writeFieldEnd()
        if self.bytes is not None:
            oprot.writeFieldBegin('bytes', TType.I64, 2)
            oprot.writeI64(self.bytes)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.path is None:
            raise TProtocolException(message='Required field path is unset!')
        if self.bytes is None:
            raise TProtocolException(message='Required field bytes is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class lease_update(object):
    """
    Attributes:
     - to_renew
     - to_flush
     - to_remove
    """


    def __init__(self, to_renew=None, to_flush=None, to_remove=None,):
        self.to_renew = to_renew
        self.to_flush = to_flush
        self.to_remove = to_remove

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.to_renew = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = rpc_file_metadata()
                        _elem12.read(iprot)
                        self.to_renew.append(_elem12)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.to_flush = []
                    (_etype16, _size13) = iprot.readListBegin()
                    for _i17 in range(_size13):
                        _elem18 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.to_flush.append(_elem18)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.to_remove = []
                    (_etype22, _size19) = iprot.readListBegin()
                    for _i23 in range(_size19):
                        _elem24 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.to_remove.append(_elem24)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('lease_update')
        if self.to_renew is not None:
            oprot.writeFieldBegin('to_renew', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.to_renew))
            for iter25 in self.to_renew:
                iter25.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.to_flush is not None:
            oprot.writeFieldBegin('to_flush', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.to_flush))
            for iter26 in self.to_flush:
                oprot.writeString(iter26.encode('utf-8') if sys.version_info[0] == 2 else iter26)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.to_remove is not None:
            oprot.writeFieldBegin('to_remove', TType.LIST, 3)
            oprot.writeListBegin(TType.STRING, len(self.to_remove))
            for iter27 in self.to_remove:
                oprot.writeString(iter27.encode('utf-8') if sys.version_info[0] == 2 else iter27)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.to_renew is None:
            raise TProtocolException(message='Required field to_renew is unset!')
        if self.to_flush is None:
            raise TProtocolException(message='Required field to_flush is unset!')
        if self.to_remove is None:
            raise TProtocolException(message='Required field to_remove is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class lease_ack(object):
    """
    Attributes:
     - renewed
     - flushed
     - removed
    """


    def __init__(self, renewed=None, flushed=None, removed=None,):
        self.renewed = renewed
        self.flushed = flushed
        self.removed = removed

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.renewed = []
                    (_etype31, _size28) = iprot.readListBegin()
                    for _i32 in range(_size28):
                        _elem33 = rpc_file_metadata()
                        _elem33.read(iprot)
                        self.renewed.append(_elem33)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.flushed = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.removed = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('lease_ack')
        if self.renewed is not None:
            oprot.writeFieldBegin('renewed', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.renewed))
            for iter34 in self.renewed:
                iter34.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.flushed is not None:
            oprot.writeFieldBegin('flushed', TType.I64, 2)
            oprot.writeI64(self.flushed)
            oprot.writeFieldEnd()
        if self.removed is not None:
            oprot.writeFieldBegin('removed', TType.I64, 3)
            oprot.writeI64(self.removed)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.renewed is None:
            raise TProtocolException(message='Required field renewed is unset!')
        if self.flushed is None:
            raise TProtocolException(message='Required field flushed is unset!')
        if self.removed is None:
            raise TProtocolException(message='Required field removed is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class directory_lease_service_exception(TException):
    """
    Attributes:
     - msg
    """


    def __init__(self, msg=None,):
        self.msg = msg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.msg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('directory_lease_service_exception')
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRING, 1)
            oprot.writeString(self.msg.encode('utf-8') if sys.version_info[0] == 2 else self.msg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(rpc_file_status)
rpc_file_status.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'type', None, None, ),  # 1
    (2, TType.I32, 'permissions', None, None, ),  # 2
    (3, TType.I64, 'last_write_time', None, None, ),  # 3
)
all_structs.append(rpc_data_status)
rpc_data_status.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'storage_mode', None, None, ),  # 1
    (2, TType.STRING, 'persistent_store_prefix', 'UTF8', None, ),  # 2
    (3, TType.LIST, 'data_blocks', (TType.STRING, 'UTF8', False), None, ),  # 3
)
all_structs.append(rpc_dir_entry)
rpc_dir_entry.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'name', 'UTF8', None, ),  # 1
    (2, TType.STRUCT, 'status', [rpc_file_status, None], None, ),  # 2
)
all_structs.append(directory_rpc_service_exception)
directory_rpc_service_exception.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'msg', 'UTF8', None, ),  # 1
)
all_structs.append(rpc_file_metadata)
rpc_file_metadata.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'path', 'UTF8', None, ),  # 1
    (2, TType.I64, 'bytes', None, None, ),  # 2
)
all_structs.append(lease_update)
lease_update.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'to_renew', (TType.STRUCT, [rpc_file_metadata, None], False), None, ),  # 1
    (2, TType.LIST, 'to_flush', (TType.STRING, 'UTF8', False), None, ),  # 2
    (3, TType.LIST, 'to_remove', (TType.STRING, 'UTF8', False), None, ),  # 3
)
all_structs.append(lease_ack)
lease_ack.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'renewed', (TType.STRUCT, [rpc_file_metadata, None], False), None, ),  # 1
    (2, TType.I64, 'flushed', None, None, ),  # 2
    (3, TType.I64, 'removed', None, None, ),  # 3
)
all_structs.append(directory_lease_service_exception)
directory_lease_service_exception.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'msg', 'UTF8', None, ),  # 1
)
fix_spec(all_structs)
del all_structs