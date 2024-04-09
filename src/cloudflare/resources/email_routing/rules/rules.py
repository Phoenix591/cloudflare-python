# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from .catch_alls import (
    CatchAlls,
    AsyncCatchAlls,
    CatchAllsWithRawResponse,
    AsyncCatchAllsWithRawResponse,
    CatchAllsWithStreamingResponse,
    AsyncCatchAllsWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.email_routing import (
    ActionParam,
    MatcherParam,
    EmailRoutingRule,
    rule_list_params,
    rule_create_params,
    rule_update_params,
)

__all__ = ["Rules", "AsyncRules"]


class Rules(SyncAPIResource):
    @cached_property
    def catch_alls(self) -> CatchAlls:
        return CatchAlls(self._client)

    @cached_property
    def with_raw_response(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self)

    def create(
        self,
        zone_identifier: str,
        *,
        actions: Iterable[ActionParam],
        matchers: Iterable[MatcherParam],
        enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailRoutingRule:
        """
        Rules consist of a set of criteria for matching emails (such as an email being
        sent to a specific custom email address) plus a set of actions to take on the
        email (like forwarding it to a specific destination address).

        Args:
          zone_identifier: Identifier

          actions: List actions patterns.

          matchers: Matching patterns to forward to your actions.

          enabled: Routing rule status.

          name: Routing rule name.

          priority: Priority of the routing rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/email/routing/rules",
            body=maybe_transform(
                {
                    "actions": actions,
                    "matchers": matchers,
                    "enabled": enabled,
                    "name": name,
                    "priority": priority,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EmailRoutingRule], ResultWrapper[EmailRoutingRule]),
        )

    def update(
        self,
        rule_identifier: str,
        *,
        zone_identifier: str,
        actions: Iterable[ActionParam],
        matchers: Iterable[MatcherParam],
        enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailRoutingRule:
        """
        Update actions and matches, or enable/disable specific routing rules.

        Args:
          zone_identifier: Identifier

          rule_identifier: Routing rule identifier.

          actions: List actions patterns.

          matchers: Matching patterns to forward to your actions.

          enabled: Routing rule status.

          name: Routing rule name.

          priority: Priority of the routing rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not rule_identifier:
            raise ValueError(f"Expected a non-empty value for `rule_identifier` but received {rule_identifier!r}")
        return self._put(
            f"/zones/{zone_identifier}/email/routing/rules/{rule_identifier}",
            body=maybe_transform(
                {
                    "actions": actions,
                    "matchers": matchers,
                    "enabled": enabled,
                    "name": name,
                    "priority": priority,
                },
                rule_update_params.RuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EmailRoutingRule], ResultWrapper[EmailRoutingRule]),
        )

    def list(
        self,
        zone_identifier: str,
        *,
        enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[EmailRoutingRule]:
        """
        Lists existing routing rules.

        Args:
          zone_identifier: Identifier

          enabled: Filter by enabled routing rules.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get_api_list(
            f"/zones/{zone_identifier}/email/routing/rules",
            page=SyncV4PagePaginationArray[EmailRoutingRule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "enabled": enabled,
                        "page": page,
                        "per_page": per_page,
                    },
                    rule_list_params.RuleListParams,
                ),
            ),
            model=EmailRoutingRule,
        )

    def delete(
        self,
        rule_identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailRoutingRule:
        """
        Delete a specific routing rule.

        Args:
          zone_identifier: Identifier

          rule_identifier: Routing rule identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not rule_identifier:
            raise ValueError(f"Expected a non-empty value for `rule_identifier` but received {rule_identifier!r}")
        return self._delete(
            f"/zones/{zone_identifier}/email/routing/rules/{rule_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EmailRoutingRule], ResultWrapper[EmailRoutingRule]),
        )

    def get(
        self,
        rule_identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailRoutingRule:
        """
        Get information for a specific routing rule already created.

        Args:
          zone_identifier: Identifier

          rule_identifier: Routing rule identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not rule_identifier:
            raise ValueError(f"Expected a non-empty value for `rule_identifier` but received {rule_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/email/routing/rules/{rule_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EmailRoutingRule], ResultWrapper[EmailRoutingRule]),
        )


class AsyncRules(AsyncAPIResource):
    @cached_property
    def catch_alls(self) -> AsyncCatchAlls:
        return AsyncCatchAlls(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self)

    async def create(
        self,
        zone_identifier: str,
        *,
        actions: Iterable[ActionParam],
        matchers: Iterable[MatcherParam],
        enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailRoutingRule:
        """
        Rules consist of a set of criteria for matching emails (such as an email being
        sent to a specific custom email address) plus a set of actions to take on the
        email (like forwarding it to a specific destination address).

        Args:
          zone_identifier: Identifier

          actions: List actions patterns.

          matchers: Matching patterns to forward to your actions.

          enabled: Routing rule status.

          name: Routing rule name.

          priority: Priority of the routing rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/email/routing/rules",
            body=await async_maybe_transform(
                {
                    "actions": actions,
                    "matchers": matchers,
                    "enabled": enabled,
                    "name": name,
                    "priority": priority,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EmailRoutingRule], ResultWrapper[EmailRoutingRule]),
        )

    async def update(
        self,
        rule_identifier: str,
        *,
        zone_identifier: str,
        actions: Iterable[ActionParam],
        matchers: Iterable[MatcherParam],
        enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailRoutingRule:
        """
        Update actions and matches, or enable/disable specific routing rules.

        Args:
          zone_identifier: Identifier

          rule_identifier: Routing rule identifier.

          actions: List actions patterns.

          matchers: Matching patterns to forward to your actions.

          enabled: Routing rule status.

          name: Routing rule name.

          priority: Priority of the routing rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not rule_identifier:
            raise ValueError(f"Expected a non-empty value for `rule_identifier` but received {rule_identifier!r}")
        return await self._put(
            f"/zones/{zone_identifier}/email/routing/rules/{rule_identifier}",
            body=await async_maybe_transform(
                {
                    "actions": actions,
                    "matchers": matchers,
                    "enabled": enabled,
                    "name": name,
                    "priority": priority,
                },
                rule_update_params.RuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EmailRoutingRule], ResultWrapper[EmailRoutingRule]),
        )

    def list(
        self,
        zone_identifier: str,
        *,
        enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EmailRoutingRule, AsyncV4PagePaginationArray[EmailRoutingRule]]:
        """
        Lists existing routing rules.

        Args:
          zone_identifier: Identifier

          enabled: Filter by enabled routing rules.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get_api_list(
            f"/zones/{zone_identifier}/email/routing/rules",
            page=AsyncV4PagePaginationArray[EmailRoutingRule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "enabled": enabled,
                        "page": page,
                        "per_page": per_page,
                    },
                    rule_list_params.RuleListParams,
                ),
            ),
            model=EmailRoutingRule,
        )

    async def delete(
        self,
        rule_identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailRoutingRule:
        """
        Delete a specific routing rule.

        Args:
          zone_identifier: Identifier

          rule_identifier: Routing rule identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not rule_identifier:
            raise ValueError(f"Expected a non-empty value for `rule_identifier` but received {rule_identifier!r}")
        return await self._delete(
            f"/zones/{zone_identifier}/email/routing/rules/{rule_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EmailRoutingRule], ResultWrapper[EmailRoutingRule]),
        )

    async def get(
        self,
        rule_identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailRoutingRule:
        """
        Get information for a specific routing rule already created.

        Args:
          zone_identifier: Identifier

          rule_identifier: Routing rule identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not rule_identifier:
            raise ValueError(f"Expected a non-empty value for `rule_identifier` but received {rule_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/email/routing/rules/{rule_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EmailRoutingRule], ResultWrapper[EmailRoutingRule]),
        )


class RulesWithRawResponse:
    def __init__(self, rules: Rules) -> None:
        self._rules = rules

        self.create = to_raw_response_wrapper(
            rules.create,
        )
        self.update = to_raw_response_wrapper(
            rules.update,
        )
        self.list = to_raw_response_wrapper(
            rules.list,
        )
        self.delete = to_raw_response_wrapper(
            rules.delete,
        )
        self.get = to_raw_response_wrapper(
            rules.get,
        )

    @cached_property
    def catch_alls(self) -> CatchAllsWithRawResponse:
        return CatchAllsWithRawResponse(self._rules.catch_alls)


class AsyncRulesWithRawResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

        self.create = async_to_raw_response_wrapper(
            rules.create,
        )
        self.update = async_to_raw_response_wrapper(
            rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
        )
        self.get = async_to_raw_response_wrapper(
            rules.get,
        )

    @cached_property
    def catch_alls(self) -> AsyncCatchAllsWithRawResponse:
        return AsyncCatchAllsWithRawResponse(self._rules.catch_alls)


class RulesWithStreamingResponse:
    def __init__(self, rules: Rules) -> None:
        self._rules = rules

        self.create = to_streamed_response_wrapper(
            rules.create,
        )
        self.update = to_streamed_response_wrapper(
            rules.update,
        )
        self.list = to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )
        self.get = to_streamed_response_wrapper(
            rules.get,
        )

    @cached_property
    def catch_alls(self) -> CatchAllsWithStreamingResponse:
        return CatchAllsWithStreamingResponse(self._rules.catch_alls)


class AsyncRulesWithStreamingResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

        self.create = async_to_streamed_response_wrapper(
            rules.create,
        )
        self.update = async_to_streamed_response_wrapper(
            rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            rules.get,
        )

    @cached_property
    def catch_alls(self) -> AsyncCatchAllsWithStreamingResponse:
        return AsyncCatchAllsWithStreamingResponse(self._rules.catch_alls)
