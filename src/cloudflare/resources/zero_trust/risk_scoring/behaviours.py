# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, cast

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
from ....types.zero_trust.risk_scoring import BehaviourGetResponse, BehaviourUpdateResponse, behaviour_update_params

__all__ = ["Behaviours", "AsyncBehaviours"]


class Behaviours(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BehavioursWithRawResponse:
        return BehavioursWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BehavioursWithStreamingResponse:
        return BehavioursWithStreamingResponse(self)

    def update(
        self,
        account_identifier: str,
        *,
        behaviors: Dict[str, behaviour_update_params.Behaviors] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BehaviourUpdateResponse:
        """
        Update configuration for risk behaviors

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._put(
            f"/accounts/{account_identifier}/zt_risk_scoring/behaviors",
            body=maybe_transform({"behaviors": behaviors}, behaviour_update_params.BehaviourUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BehaviourUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[BehaviourUpdateResponse], ResultWrapper[BehaviourUpdateResponse]),
        )

    def get(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BehaviourGetResponse:
        """
        Get all behaviors and associated configuration

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/zt_risk_scoring/behaviors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BehaviourGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[BehaviourGetResponse], ResultWrapper[BehaviourGetResponse]),
        )


class AsyncBehaviours(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBehavioursWithRawResponse:
        return AsyncBehavioursWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBehavioursWithStreamingResponse:
        return AsyncBehavioursWithStreamingResponse(self)

    async def update(
        self,
        account_identifier: str,
        *,
        behaviors: Dict[str, behaviour_update_params.Behaviors] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BehaviourUpdateResponse:
        """
        Update configuration for risk behaviors

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._put(
            f"/accounts/{account_identifier}/zt_risk_scoring/behaviors",
            body=await async_maybe_transform({"behaviors": behaviors}, behaviour_update_params.BehaviourUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BehaviourUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[BehaviourUpdateResponse], ResultWrapper[BehaviourUpdateResponse]),
        )

    async def get(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BehaviourGetResponse:
        """
        Get all behaviors and associated configuration

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/zt_risk_scoring/behaviors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BehaviourGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[BehaviourGetResponse], ResultWrapper[BehaviourGetResponse]),
        )


class BehavioursWithRawResponse:
    def __init__(self, behaviours: Behaviours) -> None:
        self._behaviours = behaviours

        self.update = to_raw_response_wrapper(
            behaviours.update,
        )
        self.get = to_raw_response_wrapper(
            behaviours.get,
        )


class AsyncBehavioursWithRawResponse:
    def __init__(self, behaviours: AsyncBehaviours) -> None:
        self._behaviours = behaviours

        self.update = async_to_raw_response_wrapper(
            behaviours.update,
        )
        self.get = async_to_raw_response_wrapper(
            behaviours.get,
        )


class BehavioursWithStreamingResponse:
    def __init__(self, behaviours: Behaviours) -> None:
        self._behaviours = behaviours

        self.update = to_streamed_response_wrapper(
            behaviours.update,
        )
        self.get = to_streamed_response_wrapper(
            behaviours.get,
        )


class AsyncBehavioursWithStreamingResponse:
    def __init__(self, behaviours: AsyncBehaviours) -> None:
        self._behaviours = behaviours

        self.update = async_to_streamed_response_wrapper(
            behaviours.update,
        )
        self.get = async_to_streamed_response_wrapper(
            behaviours.get,
        )