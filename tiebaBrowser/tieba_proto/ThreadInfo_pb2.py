# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ThreadInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import User_pb2 as User__pb2
from . import PbContent_pb2 as PbContent__pb2
from . import Agree_pb2 as Agree__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10ThreadInfo.proto\x1a\nUser.proto\x1a\x0fPbContent.proto\x1a\x0b\x41gree.proto\"\xb1\x01\n\x08PollInfo\x12\x10\n\x08is_multi\x18\x02 \x01(\x05\x12\x11\n\ttotal_num\x18\x03 \x01(\x03\x12%\n\x07options\x18\t \x03(\x0b\x32\x14.PollInfo.PollOption\x12\x12\n\ntotal_poll\x18\x0b \x01(\x03\x12\r\n\x05title\x18\x0c \x01(\t\x1a\x36\n\nPollOption\x12\x0b\n\x03num\x18\x02 \x01(\x03\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\r\n\x05image\x18\x04 \x01(\t\"\xcd\x05\n\nThreadInfo\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x03 \x01(\t\x12\x11\n\treply_num\x18\x04 \x01(\x05\x12\x10\n\x08view_num\x18\x05 \x01(\x05\x12\x15\n\rlast_time_int\x18\x07 \x01(\x05\x12\x0e\n\x06is_top\x18\t \x01(\x05\x12\x0f\n\x07is_good\x18\n \x01(\x05\x12\x17\n\x0fis_voice_thread\x18\x0f \x01(\x05\x12\x15\n\x06\x61uthor\x18\x12 \x01(\x0b\x32\x05.User\x12\x0b\n\x03\x66id\x18\x1b \x01(\x03\x12\x13\n\x0bis_livepost\x18\x1e \x01(\x05\x12\x15\n\rfirst_post_id\x18( \x01(\x03\x12\x13\n\x0b\x63reate_time\x18- \x01(\x05\x12\x11\n\tauthor_id\x18\x38 \x01(\x03\x12\r\n\x05is_ad\x18; \x01(\r\x12\x1c\n\tpoll_info\x18J \x01(\x0b\x32\t.PollInfo\x12\x1e\n\x16is_godthread_recommend\x18U \x01(\x05\x12\x15\n\x05\x61gree\x18~ \x01(\x0b\x32\x06.Agree\x12\x12\n\tshare_num\x18\x87\x01 \x01(\x05\x12\x39\n\x12origin_thread_info\x18\x8d\x01 \x01(\x0b\x32\x1c.ThreadInfo.OriginThreadInfo\x12\'\n\x12\x66irst_post_content\x18\x8e\x01 \x03(\x0b\x32\n.PbContent\x12\x18\n\x0fis_share_thread\x18\x8f\x01 \x01(\x05\x12\x0f\n\x06tab_id\x18\xaf\x01 \x01(\x05\x12\x13\n\nis_deleted\x18\xb5\x01 \x01(\x05\x12\x14\n\x0bis_frs_mask\x18\xc6\x01 \x01(\x05\x1a\x83\x01\n\x10OriginThreadInfo\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0b\n\x03tid\x18\x05 \x01(\t\x12\x0b\n\x03\x66id\x18\x07 \x01(\x03\x12\x1b\n\x07\x63ontent\x18\x0e \x03(\x0b\x32\n.PbContent\x12\x1c\n\tpoll_info\x18\x15 \x01(\x0b\x32\t.PollInfo\x12\x0b\n\x03pid\x18\x19 \x01(\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ThreadInfo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POLLINFO._serialized_start=63
  _POLLINFO._serialized_end=240
  _POLLINFO_POLLOPTION._serialized_start=186
  _POLLINFO_POLLOPTION._serialized_end=240
  _THREADINFO._serialized_start=243
  _THREADINFO._serialized_end=960
  _THREADINFO_ORIGINTHREADINFO._serialized_start=829
  _THREADINFO_ORIGINTHREADINFO._serialized_end=960
# @@protoc_insertion_point(module_scope)
