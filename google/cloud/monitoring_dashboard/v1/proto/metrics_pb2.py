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
# source: google/cloud/monitoring_dashboard_v1/proto/metrics.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.monitoring_dashboard.v1.proto import (
    common_pb2 as google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_common__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/monitoring_dashboard_v1/proto/metrics.proto",
    package="google.monitoring.dashboard.v1",
    syntax="proto3",
    serialized_options=b'\n"com.google.monitoring.dashboard.v1B\014MetricsProtoP\001ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\352\002(Google::Cloud::Monitoring::Dashboard::V1',
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n8google/cloud/monitoring_dashboard_v1/proto/metrics.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x37google/cloud/monitoring_dashboard_v1/proto/common.proto"\x83\x02\n\x0fTimeSeriesQuery\x12N\n\x12time_series_filter\x18\x01 \x01(\x0b\x32\x30.google.monitoring.dashboard.v1.TimeSeriesFilterH\x00\x12Y\n\x18time_series_filter_ratio\x18\x02 \x01(\x0b\x32\x35.google.monitoring.dashboard.v1.TimeSeriesFilterRatioH\x00\x12$\n\x1atime_series_query_language\x18\x03 \x01(\tH\x00\x12\x15\n\runit_override\x18\x05 \x01(\tB\x08\n\x06source"\x8a\x03\n\x10TimeSeriesFilter\x12\x13\n\x06\x66ilter\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12@\n\x0b\x61ggregation\x18\x02 \x01(\x0b\x32+.google.monitoring.dashboard.v1.Aggregation\x12J\n\x15secondary_aggregation\x18\x03 \x01(\x0b\x32+.google.monitoring.dashboard.v1.Aggregation\x12W\n\x17pick_time_series_filter\x18\x04 \x01(\x0b\x32\x34.google.monitoring.dashboard.v1.PickTimeSeriesFilterH\x00\x12i\n\x1estatistical_time_series_filter\x18\x05 \x01(\x0b\x32;.google.monitoring.dashboard.v1.StatisticalTimeSeriesFilterB\x02\x18\x01H\x00\x42\x0f\n\routput_filter"\xc6\x04\n\x15TimeSeriesFilterRatio\x12R\n\tnumerator\x18\x01 \x01(\x0b\x32?.google.monitoring.dashboard.v1.TimeSeriesFilterRatio.RatioPart\x12T\n\x0b\x64\x65nominator\x18\x02 \x01(\x0b\x32?.google.monitoring.dashboard.v1.TimeSeriesFilterRatio.RatioPart\x12J\n\x15secondary_aggregation\x18\x03 \x01(\x0b\x32+.google.monitoring.dashboard.v1.Aggregation\x12W\n\x17pick_time_series_filter\x18\x04 \x01(\x0b\x32\x34.google.monitoring.dashboard.v1.PickTimeSeriesFilterH\x00\x12i\n\x1estatistical_time_series_filter\x18\x05 \x01(\x0b\x32;.google.monitoring.dashboard.v1.StatisticalTimeSeriesFilterB\x02\x18\x01H\x00\x1a\x62\n\tRatioPart\x12\x13\n\x06\x66ilter\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12@\n\x0b\x61ggregation\x18\x02 \x01(\x0b\x32+.google.monitoring.dashboard.v1.AggregationB\x0f\n\routput_filter"\xa4\x02\n\tThreshold\x12\r\n\x05label\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\x12>\n\x05\x63olor\x18\x03 \x01(\x0e\x32/.google.monitoring.dashboard.v1.Threshold.Color\x12\x46\n\tdirection\x18\x04 \x01(\x0e\x32\x33.google.monitoring.dashboard.v1.Threshold.Direction"3\n\x05\x43olor\x12\x15\n\x11\x43OLOR_UNSPECIFIED\x10\x00\x12\n\n\x06YELLOW\x10\x04\x12\x07\n\x03RED\x10\x06"<\n\tDirection\x12\x19\n\x15\x44IRECTION_UNSPECIFIED\x10\x00\x12\t\n\x05\x41\x42OVE\x10\x01\x12\t\n\x05\x42\x45LOW\x10\x02*Q\n\x0eSparkChartType\x12 \n\x1cSPARK_CHART_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nSPARK_LINE\x10\x01\x12\r\n\tSPARK_BAR\x10\x02\x42\xa8\x01\n"com.google.monitoring.dashboard.v1B\x0cMetricsProtoP\x01ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3',
    dependencies=[
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_common__pb2.DESCRIPTOR,
    ],
)

_SPARKCHARTTYPE = _descriptor.EnumDescriptor(
    name="SparkChartType",
    full_name="google.monitoring.dashboard.v1.SparkChartType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="SPARK_CHART_TYPE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SPARK_LINE",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SPARK_BAR",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1721,
    serialized_end=1802,
)
_sym_db.RegisterEnumDescriptor(_SPARKCHARTTYPE)

SparkChartType = enum_type_wrapper.EnumTypeWrapper(_SPARKCHARTTYPE)
SPARK_CHART_TYPE_UNSPECIFIED = 0
SPARK_LINE = 1
SPARK_BAR = 2


_THRESHOLD_COLOR = _descriptor.EnumDescriptor(
    name="Color",
    full_name="google.monitoring.dashboard.v1.Threshold.Color",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="COLOR_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="YELLOW",
            index=1,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="RED",
            index=2,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1606,
    serialized_end=1657,
)
_sym_db.RegisterEnumDescriptor(_THRESHOLD_COLOR)

_THRESHOLD_DIRECTION = _descriptor.EnumDescriptor(
    name="Direction",
    full_name="google.monitoring.dashboard.v1.Threshold.Direction",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="DIRECTION_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ABOVE",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="BELOW",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1659,
    serialized_end=1719,
)
_sym_db.RegisterEnumDescriptor(_THRESHOLD_DIRECTION)


_TIMESERIESQUERY = _descriptor.Descriptor(
    name="TimeSeriesQuery",
    full_name="google.monitoring.dashboard.v1.TimeSeriesQuery",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="time_series_filter",
            full_name="google.monitoring.dashboard.v1.TimeSeriesQuery.time_series_filter",
            index=0,
            number=1,
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
        _descriptor.FieldDescriptor(
            name="time_series_filter_ratio",
            full_name="google.monitoring.dashboard.v1.TimeSeriesQuery.time_series_filter_ratio",
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
        _descriptor.FieldDescriptor(
            name="time_series_query_language",
            full_name="google.monitoring.dashboard.v1.TimeSeriesQuery.time_series_query_language",
            index=2,
            number=3,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="unit_override",
            full_name="google.monitoring.dashboard.v1.TimeSeriesQuery.unit_override",
            index=3,
            number=5,
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
            create_key=_descriptor._internal_create_key,
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
            name="source",
            full_name="google.monitoring.dashboard.v1.TimeSeriesQuery.source",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=183,
    serialized_end=442,
)


_TIMESERIESFILTER = _descriptor.Descriptor(
    name="TimeSeriesFilter",
    full_name="google.monitoring.dashboard.v1.TimeSeriesFilter",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="filter",
            full_name="google.monitoring.dashboard.v1.TimeSeriesFilter.filter",
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
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="aggregation",
            full_name="google.monitoring.dashboard.v1.TimeSeriesFilter.aggregation",
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
        _descriptor.FieldDescriptor(
            name="secondary_aggregation",
            full_name="google.monitoring.dashboard.v1.TimeSeriesFilter.secondary_aggregation",
            index=2,
            number=3,
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
        _descriptor.FieldDescriptor(
            name="pick_time_series_filter",
            full_name="google.monitoring.dashboard.v1.TimeSeriesFilter.pick_time_series_filter",
            index=3,
            number=4,
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
        _descriptor.FieldDescriptor(
            name="statistical_time_series_filter",
            full_name="google.monitoring.dashboard.v1.TimeSeriesFilter.statistical_time_series_filter",
            index=4,
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
            serialized_options=b"\030\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
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
            name="output_filter",
            full_name="google.monitoring.dashboard.v1.TimeSeriesFilter.output_filter",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=445,
    serialized_end=839,
)


_TIMESERIESFILTERRATIO_RATIOPART = _descriptor.Descriptor(
    name="RatioPart",
    full_name="google.monitoring.dashboard.v1.TimeSeriesFilterRatio.RatioPart",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="filter",
            full_name="google.monitoring.dashboard.v1.TimeSeriesFilterRatio.RatioPart.filter",
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
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="aggregation",
            full_name="google.monitoring.dashboard.v1.TimeSeriesFilterRatio.RatioPart.aggregation",
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
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1309,
    serialized_end=1407,
)

_TIMESERIESFILTERRATIO = _descriptor.Descriptor(
    name="TimeSeriesFilterRatio",
    full_name="google.monitoring.dashboard.v1.TimeSeriesFilterRatio",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="numerator",
            full_name="google.monitoring.dashboard.v1.TimeSeriesFilterRatio.numerator",
            index=0,
            number=1,
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
        _descriptor.FieldDescriptor(
            name="denominator",
            full_name="google.monitoring.dashboard.v1.TimeSeriesFilterRatio.denominator",
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
        _descriptor.FieldDescriptor(
            name="secondary_aggregation",
            full_name="google.monitoring.dashboard.v1.TimeSeriesFilterRatio.secondary_aggregation",
            index=2,
            number=3,
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
        _descriptor.FieldDescriptor(
            name="pick_time_series_filter",
            full_name="google.monitoring.dashboard.v1.TimeSeriesFilterRatio.pick_time_series_filter",
            index=3,
            number=4,
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
        _descriptor.FieldDescriptor(
            name="statistical_time_series_filter",
            full_name="google.monitoring.dashboard.v1.TimeSeriesFilterRatio.statistical_time_series_filter",
            index=4,
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
            serialized_options=b"\030\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[_TIMESERIESFILTERRATIO_RATIOPART,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="output_filter",
            full_name="google.monitoring.dashboard.v1.TimeSeriesFilterRatio.output_filter",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=842,
    serialized_end=1424,
)


_THRESHOLD = _descriptor.Descriptor(
    name="Threshold",
    full_name="google.monitoring.dashboard.v1.Threshold",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="label",
            full_name="google.monitoring.dashboard.v1.Threshold.label",
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.monitoring.dashboard.v1.Threshold.value",
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
            name="color",
            full_name="google.monitoring.dashboard.v1.Threshold.color",
            index=2,
            number=3,
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
            name="direction",
            full_name="google.monitoring.dashboard.v1.Threshold.direction",
            index=3,
            number=4,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_THRESHOLD_COLOR, _THRESHOLD_DIRECTION,],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1427,
    serialized_end=1719,
)

_TIMESERIESQUERY.fields_by_name["time_series_filter"].message_type = _TIMESERIESFILTER
_TIMESERIESQUERY.fields_by_name[
    "time_series_filter_ratio"
].message_type = _TIMESERIESFILTERRATIO
_TIMESERIESQUERY.oneofs_by_name["source"].fields.append(
    _TIMESERIESQUERY.fields_by_name["time_series_filter"]
)
_TIMESERIESQUERY.fields_by_name[
    "time_series_filter"
].containing_oneof = _TIMESERIESQUERY.oneofs_by_name["source"]
_TIMESERIESQUERY.oneofs_by_name["source"].fields.append(
    _TIMESERIESQUERY.fields_by_name["time_series_filter_ratio"]
)
_TIMESERIESQUERY.fields_by_name[
    "time_series_filter_ratio"
].containing_oneof = _TIMESERIESQUERY.oneofs_by_name["source"]
_TIMESERIESQUERY.oneofs_by_name["source"].fields.append(
    _TIMESERIESQUERY.fields_by_name["time_series_query_language"]
)
_TIMESERIESQUERY.fields_by_name[
    "time_series_query_language"
].containing_oneof = _TIMESERIESQUERY.oneofs_by_name["source"]
_TIMESERIESFILTER.fields_by_name[
    "aggregation"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_common__pb2._AGGREGATION
)
_TIMESERIESFILTER.fields_by_name[
    "secondary_aggregation"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_common__pb2._AGGREGATION
)
_TIMESERIESFILTER.fields_by_name[
    "pick_time_series_filter"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_common__pb2._PICKTIMESERIESFILTER
)
_TIMESERIESFILTER.fields_by_name[
    "statistical_time_series_filter"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_common__pb2._STATISTICALTIMESERIESFILTER
)
_TIMESERIESFILTER.oneofs_by_name["output_filter"].fields.append(
    _TIMESERIESFILTER.fields_by_name["pick_time_series_filter"]
)
_TIMESERIESFILTER.fields_by_name[
    "pick_time_series_filter"
].containing_oneof = _TIMESERIESFILTER.oneofs_by_name["output_filter"]
_TIMESERIESFILTER.oneofs_by_name["output_filter"].fields.append(
    _TIMESERIESFILTER.fields_by_name["statistical_time_series_filter"]
)
_TIMESERIESFILTER.fields_by_name[
    "statistical_time_series_filter"
].containing_oneof = _TIMESERIESFILTER.oneofs_by_name["output_filter"]
_TIMESERIESFILTERRATIO_RATIOPART.fields_by_name[
    "aggregation"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_common__pb2._AGGREGATION
)
_TIMESERIESFILTERRATIO_RATIOPART.containing_type = _TIMESERIESFILTERRATIO
_TIMESERIESFILTERRATIO.fields_by_name[
    "numerator"
].message_type = _TIMESERIESFILTERRATIO_RATIOPART
_TIMESERIESFILTERRATIO.fields_by_name[
    "denominator"
].message_type = _TIMESERIESFILTERRATIO_RATIOPART
_TIMESERIESFILTERRATIO.fields_by_name[
    "secondary_aggregation"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_common__pb2._AGGREGATION
)
_TIMESERIESFILTERRATIO.fields_by_name[
    "pick_time_series_filter"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_common__pb2._PICKTIMESERIESFILTER
)
_TIMESERIESFILTERRATIO.fields_by_name[
    "statistical_time_series_filter"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_common__pb2._STATISTICALTIMESERIESFILTER
)
_TIMESERIESFILTERRATIO.oneofs_by_name["output_filter"].fields.append(
    _TIMESERIESFILTERRATIO.fields_by_name["pick_time_series_filter"]
)
_TIMESERIESFILTERRATIO.fields_by_name[
    "pick_time_series_filter"
].containing_oneof = _TIMESERIESFILTERRATIO.oneofs_by_name["output_filter"]
_TIMESERIESFILTERRATIO.oneofs_by_name["output_filter"].fields.append(
    _TIMESERIESFILTERRATIO.fields_by_name["statistical_time_series_filter"]
)
_TIMESERIESFILTERRATIO.fields_by_name[
    "statistical_time_series_filter"
].containing_oneof = _TIMESERIESFILTERRATIO.oneofs_by_name["output_filter"]
_THRESHOLD.fields_by_name["color"].enum_type = _THRESHOLD_COLOR
_THRESHOLD.fields_by_name["direction"].enum_type = _THRESHOLD_DIRECTION
_THRESHOLD_COLOR.containing_type = _THRESHOLD
_THRESHOLD_DIRECTION.containing_type = _THRESHOLD
DESCRIPTOR.message_types_by_name["TimeSeriesQuery"] = _TIMESERIESQUERY
DESCRIPTOR.message_types_by_name["TimeSeriesFilter"] = _TIMESERIESFILTER
DESCRIPTOR.message_types_by_name["TimeSeriesFilterRatio"] = _TIMESERIESFILTERRATIO
DESCRIPTOR.message_types_by_name["Threshold"] = _THRESHOLD
DESCRIPTOR.enum_types_by_name["SparkChartType"] = _SPARKCHARTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimeSeriesQuery = _reflection.GeneratedProtocolMessageType(
    "TimeSeriesQuery",
    (_message.Message,),
    {
        "DESCRIPTOR": _TIMESERIESQUERY,
        "__module__": "google.cloud.monitoring_dashboard.v1.proto.metrics_pb2",
        "__doc__": """TimeSeriesQuery collects the set of supported methods for querying
  time series data from the Stackdriver metrics API.
  
  Attributes:
      source:
          Parameters needed to obtain data for the chart.
      time_series_filter:
          Filter parameters to fetch time series.
      time_series_filter_ratio:
          Parameters to fetch a ratio between two time series filters.
      time_series_query_language:
          A query used to fetch time series.
      unit_override:
          The unit of data contained in fetched time series. If non-
          empty, this unit will override any unit that accompanies
          fetched data. The format is the same as the ```unit`` <https:/
          /cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metri
          cDescriptors>`__ field in ``MetricDescriptor``.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.TimeSeriesQuery)
    },
)
_sym_db.RegisterMessage(TimeSeriesQuery)

TimeSeriesFilter = _reflection.GeneratedProtocolMessageType(
    "TimeSeriesFilter",
    (_message.Message,),
    {
        "DESCRIPTOR": _TIMESERIESFILTER,
        "__module__": "google.cloud.monitoring_dashboard.v1.proto.metrics_pb2",
        "__doc__": """A filter that defines a subset of time series data that is displayed
  in a widget. Time series data is fetched using the ```ListTimeSeries``
  <https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeS
  eries/list>`__ method.
  
  Attributes:
      filter:
          Required. The `monitoring filter
          <https://cloud.google.com/monitoring/api/v3/filters>`__ that
          identifies the metric types, resources, and projects to query.
      aggregation:
          By default, the raw time series data is returned. Use this
          field to combine multiple time series for different views of
          the data.
      secondary_aggregation:
          Apply a second aggregation after ``aggregation`` is applied.
      output_filter:
          Selects an optional time series filter.
      pick_time_series_filter:
          Ranking based time series filter.
      statistical_time_series_filter:
          Statistics based time series filter. Note: This field is
          deprecated and completely ignored by the API.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.TimeSeriesFilter)
    },
)
_sym_db.RegisterMessage(TimeSeriesFilter)

TimeSeriesFilterRatio = _reflection.GeneratedProtocolMessageType(
    "TimeSeriesFilterRatio",
    (_message.Message,),
    {
        "RatioPart": _reflection.GeneratedProtocolMessageType(
            "RatioPart",
            (_message.Message,),
            {
                "DESCRIPTOR": _TIMESERIESFILTERRATIO_RATIOPART,
                "__module__": "google.cloud.monitoring_dashboard.v1.proto.metrics_pb2",
                "__doc__": """Describes a query to build the numerator or denominator of a
    TimeSeriesFilterRatio.
    
    Attributes:
        filter:
            Required. The `monitoring filter
            <https://cloud.google.com/monitoring/api/v3/filters>`__ that
            identifies the metric types, resources, and projects to query.
        aggregation:
            By default, the raw time series data is returned. Use this
            field to combine multiple time series for different views of
            the data.
    """,
                # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.TimeSeriesFilterRatio.RatioPart)
            },
        ),
        "DESCRIPTOR": _TIMESERIESFILTERRATIO,
        "__module__": "google.cloud.monitoring_dashboard.v1.proto.metrics_pb2",
        "__doc__": """A pair of time series filters that define a ratio computation. The
  output time series is the pair-wise division of each aligned element
  from the numerator and denominator time series.
  
  Attributes:
      numerator:
          The numerator of the ratio.
      denominator:
          The denominator of the ratio.
      secondary_aggregation:
          Apply a second aggregation after the ratio is computed.
      output_filter:
          Selects an optional filter that is applied to the time series
          after computing the ratio.
      pick_time_series_filter:
          Ranking based time series filter.
      statistical_time_series_filter:
          Statistics based time series filter. Note: This field is
          deprecated and completely ignored by the API.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.TimeSeriesFilterRatio)
    },
)
_sym_db.RegisterMessage(TimeSeriesFilterRatio)
_sym_db.RegisterMessage(TimeSeriesFilterRatio.RatioPart)

Threshold = _reflection.GeneratedProtocolMessageType(
    "Threshold",
    (_message.Message,),
    {
        "DESCRIPTOR": _THRESHOLD,
        "__module__": "google.cloud.monitoring_dashboard.v1.proto.metrics_pb2",
        "__doc__": """Defines a threshold for categorizing time series values.
  
  Attributes:
      label:
          A label for the threshold.
      value:
          The value of the threshold. The value should be defined in the
          native scale of the metric.
      color:
          The state color for this threshold. Color is not allowed in a
          XyChart.
      direction:
          The direction for the current threshold. Direction is not
          allowed in a XyChart.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.Threshold)
    },
)
_sym_db.RegisterMessage(Threshold)


DESCRIPTOR._options = None
_TIMESERIESFILTER.fields_by_name["filter"]._options = None
_TIMESERIESFILTER.fields_by_name["statistical_time_series_filter"]._options = None
_TIMESERIESFILTERRATIO_RATIOPART.fields_by_name["filter"]._options = None
_TIMESERIESFILTERRATIO.fields_by_name["statistical_time_series_filter"]._options = None
# @@protoc_insertion_point(module_scope)
