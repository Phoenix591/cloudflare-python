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
from ....types.zones.settings import hotlink_protection_edit_params
from ....types.zones.settings.hotlink_protection import HotlinkProtection

__all__ = ["HotlinkProtectionResource", "AsyncHotlinkProtectionResource"]


class HotlinkProtectionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HotlinkProtectionResourceWithRawResponse:
        return HotlinkProtectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HotlinkProtectionResourceWithStreamingResponse:
        return HotlinkProtectionResourceWithStreamingResponse(self)

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
    ) -> Optional[HotlinkProtection]:
        """
        When enabled, the Hotlink Protection option ensures that other sites cannot suck
        up your bandwidth by building pages that use images hosted on your site. Anytime
        a request for an image on your site hits Cloudflare, we check to ensure that
        it's not another site requesting them. People will still be able to download and
        view images from your page, but other sites won't be able to steal them for use
        on their own pages.
        (https://support.cloudflare.com/hc/en-us/articles/200170026).

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
            f"/zones/{zone_id}/settings/hotlink_protection",
            body=maybe_transform({"value": value}, hotlink_protection_edit_params.HotlinkProtectionEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[HotlinkProtection]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HotlinkProtection]], ResultWrapper[HotlinkProtection]),
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
    ) -> Optional[HotlinkProtection]:
        """
        When enabled, the Hotlink Protection option ensures that other sites cannot suck
        up your bandwidth by building pages that use images hosted on your site. Anytime
        a request for an image on your site hits Cloudflare, we check to ensure that
        it's not another site requesting them. People will still be able to download and
        view images from your page, but other sites won't be able to steal them for use
        on their own pages.
        (https://support.cloudflare.com/hc/en-us/articles/200170026).

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
            f"/zones/{zone_id}/settings/hotlink_protection",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[HotlinkProtection]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HotlinkProtection]], ResultWrapper[HotlinkProtection]),
        )


class AsyncHotlinkProtectionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHotlinkProtectionResourceWithRawResponse:
        return AsyncHotlinkProtectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHotlinkProtectionResourceWithStreamingResponse:
        return AsyncHotlinkProtectionResourceWithStreamingResponse(self)

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
    ) -> Optional[HotlinkProtection]:
        """
        When enabled, the Hotlink Protection option ensures that other sites cannot suck
        up your bandwidth by building pages that use images hosted on your site. Anytime
        a request for an image on your site hits Cloudflare, we check to ensure that
        it's not another site requesting them. People will still be able to download and
        view images from your page, but other sites won't be able to steal them for use
        on their own pages.
        (https://support.cloudflare.com/hc/en-us/articles/200170026).

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
            f"/zones/{zone_id}/settings/hotlink_protection",
            body=await async_maybe_transform(
                {"value": value}, hotlink_protection_edit_params.HotlinkProtectionEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[HotlinkProtection]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HotlinkProtection]], ResultWrapper[HotlinkProtection]),
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
    ) -> Optional[HotlinkProtection]:
        """
        When enabled, the Hotlink Protection option ensures that other sites cannot suck
        up your bandwidth by building pages that use images hosted on your site. Anytime
        a request for an image on your site hits Cloudflare, we check to ensure that
        it's not another site requesting them. People will still be able to download and
        view images from your page, but other sites won't be able to steal them for use
        on their own pages.
        (https://support.cloudflare.com/hc/en-us/articles/200170026).

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
            f"/zones/{zone_id}/settings/hotlink_protection",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[HotlinkProtection]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HotlinkProtection]], ResultWrapper[HotlinkProtection]),
        )


class HotlinkProtectionResourceWithRawResponse:
    def __init__(self, hotlink_protection: HotlinkProtectionResource) -> None:
        self._hotlink_protection = hotlink_protection

        self.edit = to_raw_response_wrapper(
            hotlink_protection.edit,
        )
        self.get = to_raw_response_wrapper(
            hotlink_protection.get,
        )


class AsyncHotlinkProtectionResourceWithRawResponse:
    def __init__(self, hotlink_protection: AsyncHotlinkProtectionResource) -> None:
        self._hotlink_protection = hotlink_protection

        self.edit = async_to_raw_response_wrapper(
            hotlink_protection.edit,
        )
        self.get = async_to_raw_response_wrapper(
            hotlink_protection.get,
        )


class HotlinkProtectionResourceWithStreamingResponse:
    def __init__(self, hotlink_protection: HotlinkProtectionResource) -> None:
        self._hotlink_protection = hotlink_protection

        self.edit = to_streamed_response_wrapper(
            hotlink_protection.edit,
        )
        self.get = to_streamed_response_wrapper(
            hotlink_protection.get,
        )


class AsyncHotlinkProtectionResourceWithStreamingResponse:
    def __init__(self, hotlink_protection: AsyncHotlinkProtectionResource) -> None:
        self._hotlink_protection = hotlink_protection

        self.edit = async_to_streamed_response_wrapper(
            hotlink_protection.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            hotlink_protection.get,
        )
