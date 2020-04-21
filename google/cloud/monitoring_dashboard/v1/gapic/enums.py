# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Wrappers for protocol buffer enum types."""

import enum


class SparkChartType(enum.IntEnum):
    """
    A definition of a client library method signature.

    In client libraries, each proto RPC corresponds to one or more methods
    which the end user is able to call, and calls the underlying RPC.
    Normally, this method receives a single argument (a struct or instance
    corresponding to the RPC request object). Defining this field will add
    one or more overloads providing flattened or simpler method signatures
    in some languages.

    The fields on the method signature are provided as a comma-separated
    string.

    For example, the proto RPC and annotation:

    rpc CreateSubscription(CreateSubscriptionRequest) returns (Subscription)
    { option (google.api.method_signature) = "name,topic"; }

    Would add the following Java overload (in addition to the method
    accepting the request object):

    public final Subscription createSubscription(String name, String topic)

    The following backwards-compatibility guidelines apply:

    -  Adding this annotation to an unannotated method is backwards
       compatible.
    -  Adding this annotation to a method which already has existing method
       signature annotations is backwards compatible if and only if the new
       method signature annotation is last in the sequence.
    -  Modifying or removing an existing method signature annotation is a
       breaking change.
    -  Re-ordering existing method signature annotations is a breaking
       change.

    Attributes:
      SPARK_CHART_TYPE_UNSPECIFIED (int): Not allowed in well-formed requests.
      SPARK_LINE (int): The sparkline will be rendered as a small line chart.
      SPARK_BAR (int): The sparkbar will be rendered as a small bar chart.
    """

    SPARK_CHART_TYPE_UNSPECIFIED = 0
    SPARK_LINE = 1
    SPARK_BAR = 2


class Aggregation(object):
    class Aligner(enum.IntEnum):
        """
        The Aligner describes how to bring the data points in a single
        time series into temporal alignment.

        Attributes:
          ALIGN_NONE (int): No alignment. Raw data is returned. Not valid if cross-time
          series reduction is requested. The value type of the result is
          the same as the value type of the input.
          ALIGN_DELTA (int): Reduce by computing the fraction of True-valued data points across
          time series for each alignment period. This reducer is valid for delta
          and gauge metrics of Boolean value type. The output value is in the
          range [0, 1] and has value type ``DOUBLE``.
          ALIGN_RATE (int): Required. The project on which to execute the request. The format is
          ``"projects/{project_id_or_number}"``. The {project_id_or_number} must
          match the dashboard resource name.
          ALIGN_INTERPOLATE (int): Align by interpolating between adjacent points around the
          period boundary. This alignment is valid for gauge
          metrics with numeric values. The value type of the result is the same
          as the value type of the input.
          ALIGN_NEXT_OLDER (int): Align by shifting the oldest data point before the period
          boundary to the boundary. This alignment is valid for gauge
          metrics. The value type of the result is the same as the
          value type of the input.
          ALIGN_MIN (int): Align time series via aggregation. The resulting data point in
          the alignment period is the minimum of all data points in the
          period. This alignment is valid for gauge and delta metrics with numeric
          values. The value type of the result is the same as the value
          type of the input.
          ALIGN_MAX (int): Align time series via aggregation. The resulting data point in
          the alignment period is the maximum of all data points in the
          period. This alignment is valid for gauge and delta metrics with numeric
          values. The value type of the result is the same as the value
          type of the input.
          ALIGN_MEAN (int): Protocol Buffers - Google's data interchange format Copyright 2008
          Google Inc. All rights reserved.
          https://developers.google.com/protocol-buffers/

          Redistribution and use in source and binary forms, with or without
          modification, are permitted provided that the following conditions are
          met:

          ::

              * Redistributions of source code must retain the above copyright

          notice, this list of conditions and the following disclaimer. \*
          Redistributions in binary form must reproduce the above copyright
          notice, this list of conditions and the following disclaimer in the
          documentation and/or other materials provided with the distribution. \*
          Neither the name of Google Inc. nor the names of its contributors may be
          used to endorse or promote products derived from this software without
          specific prior written permission.

          THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
          IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
          TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
          PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
          OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
          EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
          PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
          PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
          LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
          NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
          SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
          ALIGN_COUNT (int): An annotation that describes a resource definition, see
          ``ResourceDescriptor``.
          ALIGN_SUM (int): Align time series via aggregation. The resulting data point in
          the alignment period is the sum of all data points in the
          period. This alignment is valid for gauge and delta metrics with numeric
          and distribution values. The value type of the output is the
          same as the value type of the input.
          ALIGN_STDDEV (int): Reduce by computing 99th percentile of data points across time
          series for each alignment period. This reducer is valid for gauge and
          delta metrics of numeric and distribution type. The value of the output
          is ``DOUBLE``
          ALIGN_COUNT_TRUE (int): Each of the definitions above may have "options" attached. These are
          just annotations which may cause code to be generated slightly
          differently or may contain hints for code that manipulates protocol
          messages.

          Clients may define custom options as extensions of the \*Options
          messages. These extensions may not yet be known at parsing time, so the
          parser cannot store the values in them. Instead it stores them in a
          field in the \*Options message called uninterpreted_option. This field
          must have the same name across all \*Options messages. We then use this
          field to populate the extensions when we build a descriptor, at which
          point all protos have been parsed and so all extensions are known.

          Extension numbers for custom options may be chosen as follows:

          -  For options which will only be used within a single application or
             organization, or for experimental options, use field numbers 50000
             through 99999. It is up to you to ensure that you do not use the same
             number for multiple options.
          -  For options which will be published and used publicly by multiple
             independent entities, e-mail
             protobuf-global-extension-registry@google.com to reserve extension
             numbers. Simply provide your project name (e.g. Objective-C plugin)
             and your project website (if available) -- there's no need to explain
             how you intend to use them. Usually you only need one extension
             number. You can declare multiple options with only one extension
             number by putting them in a sub-message. See the Custom Options
             section of the docs for examples:
             https://developers.google.com/protocol-buffers/docs/proto#options If
             this turns out to be popular, a web service will be set up to
             automatically assign option numbers.
          ALIGN_COUNT_FALSE (int): A designation of a specific field behavior (required, output only,
          etc.) in protobuf messages.

          Examples:

          string name = 1 [(google.api.field_behavior) = REQUIRED]; State state =
          1 [(google.api.field_behavior) = OUTPUT_ONLY]; google.protobuf.Duration
          ttl = 1 [(google.api.field_behavior) = INPUT_ONLY];
          google.protobuf.Timestamp expire_time = 1 [(google.api.field_behavior) =
          OUTPUT_ONLY, (google.api.field_behavior) = IMMUTABLE];
          ALIGN_FRACTION_TRUE (int): Reduce by computing 95th percentile of data points across time
          series for each alignment period. This reducer is valid for gauge and
          delta metrics of numeric and distribution type. The value of the output
          is ``DOUBLE``
          ALIGN_PERCENTILE_99 (int): The ``GetDashboard`` request.
          ALIGN_PERCENTILE_95 (int): Reduce by computing 50th percentile of data points across time
          series for each alignment period. This reducer is valid for gauge and
          delta metrics of numeric and distribution type. The value of the output
          is ``DOUBLE``
          ALIGN_PERCENTILE_50 (int): If set, all the classes from the .proto file are wrapped in a single
          outer class with the given name. This applies to both Proto1 (equivalent
          to the old "--one_java_file" option) and Proto2 (where a .proto always
          translates to a single class, but you may want to explicitly choose the
          class name).
          ALIGN_PERCENTILE_05 (int): Reduce by computing 5th percentile of data points across time series
          for each alignment period. This reducer is valid for gauge and delta
          metrics of numeric and distribution type. The value of the output is
          ``DOUBLE``
          ALIGN_PERCENT_CHANGE (int): The ``ListDashboards`` request.
        """

        ALIGN_NONE = 0
        ALIGN_DELTA = 1
        ALIGN_RATE = 2
        ALIGN_INTERPOLATE = 3
        ALIGN_NEXT_OLDER = 4
        ALIGN_MIN = 10
        ALIGN_MAX = 11
        ALIGN_MEAN = 12
        ALIGN_COUNT = 13
        ALIGN_SUM = 14
        ALIGN_STDDEV = 15
        ALIGN_COUNT_TRUE = 16
        ALIGN_COUNT_FALSE = 24
        ALIGN_FRACTION_TRUE = 17
        ALIGN_PERCENTILE_99 = 18
        ALIGN_PERCENTILE_95 = 19
        ALIGN_PERCENTILE_50 = 20
        ALIGN_PERCENTILE_05 = 21
        ALIGN_PERCENT_CHANGE = 23

    class Reducer(enum.IntEnum):
        """
        A Reducer describes how to aggregate data points from multiple
        time series into a single time series.

        Attributes:
          REDUCE_NONE (int): No cross-time series reduction. The output of the aligner is
          returned.
          REDUCE_MEAN (int): A simple descriptor of a resource type.

          ResourceDescriptor annotates a resource message (either by means of a
          protobuf annotation or use in the service config), and associates the
          resource's schema, the resource type, and the pattern of the resource
          name.

          Example:

          ::

              message Topic {
                // Indicates this message defines a resource schema.
                // Declares the resource type in the format of {service}/{kind}.
                // For Kubernetes resources, the format is {api group}/{kind}.
                option (google.api.resource) = {
                  type: "pubsub.googleapis.com/Topic"
                  name_descriptor: {
                    pattern: "projects/{project}/topics/{topic}"
                    parent_type: "cloudresourcemanager.googleapis.com/Project"
                    parent_name_extractor: "projects/{project}"
                  }
                };
              }

          The ResourceDescriptor Yaml config will look like:

          ::

              resources:
              - type: "pubsub.googleapis.com/Topic"
                name_descriptor:
                  - pattern: "projects/{project}/topics/{topic}"
                    parent_type: "cloudresourcemanager.googleapis.com/Project"
                    parent_name_extractor: "projects/{project}"

          Sometimes, resources have multiple patterns, typically because they can
          live under multiple parents.

          Example:

          ::

              message LogEntry {
                option (google.api.resource) = {
                  type: "logging.googleapis.com/LogEntry"
                  name_descriptor: {
                    pattern: "projects/{project}/logs/{log}"
                    parent_type: "cloudresourcemanager.googleapis.com/Project"
                    parent_name_extractor: "projects/{project}"
                  }
                  name_descriptor: {
                    pattern: "folders/{folder}/logs/{log}"
                    parent_type: "cloudresourcemanager.googleapis.com/Folder"
                    parent_name_extractor: "folders/{folder}"
                  }
                  name_descriptor: {
                    pattern: "organizations/{organization}/logs/{log}"
                    parent_type: "cloudresourcemanager.googleapis.com/Organization"
                    parent_name_extractor: "organizations/{organization}"
                  }
                  name_descriptor: {
                    pattern: "billingAccounts/{billing_account}/logs/{log}"
                    parent_type: "billing.googleapis.com/BillingAccount"
                    parent_name_extractor: "billingAccounts/{billing_account}"
                  }
                };
              }

          The ResourceDescriptor Yaml config will look like:

          ::

              resources:
              - type: 'logging.googleapis.com/LogEntry'
                name_descriptor:
                  - pattern: "projects/{project}/logs/{log}"
                    parent_type: "cloudresourcemanager.googleapis.com/Project"
                    parent_name_extractor: "projects/{project}"
                  - pattern: "folders/{folder}/logs/{log}"
                    parent_type: "cloudresourcemanager.googleapis.com/Folder"
                    parent_name_extractor: "folders/{folder}"
                  - pattern: "organizations/{organization}/logs/{log}"
                    parent_type: "cloudresourcemanager.googleapis.com/Organization"
                    parent_name_extractor: "organizations/{organization}"
                  - pattern: "billingAccounts/{billing_account}/logs/{log}"
                    parent_type: "billing.googleapis.com/BillingAccount"
                    parent_name_extractor: "billingAccounts/{billing_account}"

          For flexible resources, the resource name doesn't contain parent names,
          but the resource itself has parents for policy evaluation.

          Example:

          ::

              message Shelf {
                option (google.api.resource) = {
                  type: "library.googleapis.com/Shelf"
                  name_descriptor: {
                    pattern: "shelves/{shelf}"
                    parent_type: "cloudresourcemanager.googleapis.com/Project"
                  }
                  name_descriptor: {
                    pattern: "shelves/{shelf}"
                    parent_type: "cloudresourcemanager.googleapis.com/Folder"
                  }
                };
              }

          The ResourceDescriptor Yaml config will look like:

          ::

              resources:
              - type: 'library.googleapis.com/Shelf'
                name_descriptor:
                  - pattern: "shelves/{shelf}"
                    parent_type: "cloudresourcemanager.googleapis.com/Project"
                  - pattern: "shelves/{shelf}"
                    parent_type: "cloudresourcemanager.googleapis.com/Folder"
          REDUCE_MIN (int): Reduce by computing the minimum across time series for each
          alignment period. This reducer is valid for delta and
          gauge metrics with numeric values. The value type of the output
          is the same as the value type of the input.
          REDUCE_MAX (int): Reduce by computing the maximum across time series for each
          alignment period. This reducer is valid for delta and
          gauge metrics with numeric values. The value type of the output
          is the same as the value type of the input.
          REDUCE_SUM (int): Reduce by computing the sum across time series for each
          alignment period. This reducer is valid for delta and
          gauge metrics with numeric and distribution values. The value type of
          the output is the same as the value type of the input.
          REDUCE_STDDEV (int): The alignment period for per-\ ``time series`` alignment. If
          present, ``alignmentPeriod`` must be at least 60 seconds. After per-time
          series alignment, each time series will contain data points only on the
          period boundaries. If ``perSeriesAligner`` is not specified or equals
          ``ALIGN_NONE``, then this field is ignored. If ``perSeriesAligner`` is
          specified and does not equal ``ALIGN_NONE``, then this field must be
          defined; otherwise an error is returned.
          REDUCE_COUNT (int): Signed seconds of the span of time. Must be from -315,576,000,000 to
          +315,576,000,000 inclusive. Note: these bounds are computed from: 60
          sec/min \* 60 min/hr \* 24 hr/day \* 365.25 days/year \* 10000 years
          REDUCE_COUNT_TRUE (int): Optional. The relative resource name pattern associated with this
          resource type. The DNS prefix of the full resource name shouldn't be
          specified here.

          The path pattern must follow the syntax, which aligns with HTTP binding
          syntax:

          ::

              Template = Segment { "/" Segment } ;
              Segment = LITERAL | Variable ;
              Variable = "{" LITERAL "}" ;

          Examples:

          ::

              - "projects/{project}/topics/{topic}"
              - "projects/{project}/knowledgeBases/{knowledge_base}"

          The components in braces correspond to the IDs for each resource in the
          hierarchy. It is expected that, if multiple patterns are provided, the
          same component name (e.g. "project") refers to IDs of the same type of
          resource.
          REDUCE_COUNT_FALSE (int): Protocol Buffers - Google's data interchange format Copyright 2008
          Google Inc. All rights reserved.
          https://developers.google.com/protocol-buffers/

          Redistribution and use in source and binary forms, with or without
          modification, are permitted provided that the following conditions are
          met:

          ::

              * Redistributions of source code must retain the above copyright

          notice, this list of conditions and the following disclaimer. \*
          Redistributions in binary form must reproduce the above copyright
          notice, this list of conditions and the following disclaimer in the
          documentation and/or other materials provided with the distribution. \*
          Neither the name of Google Inc. nor the names of its contributors may be
          used to endorse or promote products derived from this software without
          specific prior written permission.

          THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
          IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
          TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
          PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
          OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
          EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
          PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
          PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
          LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
          NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
          SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
          REDUCE_FRACTION_TRUE (int): A generic empty message that you can re-use to avoid defining
          duplicated empty messages in your APIs. A typical example is to use it
          as the request or the response type of an API method. For instance:

          ::

              service Foo {
                rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);
              }

          The JSON representation for ``Empty`` is empty JSON object ``{}``.
          REDUCE_PERCENTILE_99 (int): Denotes a field as required. This indicates that the field **must**
          be provided as part of the request, and failure to do so will cause an
          error (usually ``INVALID_ARGUMENT``).
          REDUCE_PERCENTILE_95 (int): The approach to be used to align individual time series. Not all
          alignment functions may be applied to all time series, depending on the
          metric type and value type of the original time series. Alignment may
          change the metric type or the value type of the time series.

          Time series data must be aligned in order to perform cross-time series
          reduction. If ``crossSeriesReducer`` is specified, then
          ``perSeriesAligner`` must be specified and not equal ``ALIGN_NONE`` and
          ``alignmentPeriod`` must be specified; otherwise, an error is returned.
          REDUCE_PERCENTILE_50 (int): Signed fractions of a second at nanosecond resolution of the span of
          time. Durations less than one second are represented with a 0
          ``seconds`` field and a positive or negative ``nanos`` field. For
          durations of one second or more, a non-zero value for the ``nanos``
          field must be of the same sign as the ``seconds`` field. Must be from
          -999,999,999 to +999,999,999 inclusive.
          REDUCE_PERCENTILE_05 (int): The name of the uninterpreted option. Each string represents a
          segment in a dot-separated name. is_extension is true iff a segment
          represents an extension (denoted with parentheses in options specs in
          .proto files). E.g.,{ ["foo", false], ["bar.baz", true], ["qux", false]
          } represents "foo.(bar.baz).qux".
        """

        REDUCE_NONE = 0
        REDUCE_MEAN = 1
        REDUCE_MIN = 2
        REDUCE_MAX = 3
        REDUCE_SUM = 4
        REDUCE_STDDEV = 5
        REDUCE_COUNT = 6
        REDUCE_COUNT_TRUE = 7
        REDUCE_COUNT_FALSE = 15
        REDUCE_FRACTION_TRUE = 8
        REDUCE_PERCENTILE_99 = 9
        REDUCE_PERCENTILE_95 = 10
        REDUCE_PERCENTILE_50 = 11
        REDUCE_PERCENTILE_05 = 12


class ChartOptions(object):
    class Mode(enum.IntEnum):
        """
        Chart mode options.

        Attributes:
          MODE_UNSPECIFIED (int): The hostname for this service. This should be specified with no
          prefix or protocol.

          Example:

          service Foo { option (google.api.default_host) = "foo.googleapi.com";
          ... }
          COLOR (int): The chart distinguishes data series using different color. Line
          colors may get reused when there are many lines in the chart.
          X_RAY (int): The chart uses the Stackdriver x-ray mode, in which each
          data set is plotted using the same semi-transparent color.
          STATS (int): The chart displays statistics such as average, median, 95th percentile,
          and more.
        """

        MODE_UNSPECIFIED = 0
        COLOR = 1
        X_RAY = 2
        STATS = 3


class PickTimeSeriesFilter(object):
    class Direction(enum.IntEnum):
        """
        Describes the ranking directions.

        Attributes:
          DIRECTION_UNSPECIFIED (int): Not allowed in well-formed requests.
          TOP (int): Pass the highest ranking inputs.
          BOTTOM (int): Pass the lowest ranking inputs.
        """

        DIRECTION_UNSPECIFIED = 0
        TOP = 1
        BOTTOM = 2

    class Method(enum.IntEnum):
        """
        The value reducers that can be applied to a PickTimeSeriesFilter.

        Attributes:
          METHOD_UNSPECIFIED (int): Not allowed in well-formed requests.
          METHOD_MEAN (int): Select the mean of all values.
          METHOD_MAX (int): Select the maximum value.
          METHOD_MIN (int): Select the minimum value.
          METHOD_SUM (int): Compute the sum of all values.
          METHOD_LATEST (int): Select the most recent value.
        """

        METHOD_UNSPECIFIED = 0
        METHOD_MEAN = 1
        METHOD_MAX = 2
        METHOD_MIN = 3
        METHOD_SUM = 4
        METHOD_LATEST = 5


class StatisticalTimeSeriesFilter(object):
    class Method(enum.IntEnum):
        """
        The filter methods that can be applied to a stream.

        Attributes:
          METHOD_UNSPECIFIED (int): Not allowed in well-formed requests.
          METHOD_CLUSTER_OUTLIER (int): Compute the outlier score of each stream.
        """

        METHOD_UNSPECIFIED = 0
        METHOD_CLUSTER_OUTLIER = 1


class Text(object):
    class Format(enum.IntEnum):
        """
        The format type of the text content.

        Attributes:
          FORMAT_UNSPECIFIED (int): Format is unspecified. Defaults to MARKDOWN.
          MARKDOWN (int): The text contains Markdown formatting.
          RAW (int): The text contains no special formatting.
        """

        FORMAT_UNSPECIFIED = 0
        MARKDOWN = 1
        RAW = 2


class Threshold(object):
    class Color(enum.IntEnum):
        """
        The color suggests an interpretation to the viewer when actual values cross
        the threshold. Comments on each color provide UX guidance on how users can
        be expected to interpret a given state color.

        Attributes:
          COLOR_UNSPECIFIED (int): Color is unspecified. Not allowed in well-formed requests.
          YELLOW (int): Crossing the threshold is "concerning" behavior.
          RED (int): Crossing the threshold is "emergency" behavior.
        """

        COLOR_UNSPECIFIED = 0
        YELLOW = 4
        RED = 6

    class Direction(enum.IntEnum):
        """
        Whether the threshold is considered crossed by an actual value above or
        below its threshold value.

        Attributes:
          DIRECTION_UNSPECIFIED (int): Not allowed in well-formed requests.
          ABOVE (int): The threshold will be considered crossed if the actual value is above
          the threshold value.
          BELOW (int): The threshold will be considered crossed if the actual value is below
          the threshold value.
        """

        DIRECTION_UNSPECIFIED = 0
        ABOVE = 1
        BELOW = 2


class XyChart(object):
    class DataSet(object):
        class PlotType(enum.IntEnum):
            """
            The types of plotting strategies for data sets.

            Attributes:
              PLOT_TYPE_UNSPECIFIED (int): Defines the HTTP configuration for an API service. It contains a
              list of ``HttpRule``, each specifying the mapping of an RPC method to
              one or more HTTP REST API methods.
              LINE (int): The data is plotted as a set of lines (one line per series).
              STACKED_AREA (int): The data is plotted as a set of filled areas (one area per series),
              with the areas stacked vertically (the base of each area is the top of
              its predecessor, and the base of the first area is the X axis). Since
              the areas do not overlap, each is filled with a different opaque color.
              STACKED_BAR (int): The data is plotted as a set of rectangular boxes (one box per series),
              with the boxes stacked vertically (the base of each box is the top of
              its predecessor, and the base of the first box is the X axis). Since
              the boxes do not overlap, each is filled with a different opaque color.
              HEATMAP (int): Identifies which part of the FileDescriptorProto was defined at this
              location.

              Each element is a field number or an index. They form a path from the
              root FileDescriptorProto to the place where the definition. For example,
              this path: [ 4, 3, 2, 7, 1 ] refers to: file.message_type(3) // 4, 3
              .field(7) // 2, 7 .name() // 1 This is because
              FileDescriptorProto.message_type has field number 4: repeated
              DescriptorProto message_type = 4; and DescriptorProto.field has field
              number 2: repeated FieldDescriptorProto field = 2; and
              FieldDescriptorProto.name has field number 1: optional string name = 1;

              Thus, the above path gives the location of a field name. If we removed
              the last element: [ 4, 3, 2, 7 ] this path refers to the whole field
              declaration (from the beginning of the label to the terminating
              semicolon).
            """

            PLOT_TYPE_UNSPECIFIED = 0
            LINE = 1
            STACKED_AREA = 2
            STACKED_BAR = 3
            HEATMAP = 4

    class Axis(object):
        class Scale(enum.IntEnum):
            """
            Types of scales used in axes.

            Attributes:
              SCALE_UNSPECIFIED (int): A filter that defines a subset of time series data that is displayed
              in a widget. Time series data is fetched using the
              ```ListTimeSeries`` <https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list>`__
              method.
              LINEAR (int): Linear scale.
              LOG10 (int): Logarithmic scale (base 10).
            """

            SCALE_UNSPECIFIED = 0
            LINEAR = 1
            LOG10 = 2
