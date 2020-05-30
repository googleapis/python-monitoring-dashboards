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
# source: google/cloud/monitoring_dashboard_v1/proto/xychart.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.monitoring_dashboard_v1.proto import (
    metrics_pb2 as google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_metrics__pb2,
)
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/monitoring_dashboard_v1/proto/xychart.proto",
    package="google.monitoring.dashboard.v1",
    syntax="proto3",
    serialized_options=b'\n"com.google.monitoring.dashboard.v1B\014XyChartProtoP\001ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\352\002(Google::Cloud::Monitoring::Dashboard::V1',
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n8google/cloud/monitoring_dashboard_v1/proto/xychart.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x38google/cloud/monitoring_dashboard_v1/proto/metrics.proto\x1a\x1egoogle/protobuf/duration.proto"\xf3\x06\n\x07XyChart\x12\x42\n\tdata_sets\x18\x01 \x03(\x0b\x32/.google.monitoring.dashboard.v1.XyChart.DataSet\x12\x35\n\x12timeshift_duration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12=\n\nthresholds\x18\x05 \x03(\x0b\x32).google.monitoring.dashboard.v1.Threshold\x12<\n\x06x_axis\x18\x06 \x01(\x0b\x32,.google.monitoring.dashboard.v1.XyChart.Axis\x12<\n\x06y_axis\x18\x07 \x01(\x0b\x32,.google.monitoring.dashboard.v1.XyChart.Axis\x12\x43\n\rchart_options\x18\x08 \x01(\x0b\x32,.google.monitoring.dashboard.v1.ChartOptions\x1a\xda\x02\n\x07\x44\x61taSet\x12J\n\x11time_series_query\x18\x01 \x01(\x0b\x32/.google.monitoring.dashboard.v1.TimeSeriesQuery\x12K\n\tplot_type\x18\x02 \x01(\x0e\x32\x38.google.monitoring.dashboard.v1.XyChart.DataSet.PlotType\x12\x17\n\x0flegend_template\x18\x03 \x01(\t\x12<\n\x14min_alignment_period\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationB\x03\xe0\x41\x01"_\n\x08PlotType\x12\x19\n\x15PLOT_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04LINE\x10\x01\x12\x10\n\x0cSTACKED_AREA\x10\x02\x12\x0f\n\x0bSTACKED_BAR\x10\x03\x12\x0b\n\x07HEATMAP\x10\x04\x1a\x8f\x01\n\x04\x41xis\x12\r\n\x05label\x18\x01 \x01(\t\x12\x41\n\x05scale\x18\x02 \x01(\x0e\x32\x32.google.monitoring.dashboard.v1.XyChart.Axis.Scale"5\n\x05Scale\x12\x15\n\x11SCALE_UNSPECIFIED\x10\x00\x12\n\n\x06LINEAR\x10\x01\x12\t\n\x05LOG10\x10\x02"\x8e\x01\n\x0c\x43hartOptions\x12?\n\x04mode\x18\x01 \x01(\x0e\x32\x31.google.monitoring.dashboard.v1.ChartOptions.Mode"=\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\t\n\x05\x43OLOR\x10\x01\x12\t\n\x05X_RAY\x10\x02\x12\t\n\x05STATS\x10\x03\x42\xa8\x01\n"com.google.monitoring.dashboard.v1B\x0cXyChartProtoP\x01ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3',
    dependencies=[
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_metrics__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,
    ],
)


_XYCHART_DATASET_PLOTTYPE = _descriptor.EnumDescriptor(
    name="PlotType",
    full_name="google.monitoring.dashboard.v1.XyChart.DataSet.PlotType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="PLOT_TYPE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="LINE",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="STACKED_AREA",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="STACKED_BAR",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="HEATMAP",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=858,
    serialized_end=953,
)
_sym_db.RegisterEnumDescriptor(_XYCHART_DATASET_PLOTTYPE)

_XYCHART_AXIS_SCALE = _descriptor.EnumDescriptor(
    name="Scale",
    full_name="google.monitoring.dashboard.v1.XyChart.Axis.Scale",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="SCALE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="LINEAR",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="LOG10",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1046,
    serialized_end=1099,
)
_sym_db.RegisterEnumDescriptor(_XYCHART_AXIS_SCALE)

_CHARTOPTIONS_MODE = _descriptor.EnumDescriptor(
    name="Mode",
    full_name="google.monitoring.dashboard.v1.ChartOptions.Mode",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="MODE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="COLOR",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="X_RAY",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="STATS",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1183,
    serialized_end=1244,
)
_sym_db.RegisterEnumDescriptor(_CHARTOPTIONS_MODE)


_XYCHART_DATASET = _descriptor.Descriptor(
    name="DataSet",
    full_name="google.monitoring.dashboard.v1.XyChart.DataSet",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="time_series_query",
            full_name="google.monitoring.dashboard.v1.XyChart.DataSet.time_series_query",
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
            name="plot_type",
            full_name="google.monitoring.dashboard.v1.XyChart.DataSet.plot_type",
            index=1,
            number=2,
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
            name="legend_template",
            full_name="google.monitoring.dashboard.v1.XyChart.DataSet.legend_template",
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
            name="min_alignment_period",
            full_name="google.monitoring.dashboard.v1.XyChart.DataSet.min_alignment_period",
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
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_XYCHART_DATASET_PLOTTYPE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=607,
    serialized_end=953,
)

_XYCHART_AXIS = _descriptor.Descriptor(
    name="Axis",
    full_name="google.monitoring.dashboard.v1.XyChart.Axis",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="label",
            full_name="google.monitoring.dashboard.v1.XyChart.Axis.label",
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
            name="scale",
            full_name="google.monitoring.dashboard.v1.XyChart.Axis.scale",
            index=1,
            number=2,
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
    enum_types=[_XYCHART_AXIS_SCALE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=956,
    serialized_end=1099,
)

_XYCHART = _descriptor.Descriptor(
    name="XyChart",
    full_name="google.monitoring.dashboard.v1.XyChart",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="data_sets",
            full_name="google.monitoring.dashboard.v1.XyChart.data_sets",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
            name="timeshift_duration",
            full_name="google.monitoring.dashboard.v1.XyChart.timeshift_duration",
            index=1,
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
            name="thresholds",
            full_name="google.monitoring.dashboard.v1.XyChart.thresholds",
            index=2,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
            name="x_axis",
            full_name="google.monitoring.dashboard.v1.XyChart.x_axis",
            index=3,
            number=6,
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
            name="y_axis",
            full_name="google.monitoring.dashboard.v1.XyChart.y_axis",
            index=4,
            number=7,
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
            name="chart_options",
            full_name="google.monitoring.dashboard.v1.XyChart.chart_options",
            index=5,
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
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[_XYCHART_DATASET, _XYCHART_AXIS],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=216,
    serialized_end=1099,
)


_CHARTOPTIONS = _descriptor.Descriptor(
    name="ChartOptions",
    full_name="google.monitoring.dashboard.v1.ChartOptions",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="mode",
            full_name="google.monitoring.dashboard.v1.ChartOptions.mode",
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
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_CHARTOPTIONS_MODE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1102,
    serialized_end=1244,
)

_XYCHART_DATASET.fields_by_name[
    "time_series_query"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_metrics__pb2._TIMESERIESQUERY
)
_XYCHART_DATASET.fields_by_name["plot_type"].enum_type = _XYCHART_DATASET_PLOTTYPE
_XYCHART_DATASET.fields_by_name[
    "min_alignment_period"
].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_XYCHART_DATASET.containing_type = _XYCHART
_XYCHART_DATASET_PLOTTYPE.containing_type = _XYCHART_DATASET
_XYCHART_AXIS.fields_by_name["scale"].enum_type = _XYCHART_AXIS_SCALE
_XYCHART_AXIS.containing_type = _XYCHART
_XYCHART_AXIS_SCALE.containing_type = _XYCHART_AXIS
_XYCHART.fields_by_name["data_sets"].message_type = _XYCHART_DATASET
_XYCHART.fields_by_name[
    "timeshift_duration"
].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_XYCHART.fields_by_name[
    "thresholds"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_metrics__pb2._THRESHOLD
)
_XYCHART.fields_by_name["x_axis"].message_type = _XYCHART_AXIS
_XYCHART.fields_by_name["y_axis"].message_type = _XYCHART_AXIS
_XYCHART.fields_by_name["chart_options"].message_type = _CHARTOPTIONS
_CHARTOPTIONS.fields_by_name["mode"].enum_type = _CHARTOPTIONS_MODE
_CHARTOPTIONS_MODE.containing_type = _CHARTOPTIONS
DESCRIPTOR.message_types_by_name["XyChart"] = _XYCHART
DESCRIPTOR.message_types_by_name["ChartOptions"] = _CHARTOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

XyChart = _reflection.GeneratedProtocolMessageType(
    "XyChart",
    (_message.Message,),
    {
        "DataSet": _reflection.GeneratedProtocolMessageType(
            "DataSet",
            (_message.Message,),
            {
                "DESCRIPTOR": _XYCHART_DATASET,
                "__module__": "google.cloud.monitoring_dashboard_v1.proto.xychart_pb2",
                "__doc__": """Groups a time series query definition with charting options.
    Attributes:
        time_series_query:
            Fields for querying time series data from the Stackdriver
            metrics API.
        plot_type:
            How this data should be plotted on the chart.
        legend_template:
            A template string for naming ``TimeSeries`` in the resulting
            data set. This should be a string with interpolations of the
            form ${label_name}, which will resolve to the label’s value.
        min_alignment_period:
            Optional. The lower bound on data point frequency for this
            data set, implemented by specifying the minimum alignment
            period to use in a time series query For example, if the data
            is published once every 10 minutes, the
            ``min_alignment_period`` should be at least 10 minutes. It
            would not make sense to fetch and align data at one minute
            intervals.
    """,
                # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.XyChart.DataSet)
            },
        ),
        "Axis": _reflection.GeneratedProtocolMessageType(
            "Axis",
            (_message.Message,),
            {
                "DESCRIPTOR": _XYCHART_AXIS,
                "__module__": "google.cloud.monitoring_dashboard_v1.proto.xychart_pb2",
                "__doc__": """A chart axis.
    Attributes:
        label:
            The label of the axis.
        scale:
            The axis scale. By default, a linear scale is used.
    """,
                # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.XyChart.Axis)
            },
        ),
        "DESCRIPTOR": _XYCHART,
        "__module__": "google.cloud.monitoring_dashboard_v1.proto.xychart_pb2",
        "__doc__": """A chart that displays data on a 2D (X and Y axes) plane.
  Attributes:
      data_sets:
          The data displayed in this chart.
      timeshift_duration:
          The duration used to display a comparison chart. A comparison
          chart simultaneously shows values from two similar-length time
          periods (e.g., week-over-week metrics). The duration must be
          positive, and it can only be applied to charts with data sets
          of LINE plot type.
      thresholds:
          Threshold lines drawn horizontally across the chart.
      x_axis:
          The properties applied to the X axis.
      y_axis:
          The properties applied to the Y axis.
      chart_options:
          Display options for the chart.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.XyChart)
    },
)
_sym_db.RegisterMessage(XyChart)
_sym_db.RegisterMessage(XyChart.DataSet)
_sym_db.RegisterMessage(XyChart.Axis)

ChartOptions = _reflection.GeneratedProtocolMessageType(
    "ChartOptions",
    (_message.Message,),
    {
        "DESCRIPTOR": _CHARTOPTIONS,
        "__module__": "google.cloud.monitoring_dashboard_v1.proto.xychart_pb2",
        "__doc__": """Options to control visual rendering of a chart.
  Attributes:
      mode:
          The chart mode.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.ChartOptions)
    },
)
_sym_db.RegisterMessage(ChartOptions)


DESCRIPTOR._options = None
_XYCHART_DATASET.fields_by_name["min_alignment_period"]._options = None
# @@protoc_insertion_point(module_scope)
