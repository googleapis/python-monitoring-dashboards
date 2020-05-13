# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/monitoring_dashboard_v1/proto/dashboard.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.monitoring_dashboard_v1.proto import (
    layouts_pb2 as google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_layouts__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/monitoring_dashboard_v1/proto/dashboard.proto",
    package="google.monitoring.dashboard.v1",
    syntax="proto3",
    serialized_options=b'\n"com.google.monitoring.dashboard.v1B\017DashboardsProtoP\001ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\352\002(Google::Cloud::Monitoring::Dashboard::V1',
    serialized_pb=b'\n:google/cloud/monitoring_dashboard_v1/proto/dashboard.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x38google/cloud/monitoring_dashboard_v1/proto/layouts.proto"\x92\x02\n\tDashboard\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x0c\n\x04\x65tag\x18\x04 \x01(\t\x12\x41\n\x0bgrid_layout\x18\x05 \x01(\x0b\x32*.google.monitoring.dashboard.v1.GridLayoutH\x00\x12?\n\nrow_layout\x18\x08 \x01(\x0b\x32).google.monitoring.dashboard.v1.RowLayoutH\x00\x12\x45\n\rcolumn_layout\x18\t \x01(\x0b\x32,.google.monitoring.dashboard.v1.ColumnLayoutH\x00\x42\x08\n\x06layoutB\xab\x01\n"com.google.monitoring.dashboard.v1B\x0f\x44\x61shboardsProtoP\x01ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3',
    dependencies=[
        google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_layouts__pb2.DESCRIPTOR
    ],
)


_DASHBOARD = _descriptor.Descriptor(
    name="Dashboard",
    full_name="google.monitoring.dashboard.v1.Dashboard",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.monitoring.dashboard.v1.Dashboard.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.monitoring.dashboard.v1.Dashboard.display_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="etag",
            full_name="google.monitoring.dashboard.v1.Dashboard.etag",
            index=2,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="grid_layout",
            full_name="google.monitoring.dashboard.v1.Dashboard.grid_layout",
            index=3,
            number=5,
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
        ),
        _descriptor.FieldDescriptor(
            name="row_layout",
            full_name="google.monitoring.dashboard.v1.Dashboard.row_layout",
            index=4,
            number=8,
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
        ),
        _descriptor.FieldDescriptor(
            name="column_layout",
            full_name="google.monitoring.dashboard.v1.Dashboard.column_layout",
            index=5,
            number=9,
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
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="layout",
            full_name="google.monitoring.dashboard.v1.Dashboard.layout",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=153,
    serialized_end=427,
)

_DASHBOARD.fields_by_name[
    "grid_layout"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_layouts__pb2._GRIDLAYOUT
)
_DASHBOARD.fields_by_name[
    "row_layout"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_layouts__pb2._ROWLAYOUT
)
_DASHBOARD.fields_by_name[
    "column_layout"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_layouts__pb2._COLUMNLAYOUT
)
_DASHBOARD.oneofs_by_name["layout"].fields.append(
    _DASHBOARD.fields_by_name["grid_layout"]
)
_DASHBOARD.fields_by_name["grid_layout"].containing_oneof = _DASHBOARD.oneofs_by_name[
    "layout"
]
_DASHBOARD.oneofs_by_name["layout"].fields.append(
    _DASHBOARD.fields_by_name["row_layout"]
)
_DASHBOARD.fields_by_name["row_layout"].containing_oneof = _DASHBOARD.oneofs_by_name[
    "layout"
]
_DASHBOARD.oneofs_by_name["layout"].fields.append(
    _DASHBOARD.fields_by_name["column_layout"]
)
_DASHBOARD.fields_by_name["column_layout"].containing_oneof = _DASHBOARD.oneofs_by_name[
    "layout"
]
DESCRIPTOR.message_types_by_name["Dashboard"] = _DASHBOARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dashboard = _reflection.GeneratedProtocolMessageType(
    "Dashboard",
    (_message.Message,),
    {
        "DESCRIPTOR": _DASHBOARD,
        "__module__": "google.cloud.monitoring_dashboard_v1.proto.dashboard_pb2",
        "__doc__": """A Google Stackdriver dashboard. Dashboards define the
  content and layout of pages in the Stackdriver web application.
  
  
  Attributes:
      name:
          The resource name of the dashboard.
      display_name:
          The mutable, human-readable name.
      etag:
          \ ``etag`` is used for optimistic concurrency control as a way
          to help prevent simultaneous updates of a policy from
          overwriting each other. An ``etag`` is returned in the
          response to ``GetDashboard``, and users are expected to put
          that etag in the request to ``UpdateDashboard`` to ensure that
          their change will be applied to the same version of the
          Dashboard configuration. The field should not be passed during
          dashboard creation.
      layout:
          A dashboard’s root container element that defines the layout
          style.
      grid_layout:
          Content is arranged with a basic layout that re-flows a simple
          list of informational elements like widgets or tiles.
      row_layout:
          The content is divided into equally spaced rows and the
          widgets are arranged horizontally.
      column_layout:
          The content is divided into equally spaced columns and the
          widgets are arranged vertically.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.Dashboard)
    },
)
_sym_db.RegisterMessage(Dashboard)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
