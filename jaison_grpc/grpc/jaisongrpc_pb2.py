# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: jaisongrpc.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'jaisongrpc.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10jaisongrpc.proto\x12\njaisongrpc\"4\n\x13STTComponentRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\r\n\x05\x61udio\x18\x02 \x01(\x0c\"=\n\x14STTComponentResponse\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\x15\n\rcontent_chunk\x18\x02 \x01(\t\"O\n\x13T2TComponentRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\x14\n\x0csystem_input\x18\x02 \x01(\t\x12\x12\n\nuser_input\x18\x03 \x01(\t\"=\n\x14T2TComponentResponse\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\x15\n\rcontent_chunk\x18\x02 \x01(\t\"7\n\x14TTSGComponentRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"<\n\x15TTSGComponentResponse\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\x13\n\x0b\x61udio_chunk\x18\x02 \x01(\x0c\"5\n\x14TTSCComponentRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\r\n\x05\x61udio\x18\x02 \x01(\x0c\"<\n\x15TTSCComponentResponse\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\x13\n\x0b\x61udio_chunk\x18\x02 \x01(\x0c\x32g\n\x14STTComponentStreamer\x12O\n\x06invoke\x12\x1f.jaisongrpc.STTComponentRequest\x1a .jaisongrpc.STTComponentResponse\"\x00\x30\x01\x32g\n\x14T2TComponentStreamer\x12O\n\x06invoke\x12\x1f.jaisongrpc.T2TComponentRequest\x1a .jaisongrpc.T2TComponentResponse\"\x00\x30\x01\x32j\n\x15TTSGComponentStreamer\x12Q\n\x06invoke\x12 .jaisongrpc.TTSGComponentRequest\x1a!.jaisongrpc.TTSGComponentResponse\"\x00\x30\x01\x32j\n\x15TTSCComponentStreamer\x12Q\n\x06invoke\x12 .jaisongrpc.TTSCComponentRequest\x1a!.jaisongrpc.TTSCComponentResponse\"\x00\x30\x01\x42\x1c\n\rex.jaisongrpc\xa2\x02\njaisongrpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'jaisongrpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\rex.jaisongrpc\242\002\njaisongrpc'
  _globals['_STTCOMPONENTREQUEST']._serialized_start=32
  _globals['_STTCOMPONENTREQUEST']._serialized_end=84
  _globals['_STTCOMPONENTRESPONSE']._serialized_start=86
  _globals['_STTCOMPONENTRESPONSE']._serialized_end=147
  _globals['_T2TCOMPONENTREQUEST']._serialized_start=149
  _globals['_T2TCOMPONENTREQUEST']._serialized_end=228
  _globals['_T2TCOMPONENTRESPONSE']._serialized_start=230
  _globals['_T2TCOMPONENTRESPONSE']._serialized_end=291
  _globals['_TTSGCOMPONENTREQUEST']._serialized_start=293
  _globals['_TTSGCOMPONENTREQUEST']._serialized_end=348
  _globals['_TTSGCOMPONENTRESPONSE']._serialized_start=350
  _globals['_TTSGCOMPONENTRESPONSE']._serialized_end=410
  _globals['_TTSCCOMPONENTREQUEST']._serialized_start=412
  _globals['_TTSCCOMPONENTREQUEST']._serialized_end=465
  _globals['_TTSCCOMPONENTRESPONSE']._serialized_start=467
  _globals['_TTSCCOMPONENTRESPONSE']._serialized_end=527
  _globals['_STTCOMPONENTSTREAMER']._serialized_start=529
  _globals['_STTCOMPONENTSTREAMER']._serialized_end=632
  _globals['_T2TCOMPONENTSTREAMER']._serialized_start=634
  _globals['_T2TCOMPONENTSTREAMER']._serialized_end=737
  _globals['_TTSGCOMPONENTSTREAMER']._serialized_start=739
  _globals['_TTSGCOMPONENTSTREAMER']._serialized_end=845
  _globals['_TTSCCOMPONENTSTREAMER']._serialized_start=847
  _globals['_TTSCCOMPONENTSTREAMER']._serialized_end=953
# @@protoc_insertion_point(module_scope)