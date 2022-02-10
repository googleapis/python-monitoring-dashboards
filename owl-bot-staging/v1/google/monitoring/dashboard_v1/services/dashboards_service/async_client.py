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
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials   # type: ignore
from google.oauth2 import service_account              # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.monitoring.dashboard_v1.services.dashboards_service import pagers
from google.monitoring.dashboard_v1.types import dashboard
from google.monitoring.dashboard_v1.types import dashboards_service
from google.monitoring.dashboard_v1.types import layouts
from .transports.base import DashboardsServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import DashboardsServiceGrpcAsyncIOTransport
from .client import DashboardsServiceClient


class DashboardsServiceAsyncClient:
    """Manages Stackdriver dashboards. A dashboard is an arrangement
    of data display widgets in a specific layout.
    """

    _client: DashboardsServiceClient

    DEFAULT_ENDPOINT = DashboardsServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DashboardsServiceClient.DEFAULT_MTLS_ENDPOINT

    alert_policy_path = staticmethod(DashboardsServiceClient.alert_policy_path)
    parse_alert_policy_path = staticmethod(DashboardsServiceClient.parse_alert_policy_path)
    dashboard_path = staticmethod(DashboardsServiceClient.dashboard_path)
    parse_dashboard_path = staticmethod(DashboardsServiceClient.parse_dashboard_path)
    common_billing_account_path = staticmethod(DashboardsServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(DashboardsServiceClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(DashboardsServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(DashboardsServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(DashboardsServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(DashboardsServiceClient.parse_common_organization_path)
    common_project_path = staticmethod(DashboardsServiceClient.common_project_path)
    parse_common_project_path = staticmethod(DashboardsServiceClient.parse_common_project_path)
    common_location_path = staticmethod(DashboardsServiceClient.common_location_path)
    parse_common_location_path = staticmethod(DashboardsServiceClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DashboardsServiceAsyncClient: The constructed client.
        """
        return DashboardsServiceClient.from_service_account_info.__func__(DashboardsServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DashboardsServiceAsyncClient: The constructed client.
        """
        return DashboardsServiceClient.from_service_account_file.__func__(DashboardsServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(cls, client_options: Optional[ClientOptions] = None):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return DashboardsServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> DashboardsServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            DashboardsServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(DashboardsServiceClient).get_transport_class, type(DashboardsServiceClient))

    def __init__(self, *,
            credentials: ga_credentials.Credentials = None,
            transport: Union[str, DashboardsServiceTransport] = "grpc_asyncio",
            client_options: ClientOptions = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the dashboards service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.DashboardsServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = DashboardsServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,

        )

    async def create_dashboard(self,
            request: Union[dashboards_service.CreateDashboardRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> dashboard.Dashboard:
        r"""Creates a new custom dashboard. For examples on how you can use
        this API to create dashboards, see `Managing dashboards by
        API <https://cloud.google.com/monitoring/dashboards/api-dashboard>`__.
        This method requires the ``monitoring.dashboards.create``
        permission on the specified project. For more information about
        permissions, see `Cloud Identity and Access
        Management <https://cloud.google.com/iam>`__.


        .. code-block::

            from google.monitoring import dashboard_v1

            def sample_create_dashboard():
                # Create a client
                client = dashboard_v1.DashboardsServiceClient()

                # Initialize request argument(s)
                dashboard = dashboard_v1.Dashboard()
                dashboard.display_name = "display_name_value"

                request = dashboard_v1.CreateDashboardRequest(
                    parent="parent_value",
                    dashboard=dashboard,
                )

                # Make the request
                response = client.create_dashboard(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.monitoring.dashboard_v1.types.CreateDashboardRequest, dict]):
                The request object. The `CreateDashboard` request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.monitoring.dashboard_v1.types.Dashboard:
                A Google Stackdriver dashboard.
                Dashboards define the content and layout
                of pages in the Stackdriver web
                application.

        """
        # Create or coerce a protobuf request object.
        request = dashboards_service.CreateDashboardRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_dashboard,
            default_timeout=30.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_dashboards(self,
            request: Union[dashboards_service.ListDashboardsRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListDashboardsAsyncPager:
        r"""Lists the existing dashboards.

        This method requires the ``monitoring.dashboards.list``
        permission on the specified project. For more information, see
        `Cloud Identity and Access
        Management <https://cloud.google.com/iam>`__.


        .. code-block::

            from google.monitoring import dashboard_v1

            def sample_list_dashboards():
                # Create a client
                client = dashboard_v1.DashboardsServiceClient()

                # Initialize request argument(s)
                request = dashboard_v1.ListDashboardsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_dashboards(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.monitoring.dashboard_v1.types.ListDashboardsRequest, dict]):
                The request object. The `ListDashboards` request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.monitoring.dashboard_v1.services.dashboards_service.pagers.ListDashboardsAsyncPager:
                The ListDashboards request.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        request = dashboards_service.ListDashboardsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_dashboards,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListDashboardsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_dashboard(self,
            request: Union[dashboards_service.GetDashboardRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> dashboard.Dashboard:
        r"""Fetches a specific dashboard.

        This method requires the ``monitoring.dashboards.get``
        permission on the specified dashboard. For more information, see
        `Cloud Identity and Access
        Management <https://cloud.google.com/iam>`__.


        .. code-block::

            from google.monitoring import dashboard_v1

            def sample_get_dashboard():
                # Create a client
                client = dashboard_v1.DashboardsServiceClient()

                # Initialize request argument(s)
                request = dashboard_v1.GetDashboardRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_dashboard(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.monitoring.dashboard_v1.types.GetDashboardRequest, dict]):
                The request object. The `GetDashboard` request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.monitoring.dashboard_v1.types.Dashboard:
                A Google Stackdriver dashboard.
                Dashboards define the content and layout
                of pages in the Stackdriver web
                application.

        """
        # Create or coerce a protobuf request object.
        request = dashboards_service.GetDashboardRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_dashboard,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_dashboard(self,
            request: Union[dashboards_service.DeleteDashboardRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> None:
        r"""Deletes an existing custom dashboard.

        This method requires the ``monitoring.dashboards.delete``
        permission on the specified dashboard. For more information, see
        `Cloud Identity and Access
        Management <https://cloud.google.com/iam>`__.


        .. code-block::

            from google.monitoring import dashboard_v1

            def sample_delete_dashboard():
                # Create a client
                client = dashboard_v1.DashboardsServiceClient()

                # Initialize request argument(s)
                request = dashboard_v1.DeleteDashboardRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_dashboard(request=request)

        Args:
            request (Union[google.monitoring.dashboard_v1.types.DeleteDashboardRequest, dict]):
                The request object. The `DeleteDashboard` request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        request = dashboards_service.DeleteDashboardRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_dashboard,
            default_timeout=30.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def update_dashboard(self,
            request: Union[dashboards_service.UpdateDashboardRequest, dict] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> dashboard.Dashboard:
        r"""Replaces an existing custom dashboard with a new definition.

        This method requires the ``monitoring.dashboards.update``
        permission on the specified dashboard. For more information, see
        `Cloud Identity and Access
        Management <https://cloud.google.com/iam>`__.


        .. code-block::

            from google.monitoring import dashboard_v1

            def sample_update_dashboard():
                # Create a client
                client = dashboard_v1.DashboardsServiceClient()

                # Initialize request argument(s)
                dashboard = dashboard_v1.Dashboard()
                dashboard.display_name = "display_name_value"

                request = dashboard_v1.UpdateDashboardRequest(
                    dashboard=dashboard,
                )

                # Make the request
                response = client.update_dashboard(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.monitoring.dashboard_v1.types.UpdateDashboardRequest, dict]):
                The request object. The `UpdateDashboard` request.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.monitoring.dashboard_v1.types.Dashboard:
                A Google Stackdriver dashboard.
                Dashboards define the content and layout
                of pages in the Stackdriver web
                application.

        """
        # Create or coerce a protobuf request object.
        request = dashboards_service.UpdateDashboardRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_dashboard,
            default_timeout=30.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("dashboard.name", request.dashboard.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-monitoring-dashboard",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = (
    "DashboardsServiceAsyncClient",
)