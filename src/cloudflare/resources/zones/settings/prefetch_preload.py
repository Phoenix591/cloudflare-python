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
from ....types.zones.settings import prefetch_preload_edit_params
from ....types.zones.settings.prefetch_preload import PrefetchPreload

__all__ = ["PrefetchPreloadResource", "AsyncPrefetchPreloadResource"]


class PrefetchPreloadResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrefetchPreloadResourceWithRawResponse:
        return PrefetchPreloadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrefetchPreloadResourceWithStreamingResponse:
        return PrefetchPreloadResourceWithStreamingResponse(self)

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
    ) -> Optional[PrefetchPreload]:
        """
        Cloudflare will prefetch any URLs that are included in the response headers.
        This is limited to Enterprise Zones.

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
            f"/zones/{zone_id}/settings/prefetch_preload",
            body=maybe_transform({"value": value}, prefetch_preload_edit_params.PrefetchPreloadEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PrefetchPreload]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrefetchPreload]], ResultWrapper[PrefetchPreload]),
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
    ) -> Optional[PrefetchPreload]:
        """
        Cloudflare will prefetch any URLs that are included in the response headers.
        This is limited to Enterprise Zones.

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
            f"/zones/{zone_id}/settings/prefetch_preload",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PrefetchPreload]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrefetchPreload]], ResultWrapper[PrefetchPreload]),
        )


class AsyncPrefetchPreloadResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrefetchPreloadResourceWithRawResponse:
        return AsyncPrefetchPreloadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrefetchPreloadResourceWithStreamingResponse:
        return AsyncPrefetchPreloadResourceWithStreamingResponse(self)

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
    ) -> Optional[PrefetchPreload]:
        """
        Cloudflare will prefetch any URLs that are included in the response headers.
        This is limited to Enterprise Zones.

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
            f"/zones/{zone_id}/settings/prefetch_preload",
            body=await async_maybe_transform({"value": value}, prefetch_preload_edit_params.PrefetchPreloadEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PrefetchPreload]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrefetchPreload]], ResultWrapper[PrefetchPreload]),
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
    ) -> Optional[PrefetchPreload]:
        """
        Cloudflare will prefetch any URLs that are included in the response headers.
        This is limited to Enterprise Zones.

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
            f"/zones/{zone_id}/settings/prefetch_preload",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PrefetchPreload]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrefetchPreload]], ResultWrapper[PrefetchPreload]),
        )


class PrefetchPreloadResourceWithRawResponse:
    def __init__(self, prefetch_preload: PrefetchPreloadResource) -> None:
        self._prefetch_preload = prefetch_preload

        self.edit = to_raw_response_wrapper(
            prefetch_preload.edit,
        )
        self.get = to_raw_response_wrapper(
            prefetch_preload.get,
        )


class AsyncPrefetchPreloadResourceWithRawResponse:
    def __init__(self, prefetch_preload: AsyncPrefetchPreloadResource) -> None:
        self._prefetch_preload = prefetch_preload

        self.edit = async_to_raw_response_wrapper(
            prefetch_preload.edit,
        )
        self.get = async_to_raw_response_wrapper(
            prefetch_preload.get,
        )


class PrefetchPreloadResourceWithStreamingResponse:
    def __init__(self, prefetch_preload: PrefetchPreloadResource) -> None:
        self._prefetch_preload = prefetch_preload

        self.edit = to_streamed_response_wrapper(
            prefetch_preload.edit,
        )
        self.get = to_streamed_response_wrapper(
            prefetch_preload.get,
        )


class AsyncPrefetchPreloadResourceWithStreamingResponse:
    def __init__(self, prefetch_preload: AsyncPrefetchPreloadResource) -> None:
        self._prefetch_preload = prefetch_preload

        self.edit = async_to_streamed_response_wrapper(
            prefetch_preload.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            prefetch_preload.get,
        )
