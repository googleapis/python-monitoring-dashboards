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
# source: google/cloud/monitoring_dashboard_v1/proto/scorecard.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.monitoring_dashboard_v1.proto import (
    metrics_pb2 as google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_metrics__pb2,
)
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/monitoring_dashboard_v1/proto/scorecard.proto",
    package="google.monitoring.dashboard.v1",
    syntax="proto3",
    serialized_options=b'\n"com.google.monitoring.dashboard.v1B\016ScorecardProtoP\001ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\352\002(Google::Cloud::Monitoring::Dashboard::V1',
    serialized_pb=b'\n:google/cloud/monitoring_dashboard_v1/proto/scorecard.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x38google/cloud/monitoring_dashboard_v1/proto/metrics.proto\x1a\x1egoogle/protobuf/duration.proto"\x91\x04\n\tScorecard\x12J\n\x11time_series_query\x18\x01 \x01(\x0b\x32/.google.monitoring.dashboard.v1.TimeSeriesQuery\x12I\n\ngauge_view\x18\x04 \x01(\x0b\x32\x33.google.monitoring.dashboard.v1.Scorecard.GaugeViewH\x00\x12T\n\x10spark_chart_view\x18\x05 \x01(\x0b\x32\x38.google.monitoring.dashboard.v1.Scorecard.SparkChartViewH\x00\x12=\n\nthresholds\x18\x06 \x03(\x0b\x32).google.monitoring.dashboard.v1.Threshold\x1a\x35\n\tGaugeView\x12\x13\n\x0blower_bound\x18\x01 \x01(\x01\x12\x13\n\x0bupper_bound\x18\x02 \x01(\x01\x1a\x93\x01\n\x0eSparkChartView\x12H\n\x10spark_chart_type\x18\x01 \x01(\x0e\x32..google.monitoring.dashboard.v1.SparkChartType\x12\x37\n\x14min_alignment_period\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0b\n\tdata_viewB\xaa\x01\n"com.google.monitoring.dashboard.v1B\x0eScorecardProtoP\x01ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3',
    dependencies=[
        google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_metrics__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,
    ],
)


_SCORECARD_GAUGEVIEW = _descriptor.Descriptor(
    name="GaugeView",
    full_name="google.monitoring.dashboard.v1.Scorecard.GaugeView",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="lower_bound",
            full_name="google.monitoring.dashboard.v1.Scorecard.GaugeView.lower_bound",
            index=0,
            number=1,
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
        ),
        _descriptor.FieldDescriptor(
            name="upper_bound",
            full_name="google.monitoring.dashboard.v1.Scorecard.GaugeView.upper_bound",
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
    serialized_start=498,
    serialized_end=551,
)

_SCORECARD_SPARKCHARTVIEW = _descriptor.Descriptor(
    name="SparkChartView",
    full_name="google.monitoring.dashboard.v1.Scorecard.SparkChartView",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="spark_chart_type",
            full_name="google.monitoring.dashboard.v1.Scorecard.SparkChartView.spark_chart_type",
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
        ),
        _descriptor.FieldDescriptor(
            name="min_alignment_period",
            full_name="google.monitoring.dashboard.v1.Scorecard.SparkChartView.min_alignment_period",
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
    serialized_start=554,
    serialized_end=701,
)

_SCORECARD = _descriptor.Descriptor(
    name="Scorecard",
    full_name="google.monitoring.dashboard.v1.Scorecard",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="time_series_query",
            full_name="google.monitoring.dashboard.v1.Scorecard.time_series_query",
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
        ),
        _descriptor.FieldDescriptor(
            name="gauge_view",
            full_name="google.monitoring.dashboard.v1.Scorecard.gauge_view",
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
        ),
        _descriptor.FieldDescriptor(
            name="spark_chart_view",
            full_name="google.monitoring.dashboard.v1.Scorecard.spark_chart_view",
            index=2,
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
            name="thresholds",
            full_name="google.monitoring.dashboard.v1.Scorecard.thresholds",
            index=3,
            number=6,
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
        ),
    ],
    extensions=[],
    nested_types=[_SCORECARD_GAUGEVIEW, _SCORECARD_SPARKCHARTVIEW],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="data_view",
            full_name="google.monitoring.dashboard.v1.Scorecard.data_view",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=185,
    serialized_end=714,
)

_SCORECARD_GAUGEVIEW.containing_type = _SCORECARD
_SCORECARD_SPARKCHARTVIEW.fields_by_name[
    "spark_chart_type"
].enum_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_metrics__pb2._SPARKCHARTTYPE
)
_SCORECARD_SPARKCHARTVIEW.fields_by_name[
    "min_alignment_period"
].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_SCORECARD_SPARKCHARTVIEW.containing_type = _SCORECARD
_SCORECARD.fields_by_name[
    "time_series_query"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_metrics__pb2._TIMESERIESQUERY
)
_SCORECARD.fields_by_name["gauge_view"].message_type = _SCORECARD_GAUGEVIEW
_SCORECARD.fields_by_name["spark_chart_view"].message_type = _SCORECARD_SPARKCHARTVIEW
_SCORECARD.fields_by_name[
    "thresholds"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_metrics__pb2._THRESHOLD
)
_SCORECARD.oneofs_by_name["data_view"].fields.append(
    _SCORECARD.fields_by_name["gauge_view"]
)
_SCORECARD.fields_by_name["gauge_view"].containing_oneof = _SCORECARD.oneofs_by_name[
    "data_view"
]
_SCORECARD.oneofs_by_name["data_view"].fields.append(
    _SCORECARD.fields_by_name["spark_chart_view"]
)
_SCORECARD.fields_by_name[
    "spark_chart_view"
].containing_oneof = _SCORECARD.oneofs_by_name["data_view"]
DESCRIPTOR.message_types_by_name["Scorecard"] = _SCORECARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Scorecard = _reflection.GeneratedProtocolMessageType(
    "Scorecard",
    (_message.Message,),
    {
        "GaugeView": _reflection.GeneratedProtocolMessageType(
            "GaugeView",
            (_message.Message,),
            {
                "DESCRIPTOR": _SCORECARD_GAUGEVIEW,
                "__module__": "google.cloud.monitoring_dashboard_v1.proto.scorecard_pb2",
                "__doc__": """A gauge chart shows where the current value sits within a pre-defined
    range. The upper and lower bounds should define the possible range of
    values for the scorecard’s query (inclusive).
    Attributes:
        lower_bound:
            The lower bound for this gauge chart. The value of the chart
            should always be greater than or equal to this.
        upper_bound:
            The upper bound for this gauge chart. The value of the chart
            should always be less than or equal to this.
    """,
                # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.Scorecard.GaugeView)
            },
        ),
        "SparkChartView": _reflection.GeneratedProtocolMessageType(
            "SparkChartView",
            (_message.Message,),
            {
                "DESCRIPTOR": _SCORECARD_SPARKCHARTVIEW,
                "__module__": "google.cloud.monitoring_dashboard_v1.proto.scorecard_pb2",
                "__doc__": """A sparkChart is a small chart suitable for inclusion in a table-cell
    or inline in text. This message contains the configuration for a
    sparkChart to show up on a Scorecard, showing recent trends of the
    scorecard’s timeseries.
    Attributes:
        spark_chart_type:
            The type of sparkchart to show in this chartView.
        min_alignment_period:
            The lower bound on data point frequency in the chart
            implemented by specifying the minimum alignment period to use
            in a time series query. For example, if the data is published
            once every 10 minutes it would not make sense to fetch and
            align data at one minute intervals. This field is optional and
            exists only as a hint.
    """,
                # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.Scorecard.SparkChartView)
            },
        ),
        "DESCRIPTOR": _SCORECARD,
        "__module__": "google.cloud.monitoring_dashboard_v1.proto.scorecard_pb2",
        "__doc__": """A widget showing the latest value of a metric, and how this value
  relates to one or more thresholds.
  Attributes:
      time_series_query:
          Fields for querying time series data from the Stackdriver
          metrics API.
      data_view:
          Defines the optional additional chart shown on the scorecard.
          If neither is included - then a default scorecard is shown.
      gauge_view:
          Will cause the scorecard to show a gauge chart.
      spark_chart_view:
          Will cause the scorecard to show a spark chart.
      thresholds:
          The thresholds used to determine the state of the scorecard
          given the time series’ current value. For an actual value x,
          the scorecard is in a danger state if x is less than or equal
          to a danger threshold that triggers below, or greater than or
          equal to a danger threshold that triggers above. Similarly, if
          x is above/below a warning threshold that triggers
          above/below, then the scorecard is in a warning state - unless
          x also puts it in a danger state. (Danger trumps warning.)  As
          an example, consider a scorecard with the following four
          thresholds: { value: 90, category: ‘DANGER’, trigger: ‘ABOVE’,
          }, { value: 70, category: ‘WARNING’, trigger: ‘ABOVE’, }, {
          value: 10, category: ‘DANGER’, trigger: ‘BELOW’, }, { value:
          20, category: ‘WARNING’, trigger: ‘BELOW’, }  Then: values
          less than or equal to 10 would put the scorecard in a DANGER
          state, values greater than 10 but less than or equal to 20 a
          WARNING state, values strictly between 20 and 70 an OK state,
          values greater than or equal to 70 but less than 90 a WARNING
          state, and values greater than or equal to 90 a DANGER state.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.Scorecard)
    },
)
_sym_db.RegisterMessage(Scorecard)
_sym_db.RegisterMessage(Scorecard.GaugeView)
_sym_db.RegisterMessage(Scorecard.SparkChartView)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
