# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/securitycenter_v1/proto/run_asset_discovery_response.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/securitycenter_v1/proto/run_asset_discovery_response.proto",
    package="google.cloud.securitycenter.v1",
    syntax="proto3",
    serialized_options=b'\n"com.google.cloud.securitycenter.v1P\001ZLgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1;securitycenter\252\002\036Google.Cloud.SecurityCenter.V1\312\002\036Google\\Cloud\\SecurityCenter\\V1\352\002!Google::Cloud::SecurityCenter::V1',
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\nGgoogle/cloud/securitycenter_v1/proto/run_asset_discovery_response.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto"\xe7\x01\n\x19RunAssetDiscoveryResponse\x12N\n\x05state\x18\x01 \x01(\x0e\x32?.google.cloud.securitycenter.v1.RunAssetDiscoveryResponse.State\x12+\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration"M\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tCOMPLETED\x10\x01\x12\x0e\n\nSUPERSEDED\x10\x02\x12\x0e\n\nTERMINATED\x10\x03\x42\xda\x01\n"com.google.cloud.securitycenter.v1P\x01ZLgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1;securitycenter\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3',
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,
    ],
)


_RUNASSETDISCOVERYRESPONSE_STATE = _descriptor.EnumDescriptor(
    name="State",
    full_name="google.cloud.securitycenter.v1.RunAssetDiscoveryResponse.State",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="STATE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="COMPLETED",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SUPERSEDED",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TERMINATED",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=324,
    serialized_end=401,
)
_sym_db.RegisterEnumDescriptor(_RUNASSETDISCOVERYRESPONSE_STATE)


_RUNASSETDISCOVERYRESPONSE = _descriptor.Descriptor(
    name="RunAssetDiscoveryResponse",
    full_name="google.cloud.securitycenter.v1.RunAssetDiscoveryResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="state",
            full_name="google.cloud.securitycenter.v1.RunAssetDiscoveryResponse.state",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="duration",
            full_name="google.cloud.securitycenter.v1.RunAssetDiscoveryResponse.duration",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_RUNASSETDISCOVERYRESPONSE_STATE,],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=170,
    serialized_end=401,
)

_RUNASSETDISCOVERYRESPONSE.fields_by_name[
    "state"
].enum_type = _RUNASSETDISCOVERYRESPONSE_STATE
_RUNASSETDISCOVERYRESPONSE.fields_by_name[
    "duration"
].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_RUNASSETDISCOVERYRESPONSE_STATE.containing_type = _RUNASSETDISCOVERYRESPONSE
DESCRIPTOR.message_types_by_name[
    "RunAssetDiscoveryResponse"
] = _RUNASSETDISCOVERYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RunAssetDiscoveryResponse = _reflection.GeneratedProtocolMessageType(
    "RunAssetDiscoveryResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _RUNASSETDISCOVERYRESPONSE,
        "__module__": "google.cloud.securitycenter_v1.proto.run_asset_discovery_response_pb2",
        "__doc__": """Response of asset discovery run
  
  Attributes:
      state:
          The state of an asset discovery run.
      duration:
          The duration between asset discovery run start and end
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.securitycenter.v1.RunAssetDiscoveryResponse)
    },
)
_sym_db.RegisterMessage(RunAssetDiscoveryResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
