# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crypto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='crypto.proto',
  package='crypto.pb',
  syntax='proto2',
  serialized_pb=_b('\n\x0c\x63rypto.proto\x12\tcrypto.pb\";\n\tPublicKey\x12 \n\x04Type\x18\x01 \x02(\x0e\x32\x12.crypto.pb.KeyType\x12\x0c\n\x04\x44\x61ta\x18\x02 \x02(\x0c\"<\n\nPrivateKey\x12 \n\x04Type\x18\x01 \x02(\x0e\x32\x12.crypto.pb.KeyType\x12\x0c\n\x04\x44\x61ta\x18\x02 \x02(\x0c*9\n\x07KeyType\x12\x07\n\x03RSA\x10\x00\x12\x0b\n\x07\x45\x64\x32\x35\x35\x31\x39\x10\x01\x12\r\n\tSecp256k1\x10\x02\x12\t\n\x05\x45\x43\x44SA\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_KEYTYPE = _descriptor.EnumDescriptor(
  name='KeyType',
  full_name='crypto.pb.KeyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RSA', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Ed25519', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Secp256k1', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ECDSA', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=150,
  serialized_end=207,
)
_sym_db.RegisterEnumDescriptor(_KEYTYPE)

KeyType = enum_type_wrapper.EnumTypeWrapper(_KEYTYPE)
RSA = 0
Ed25519 = 1
Secp256k1 = 2
ECDSA = 3



_PUBLICKEY = _descriptor.Descriptor(
  name='PublicKey',
  full_name='crypto.pb.PublicKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='crypto.pb.PublicKey.Type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data', full_name='crypto.pb.PublicKey.Data', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=86,
)


_PRIVATEKEY = _descriptor.Descriptor(
  name='PrivateKey',
  full_name='crypto.pb.PrivateKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='crypto.pb.PrivateKey.Type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data', full_name='crypto.pb.PrivateKey.Data', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=148,
)

_PUBLICKEY.fields_by_name['Type'].enum_type = _KEYTYPE
_PRIVATEKEY.fields_by_name['Type'].enum_type = _KEYTYPE
DESCRIPTOR.message_types_by_name['PublicKey'] = _PUBLICKEY
DESCRIPTOR.message_types_by_name['PrivateKey'] = _PRIVATEKEY
DESCRIPTOR.enum_types_by_name['KeyType'] = _KEYTYPE

PublicKey = _reflection.GeneratedProtocolMessageType('PublicKey', (_message.Message,), dict(
  DESCRIPTOR = _PUBLICKEY,
  __module__ = 'crypto_pb2'
  # @@protoc_insertion_point(class_scope:crypto.pb.PublicKey)
  ))
_sym_db.RegisterMessage(PublicKey)

PrivateKey = _reflection.GeneratedProtocolMessageType('PrivateKey', (_message.Message,), dict(
  DESCRIPTOR = _PRIVATEKEY,
  __module__ = 'crypto_pb2'
  # @@protoc_insertion_point(class_scope:crypto.pb.PrivateKey)
  ))
_sym_db.RegisterMessage(PrivateKey)


# @@protoc_insertion_point(module_scope)