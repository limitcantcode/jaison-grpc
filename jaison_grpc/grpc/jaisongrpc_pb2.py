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


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10jaisongrpc.proto\x12\njaisongrpc\x1a\x1bgoogle/protobuf/empty.proto\"\xa2\x01\n\x08Metadata\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x1d\n\x15is_windows_compatible\x18\x04 \x01(\x08\x12\x1a\n\x12is_unix_compatible\x18\x05 \x01(\x08\x12\x1a\n\x12windows_run_script\x18\x06 \x01(\t\x12\x17\n\x0funix_run_script\x18\x07 \x01(\t\"q\n\x13STTComponentRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\r\n\x05\x61udio\x18\x02 \x01(\x0c\x12\x10\n\x08\x63hannels\x18\x03 \x01(\x05\x12\x14\n\x0csample_width\x18\x04 \x01(\x05\x12\x13\n\x0bsample_rate\x18\x05 \x01(\x05\"=\n\x14STTComponentResponse\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\x15\n\rcontent_chunk\x18\x02 \x01(\t\"O\n\x13T2TComponentRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\x14\n\x0csystem_input\x18\x02 \x01(\t\x12\x12\n\nuser_input\x18\x03 \x01(\t\"=\n\x14T2TComponentResponse\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\x15\n\rcontent_chunk\x18\x02 \x01(\t\"7\n\x14TTSGComponentRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"y\n\x15TTSGComponentResponse\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\x13\n\x0b\x61udio_chunk\x18\x02 \x01(\x0c\x12\x10\n\x08\x63hannels\x18\x03 \x01(\x05\x12\x14\n\x0csample_width\x18\x04 \x01(\x05\x12\x13\n\x0bsample_rate\x18\x05 \x01(\x05\"r\n\x14TTSCComponentRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\r\n\x05\x61udio\x18\x02 \x01(\x0c\x12\x10\n\x08\x63hannels\x18\x03 \x01(\x05\x12\x14\n\x0csample_width\x18\x04 \x01(\x05\x12\x13\n\x0bsample_rate\x18\x05 \x01(\x05\"y\n\x15TTSCComponentResponse\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\x13\n\x0b\x61udio_chunk\x18\x02 \x01(\x0c\x12\x10\n\x08\x63hannels\x18\x03 \x01(\x05\x12\x14\n\x0csample_width\x18\x04 \x01(\x05\x12\x13\n\x0bsample_rate\x18\x05 \x01(\x05\x32N\n\x10MetadataInformer\x12:\n\x08metadata\x12\x16.google.protobuf.Empty\x1a\x14.jaisongrpc.Metadata\"\x00\x32i\n\x14STTComponentStreamer\x12Q\n\x06invoke\x12\x1f.jaisongrpc.STTComponentRequest\x1a .jaisongrpc.STTComponentResponse\"\x00(\x01\x30\x01\x32i\n\x14T2TComponentStreamer\x12Q\n\x06invoke\x12\x1f.jaisongrpc.T2TComponentRequest\x1a .jaisongrpc.T2TComponentResponse\"\x00(\x01\x30\x01\x32l\n\x15TTSGComponentStreamer\x12S\n\x06invoke\x12 .jaisongrpc.TTSGComponentRequest\x1a!.jaisongrpc.TTSGComponentResponse\"\x00(\x01\x30\x01\x32l\n\x15TTSCComponentStreamer\x12S\n\x06invoke\x12 .jaisongrpc.TTSCComponentRequest\x1a!.jaisongrpc.TTSCComponentResponse\"\x00(\x01\x30\x01\x42\x1c\n\rex.jaisongrpc\xa2\x02\njaisongrpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'jaisongrpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\rex.jaisongrpc\242\002\njaisongrpc'
  _globals['_METADATA']._serialized_start=62
  _globals['_METADATA']._serialized_end=224
  _globals['_STTCOMPONENTREQUEST']._serialized_start=226
  _globals['_STTCOMPONENTREQUEST']._serialized_end=339
  _globals['_STTCOMPONENTRESPONSE']._serialized_start=341
  _globals['_STTCOMPONENTRESPONSE']._serialized_end=402
  _globals['_T2TCOMPONENTREQUEST']._serialized_start=404
  _globals['_T2TCOMPONENTREQUEST']._serialized_end=483
  _globals['_T2TCOMPONENTRESPONSE']._serialized_start=485
  _globals['_T2TCOMPONENTRESPONSE']._serialized_end=546
  _globals['_TTSGCOMPONENTREQUEST']._serialized_start=548
  _globals['_TTSGCOMPONENTREQUEST']._serialized_end=603
  _globals['_TTSGCOMPONENTRESPONSE']._serialized_start=605
  _globals['_TTSGCOMPONENTRESPONSE']._serialized_end=726
  _globals['_TTSCCOMPONENTREQUEST']._serialized_start=728
  _globals['_TTSCCOMPONENTREQUEST']._serialized_end=842
  _globals['_TTSCCOMPONENTRESPONSE']._serialized_start=844
  _globals['_TTSCCOMPONENTRESPONSE']._serialized_end=965
  _globals['_METADATAINFORMER']._serialized_start=967
  _globals['_METADATAINFORMER']._serialized_end=1045
  _globals['_STTCOMPONENTSTREAMER']._serialized_start=1047
  _globals['_STTCOMPONENTSTREAMER']._serialized_end=1152
  _globals['_T2TCOMPONENTSTREAMER']._serialized_start=1154
  _globals['_T2TCOMPONENTSTREAMER']._serialized_end=1259
  _globals['_TTSGCOMPONENTSTREAMER']._serialized_start=1261
  _globals['_TTSGCOMPONENTSTREAMER']._serialized_end=1369
  _globals['_TTSCCOMPONENTSTREAMER']._serialized_start=1371
  _globals['_TTSCCOMPONENTSTREAMER']._serialized_end=1479
# @@protoc_insertion_point(module_scope)
