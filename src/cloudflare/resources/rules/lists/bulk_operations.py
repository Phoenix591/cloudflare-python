# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.rules.lists.bulk_operation_get_response import BulkOperationGetResponse

from ...._wrappers import ResultWrapper

from typing import Optional, Type

from ...._base_client import make_request_options

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from typing import cast
from typing import cast

__all__ = ["BulkOperationsResource", "AsyncBulkOperationsResource"]

class BulkOperationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulkOperationsResourceWithRawResponse:
        return BulkOperationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkOperationsResourceWithStreamingResponse:
        return BulkOperationsResourceWithStreamingResponse(self)

    def get(self,
    operation_id: str,
    *,
    account_identifier: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[BulkOperationGetResponse]:
        """
        Gets the current status of an asynchronous operation on a list.

        The `status` property can have one of the following values: `pending`,
        `running`, `completed`, or `failed`. If the status is `failed`, the `error`
        property will contain a message describing the error.

        Args:
          account_identifier: Identifier

          operation_id: The unique operation ID of the asynchronous action.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
          raise ValueError(
            f'Expected a non-empty value for `account_identifier` but received {account_identifier!r}'
          )
        if not operation_id:
          raise ValueError(
            f'Expected a non-empty value for `operation_id` but received {operation_id!r}'
          )
        return self._get(
            f"/accounts/{account_identifier}/rules/lists/bulk_operations/{operation_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[BulkOperationGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[BulkOperationGetResponse]], ResultWrapper[BulkOperationGetResponse]),
        )

class AsyncBulkOperationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulkOperationsResourceWithRawResponse:
        return AsyncBulkOperationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkOperationsResourceWithStreamingResponse:
        return AsyncBulkOperationsResourceWithStreamingResponse(self)

    async def get(self,
    operation_id: str,
    *,
    account_identifier: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[BulkOperationGetResponse]:
        """
        Gets the current status of an asynchronous operation on a list.

        The `status` property can have one of the following values: `pending`,
        `running`, `completed`, or `failed`. If the status is `failed`, the `error`
        property will contain a message describing the error.

        Args:
          account_identifier: Identifier

          operation_id: The unique operation ID of the asynchronous action.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
          raise ValueError(
            f'Expected a non-empty value for `account_identifier` but received {account_identifier!r}'
          )
        if not operation_id:
          raise ValueError(
            f'Expected a non-empty value for `operation_id` but received {operation_id!r}'
          )
        return await self._get(
            f"/accounts/{account_identifier}/rules/lists/bulk_operations/{operation_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[BulkOperationGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[BulkOperationGetResponse]], ResultWrapper[BulkOperationGetResponse]),
        )

class BulkOperationsResourceWithRawResponse:
    def __init__(self, bulk_operations: BulkOperationsResource) -> None:
        self._bulk_operations = bulk_operations

        self.get = to_raw_response_wrapper(
            bulk_operations.get,
        )

class AsyncBulkOperationsResourceWithRawResponse:
    def __init__(self, bulk_operations: AsyncBulkOperationsResource) -> None:
        self._bulk_operations = bulk_operations

        self.get = async_to_raw_response_wrapper(
            bulk_operations.get,
        )

class BulkOperationsResourceWithStreamingResponse:
    def __init__(self, bulk_operations: BulkOperationsResource) -> None:
        self._bulk_operations = bulk_operations

        self.get = to_streamed_response_wrapper(
            bulk_operations.get,
        )

class AsyncBulkOperationsResourceWithStreamingResponse:
    def __init__(self, bulk_operations: AsyncBulkOperationsResource) -> None:
        self._bulk_operations = bulk_operations

        self.get = async_to_streamed_response_wrapper(
            bulk_operations.get,
        )