# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syft_proto/types/torch/v1/tensor_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft_proto.types.syft.v1 import id_pb2 as syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2
from syft_proto.types.torch.v1 import size_pb2 as syft__proto_dot_types_dot_torch_dot_v1_dot_size__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='syft_proto/types/torch/v1/tensor_data.proto',
  package='syft_proto.types.torch.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n+syft_proto/types/torch/v1/tensor_data.proto\x12\x19syft_proto.types.torch.v1\x1a!syft_proto/types/syft/v1/id.proto\x1a$syft_proto/types/torch/v1/size.proto\"\xbe\x05\n\nTensorData\x12\x35\n\x05shape\x18\x01 \x01(\x0b\x32\x1f.syft_proto.types.torch.v1.SizeR\x05shape\x12\x14\n\x05\x64type\x18\x02 \x01(\tR\x05\x64type\x12!\n\x0cis_quantized\x18\x03 \x01(\x08R\x0bisQuantized\x12\x14\n\x05scale\x18\x04 \x01(\x02R\x05scale\x12\x1d\n\nzero_point\x18\x05 \x01(\x05R\tzeroPoint\x12%\n\x0e\x63ontents_uint8\x18\x10 \x03(\rR\rcontentsUint8\x12#\n\rcontents_int8\x18\x11 \x03(\x05R\x0c\x63ontentsInt8\x12%\n\x0e\x63ontents_int16\x18\x12 \x03(\x05R\rcontentsInt16\x12%\n\x0e\x63ontents_int32\x18\x13 \x03(\x05R\rcontentsInt32\x12%\n\x0e\x63ontents_int64\x18\x14 \x03(\x03R\rcontentsInt64\x12)\n\x10\x63ontents_float16\x18\x15 \x03(\x02R\x0f\x63ontentsFloat16\x12)\n\x10\x63ontents_float32\x18\x16 \x03(\x02R\x0f\x63ontentsFloat32\x12)\n\x10\x63ontents_float64\x18\x17 \x03(\x01R\x0f\x63ontentsFloat64\x12#\n\rcontents_bool\x18\x18 \x03(\x08R\x0c\x63ontentsBool\x12%\n\x0e\x63ontents_qint8\x18\x19 \x03(\x11R\rcontentsQint8\x12\'\n\x0f\x63ontents_quint8\x18\x1a \x03(\rR\x0e\x63ontentsQuint8\x12\'\n\x0f\x63ontents_qint32\x18\x1b \x03(\x11R\x0e\x63ontentsQint32\x12+\n\x11\x63ontents_bfloat16\x18\x1c \x03(\x02R\x10\x63ontentsBfloat16b\x06proto3')
  ,
  dependencies=[syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2.DESCRIPTOR,syft__proto_dot_types_dot_torch_dot_v1_dot_size__pb2.DESCRIPTOR,])




_TENSORDATA = _descriptor.Descriptor(
  name='TensorData',
  full_name='syft_proto.types.torch.v1.TensorData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape', full_name='syft_proto.types.torch.v1.TensorData.shape', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='shape', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='syft_proto.types.torch.v1.TensorData.dtype', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='dtype', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_quantized', full_name='syft_proto.types.torch.v1.TensorData.is_quantized', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='isQuantized', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='syft_proto.types.torch.v1.TensorData.scale', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='scale', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zero_point', full_name='syft_proto.types.torch.v1.TensorData.zero_point', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='zeroPoint', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents_uint8', full_name='syft_proto.types.torch.v1.TensorData.contents_uint8', index=5,
      number=16, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsUint8', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents_int8', full_name='syft_proto.types.torch.v1.TensorData.contents_int8', index=6,
      number=17, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsInt8', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents_int16', full_name='syft_proto.types.torch.v1.TensorData.contents_int16', index=7,
      number=18, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsInt16', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents_int32', full_name='syft_proto.types.torch.v1.TensorData.contents_int32', index=8,
      number=19, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsInt32', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents_int64', full_name='syft_proto.types.torch.v1.TensorData.contents_int64', index=9,
      number=20, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsInt64', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents_float16', full_name='syft_proto.types.torch.v1.TensorData.contents_float16', index=10,
      number=21, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsFloat16', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents_float32', full_name='syft_proto.types.torch.v1.TensorData.contents_float32', index=11,
      number=22, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsFloat32', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents_float64', full_name='syft_proto.types.torch.v1.TensorData.contents_float64', index=12,
      number=23, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsFloat64', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents_bool', full_name='syft_proto.types.torch.v1.TensorData.contents_bool', index=13,
      number=24, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsBool', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents_qint8', full_name='syft_proto.types.torch.v1.TensorData.contents_qint8', index=14,
      number=25, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsQint8', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents_quint8', full_name='syft_proto.types.torch.v1.TensorData.contents_quint8', index=15,
      number=26, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsQuint8', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents_qint32', full_name='syft_proto.types.torch.v1.TensorData.contents_qint32', index=16,
      number=27, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsQint32', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents_bfloat16', full_name='syft_proto.types.torch.v1.TensorData.contents_bfloat16', index=17,
      number=28, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsBfloat16', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=850,
)

_TENSORDATA.fields_by_name['shape'].message_type = syft__proto_dot_types_dot_torch_dot_v1_dot_size__pb2._SIZE
DESCRIPTOR.message_types_by_name['TensorData'] = _TENSORDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TensorData = _reflection.GeneratedProtocolMessageType('TensorData', (_message.Message,), {
  'DESCRIPTOR' : _TENSORDATA,
  '__module__' : 'syft_proto.types.torch.v1.tensor_data_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.types.torch.v1.TensorData)
  })
_sym_db.RegisterMessage(TensorData)


# @@protoc_insertion_point(module_scope)
