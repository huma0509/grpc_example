# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x03\x61pi\"\x1c\n\x0eGetUserRequest\x12\n\n\x02Id\x18\x01 \x01(\x05\"\x1f\n\x0fGetUserResponse\x12\x0c\n\x04Name\x18\x01 \x01(\t2E\n\x0bUserService\x12\x36\n\x07GetUser\x12\x13.api.GetUserRequest\x1a\x14.api.GetUserResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETUSERREQUEST._serialized_start=19
  _GETUSERREQUEST._serialized_end=47
  _GETUSERRESPONSE._serialized_start=49
  _GETUSERRESPONSE._serialized_end=80
  _USERSERVICE._serialized_start=82
  _USERSERVICE._serialized_end=151
# @@protoc_insertion_point(module_scope)
