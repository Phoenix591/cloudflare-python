# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.zero_trust.tunnels.configuration_update_response import ConfigurationUpdateResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ...._base_client import make_request_options

from ....types.zero_trust.tunnels.configuration_get_response import ConfigurationGetResponse

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from ....types.zero_trust.tunnels import configuration_update_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.zero_trust.tunnels import configuration_update_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["ConfigurationsResource", "AsyncConfigurationsResource"]

class ConfigurationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigurationsResourceWithRawResponse:
        return ConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationsResourceWithStreamingResponse:
        return ConfigurationsResourceWithStreamingResponse(self)

    def update(self,
    tunnel_id: str,
    *,
    account_id: str,
    config: configuration_update_params.Config | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ConfigurationUpdateResponse]:
        """
        Adds or updates the configuration for a remotely-managed tunnel.

        Args:
          account_id: Identifier

          tunnel_id: UUID of the tunnel.

          config: The tunnel configuration and ingress rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not tunnel_id:
          raise ValueError(
            f'Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}'
          )
        return self._put(
            f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations",
            body=maybe_transform({
                "config": config
            }, configuration_update_params.ConfigurationUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[ConfigurationUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[ConfigurationUpdateResponse]], ResultWrapper[ConfigurationUpdateResponse]),
        )

    def get(self,
    tunnel_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ConfigurationGetResponse]:
        """
        Gets the configuration for a remotely-managed tunnel

        Args:
          account_id: Identifier

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not tunnel_id:
          raise ValueError(
            f'Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[ConfigurationGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[ConfigurationGetResponse]], ResultWrapper[ConfigurationGetResponse]),
        )

class AsyncConfigurationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigurationsResourceWithRawResponse:
        return AsyncConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        return AsyncConfigurationsResourceWithStreamingResponse(self)

    async def update(self,
    tunnel_id: str,
    *,
    account_id: str,
    config: configuration_update_params.Config | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ConfigurationUpdateResponse]:
        """
        Adds or updates the configuration for a remotely-managed tunnel.

        Args:
          account_id: Identifier

          tunnel_id: UUID of the tunnel.

          config: The tunnel configuration and ingress rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not tunnel_id:
          raise ValueError(
            f'Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}'
          )
        return await self._put(
            f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations",
            body=await async_maybe_transform({
                "config": config
            }, configuration_update_params.ConfigurationUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[ConfigurationUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[ConfigurationUpdateResponse]], ResultWrapper[ConfigurationUpdateResponse]),
        )

    async def get(self,
    tunnel_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ConfigurationGetResponse]:
        """
        Gets the configuration for a remotely-managed tunnel

        Args:
          account_id: Identifier

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not tunnel_id:
          raise ValueError(
            f'Expected a non-empty value for `tunnel_id` but received {tunnel_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[ConfigurationGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[ConfigurationGetResponse]], ResultWrapper[ConfigurationGetResponse]),
        )

class ConfigurationsResourceWithRawResponse:
    def __init__(self, configurations: ConfigurationsResource) -> None:
        self._configurations = configurations

        self.update = to_raw_response_wrapper(
            configurations.update,
        )
        self.get = to_raw_response_wrapper(
            configurations.get,
        )

class AsyncConfigurationsResourceWithRawResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.update = async_to_raw_response_wrapper(
            configurations.update,
        )
        self.get = async_to_raw_response_wrapper(
            configurations.get,
        )

class ConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: ConfigurationsResource) -> None:
        self._configurations = configurations

        self.update = to_streamed_response_wrapper(
            configurations.update,
        )
        self.get = to_streamed_response_wrapper(
            configurations.get,
        )

class AsyncConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.update = async_to_streamed_response_wrapper(
            configurations.update,
        )
        self.get = async_to_streamed_response_wrapper(
            configurations.get,
        )