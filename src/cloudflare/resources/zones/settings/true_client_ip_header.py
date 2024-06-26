# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.zones.settings import true_client_ip_header_edit_params
from ....types.zones.settings.true_client_ip_header import TrueClientIPHeader

__all__ = ["TrueClientIPHeaderResource", "AsyncTrueClientIPHeaderResource"]


class TrueClientIPHeaderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrueClientIPHeaderResourceWithRawResponse:
        return TrueClientIPHeaderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrueClientIPHeaderResourceWithStreamingResponse:
        return TrueClientIPHeaderResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TrueClientIPHeader]:
        """
        Allows customer to continue to use True Client IP (Akamai feature) in the
        headers we send to the origin. This is limited to Enterprise Zones.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/true_client_ip_header",
            body=maybe_transform({"value": value}, true_client_ip_header_edit_params.TrueClientIPHeaderEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TrueClientIPHeader]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TrueClientIPHeader]], ResultWrapper[TrueClientIPHeader]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TrueClientIPHeader]:
        """
        Allows customer to continue to use True Client IP (Akamai feature) in the
        headers we send to the origin. This is limited to Enterprise Zones.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/true_client_ip_header",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TrueClientIPHeader]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TrueClientIPHeader]], ResultWrapper[TrueClientIPHeader]),
        )


class AsyncTrueClientIPHeaderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrueClientIPHeaderResourceWithRawResponse:
        return AsyncTrueClientIPHeaderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrueClientIPHeaderResourceWithStreamingResponse:
        return AsyncTrueClientIPHeaderResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TrueClientIPHeader]:
        """
        Allows customer to continue to use True Client IP (Akamai feature) in the
        headers we send to the origin. This is limited to Enterprise Zones.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/true_client_ip_header",
            body=await async_maybe_transform(
                {"value": value}, true_client_ip_header_edit_params.TrueClientIPHeaderEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TrueClientIPHeader]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TrueClientIPHeader]], ResultWrapper[TrueClientIPHeader]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TrueClientIPHeader]:
        """
        Allows customer to continue to use True Client IP (Akamai feature) in the
        headers we send to the origin. This is limited to Enterprise Zones.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/true_client_ip_header",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TrueClientIPHeader]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TrueClientIPHeader]], ResultWrapper[TrueClientIPHeader]),
        )


class TrueClientIPHeaderResourceWithRawResponse:
    def __init__(self, true_client_ip_header: TrueClientIPHeaderResource) -> None:
        self._true_client_ip_header = true_client_ip_header

        self.edit = to_raw_response_wrapper(
            true_client_ip_header.edit,
        )
        self.get = to_raw_response_wrapper(
            true_client_ip_header.get,
        )


class AsyncTrueClientIPHeaderResourceWithRawResponse:
    def __init__(self, true_client_ip_header: AsyncTrueClientIPHeaderResource) -> None:
        self._true_client_ip_header = true_client_ip_header

        self.edit = async_to_raw_response_wrapper(
            true_client_ip_header.edit,
        )
        self.get = async_to_raw_response_wrapper(
            true_client_ip_header.get,
        )


class TrueClientIPHeaderResourceWithStreamingResponse:
    def __init__(self, true_client_ip_header: TrueClientIPHeaderResource) -> None:
        self._true_client_ip_header = true_client_ip_header

        self.edit = to_streamed_response_wrapper(
            true_client_ip_header.edit,
        )
        self.get = to_streamed_response_wrapper(
            true_client_ip_header.get,
        )


class AsyncTrueClientIPHeaderResourceWithStreamingResponse:
    def __init__(self, true_client_ip_header: AsyncTrueClientIPHeaderResource) -> None:
        self._true_client_ip_header = true_client_ip_header

        self.edit = async_to_streamed_response_wrapper(
            true_client_ip_header.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            true_client_ip_header.get,
        )
