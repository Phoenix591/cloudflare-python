# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .custom import CustomResource, AsyncCustomResource

from ....._compat import cached_property

from .predefined import PredefinedResource, AsyncPredefinedResource

from .....types.zero_trust.dlp.profile import Profile

from .....pagination import SyncSinglePage, AsyncSinglePage

from ....._base_client import make_request_options, AsyncPaginator

from ....._wrappers import ResultWrapper

from typing import Optional

from ....._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .custom import CustomResource, AsyncCustomResource, CustomResourceWithRawResponse, AsyncCustomResourceWithRawResponse, CustomResourceWithStreamingResponse, AsyncCustomResourceWithStreamingResponse
from .predefined import PredefinedResource, AsyncPredefinedResource, PredefinedResourceWithRawResponse, AsyncPredefinedResourceWithRawResponse, PredefinedResourceWithStreamingResponse, AsyncPredefinedResourceWithStreamingResponse
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["ProfilesResource", "AsyncProfilesResource"]

class ProfilesResource(SyncAPIResource):
    @cached_property
    def custom(self) -> CustomResource:
        return CustomResource(self._client)

    @cached_property
    def predefined(self) -> PredefinedResource:
        return PredefinedResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProfilesResourceWithRawResponse:
        return ProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfilesResourceWithStreamingResponse:
        return ProfilesResourceWithStreamingResponse(self)

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncSinglePage[Profile]:
        """
        Lists all DLP profiles in an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/dlp/profiles",
            page = SyncSinglePage[Profile],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=cast(Any, Profile),  # Union types cannot be passed in as arguments in the type system
        )

    def get(self,
    profile_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Profile]:
        """
        Fetches a DLP profile by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not profile_id:
          raise ValueError(
            f'Expected a non-empty value for `profile_id` but received {profile_id!r}'
          )
        return cast(Optional[Profile], self._get(
            f"/accounts/{account_id}/dlp/profiles/{profile_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Profile]]._unwrapper),
            cast_to=cast(Any, ResultWrapper[Profile]),  # Union types cannot be passed in as arguments in the type system
        ))

class AsyncProfilesResource(AsyncAPIResource):
    @cached_property
    def custom(self) -> AsyncCustomResource:
        return AsyncCustomResource(self._client)

    @cached_property
    def predefined(self) -> AsyncPredefinedResource:
        return AsyncPredefinedResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProfilesResourceWithRawResponse:
        return AsyncProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfilesResourceWithStreamingResponse:
        return AsyncProfilesResourceWithStreamingResponse(self)

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[Profile, AsyncSinglePage[Profile]]:
        """
        Lists all DLP profiles in an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/dlp/profiles",
            page = AsyncSinglePage[Profile],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=cast(Any, Profile),  # Union types cannot be passed in as arguments in the type system
        )

    async def get(self,
    profile_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Profile]:
        """
        Fetches a DLP profile by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not profile_id:
          raise ValueError(
            f'Expected a non-empty value for `profile_id` but received {profile_id!r}'
          )
        return cast(Optional[Profile], await self._get(
            f"/accounts/{account_id}/dlp/profiles/{profile_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Profile]]._unwrapper),
            cast_to=cast(Any, ResultWrapper[Profile]),  # Union types cannot be passed in as arguments in the type system
        ))

class ProfilesResourceWithRawResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.list = to_raw_response_wrapper(
            profiles.list,
        )
        self.get = to_raw_response_wrapper(
            profiles.get,
        )

    @cached_property
    def custom(self) -> CustomResourceWithRawResponse:
        return CustomResourceWithRawResponse(self._profiles.custom)

    @cached_property
    def predefined(self) -> PredefinedResourceWithRawResponse:
        return PredefinedResourceWithRawResponse(self._profiles.predefined)

class AsyncProfilesResourceWithRawResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.list = async_to_raw_response_wrapper(
            profiles.list,
        )
        self.get = async_to_raw_response_wrapper(
            profiles.get,
        )

    @cached_property
    def custom(self) -> AsyncCustomResourceWithRawResponse:
        return AsyncCustomResourceWithRawResponse(self._profiles.custom)

    @cached_property
    def predefined(self) -> AsyncPredefinedResourceWithRawResponse:
        return AsyncPredefinedResourceWithRawResponse(self._profiles.predefined)

class ProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.list = to_streamed_response_wrapper(
            profiles.list,
        )
        self.get = to_streamed_response_wrapper(
            profiles.get,
        )

    @cached_property
    def custom(self) -> CustomResourceWithStreamingResponse:
        return CustomResourceWithStreamingResponse(self._profiles.custom)

    @cached_property
    def predefined(self) -> PredefinedResourceWithStreamingResponse:
        return PredefinedResourceWithStreamingResponse(self._profiles.predefined)

class AsyncProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.list = async_to_streamed_response_wrapper(
            profiles.list,
        )
        self.get = async_to_streamed_response_wrapper(
            profiles.get,
        )

    @cached_property
    def custom(self) -> AsyncCustomResourceWithStreamingResponse:
        return AsyncCustomResourceWithStreamingResponse(self._profiles.custom)

    @cached_property
    def predefined(self) -> AsyncPredefinedResourceWithStreamingResponse:
        return AsyncPredefinedResourceWithStreamingResponse(self._profiles.predefined)