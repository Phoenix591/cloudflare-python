# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .resource_groups import (
    ResourceGroupsResource,
    AsyncResourceGroupsResource,
    ResourceGroupsResourceWithRawResponse,
    AsyncResourceGroupsResourceWithRawResponse,
    ResourceGroupsResourceWithStreamingResponse,
    AsyncResourceGroupsResourceWithStreamingResponse,
)
from .permission_groups import (
    PermissionGroupsResource,
    AsyncPermissionGroupsResource,
    PermissionGroupsResourceWithRawResponse,
    AsyncPermissionGroupsResourceWithRawResponse,
    PermissionGroupsResourceWithStreamingResponse,
    AsyncPermissionGroupsResourceWithStreamingResponse,
)

__all__ = ["IAMResource", "AsyncIAMResource"]


class IAMResource(SyncAPIResource):
    @cached_property
    def permission_groups(self) -> PermissionGroupsResource:
        return PermissionGroupsResource(self._client)

    @cached_property
    def resource_groups(self) -> ResourceGroupsResource:
        return ResourceGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> IAMResourceWithRawResponse:
        return IAMResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IAMResourceWithStreamingResponse:
        return IAMResourceWithStreamingResponse(self)


class AsyncIAMResource(AsyncAPIResource):
    @cached_property
    def permission_groups(self) -> AsyncPermissionGroupsResource:
        return AsyncPermissionGroupsResource(self._client)

    @cached_property
    def resource_groups(self) -> AsyncResourceGroupsResource:
        return AsyncResourceGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIAMResourceWithRawResponse:
        return AsyncIAMResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIAMResourceWithStreamingResponse:
        return AsyncIAMResourceWithStreamingResponse(self)


class IAMResourceWithRawResponse:
    def __init__(self, iam: IAMResource) -> None:
        self._iam = iam

    @cached_property
    def permission_groups(self) -> PermissionGroupsResourceWithRawResponse:
        return PermissionGroupsResourceWithRawResponse(self._iam.permission_groups)

    @cached_property
    def resource_groups(self) -> ResourceGroupsResourceWithRawResponse:
        return ResourceGroupsResourceWithRawResponse(self._iam.resource_groups)


class AsyncIAMResourceWithRawResponse:
    def __init__(self, iam: AsyncIAMResource) -> None:
        self._iam = iam

    @cached_property
    def permission_groups(self) -> AsyncPermissionGroupsResourceWithRawResponse:
        return AsyncPermissionGroupsResourceWithRawResponse(self._iam.permission_groups)

    @cached_property
    def resource_groups(self) -> AsyncResourceGroupsResourceWithRawResponse:
        return AsyncResourceGroupsResourceWithRawResponse(self._iam.resource_groups)


class IAMResourceWithStreamingResponse:
    def __init__(self, iam: IAMResource) -> None:
        self._iam = iam

    @cached_property
    def permission_groups(self) -> PermissionGroupsResourceWithStreamingResponse:
        return PermissionGroupsResourceWithStreamingResponse(self._iam.permission_groups)

    @cached_property
    def resource_groups(self) -> ResourceGroupsResourceWithStreamingResponse:
        return ResourceGroupsResourceWithStreamingResponse(self._iam.resource_groups)


class AsyncIAMResourceWithStreamingResponse:
    def __init__(self, iam: AsyncIAMResource) -> None:
        self._iam = iam

    @cached_property
    def permission_groups(self) -> AsyncPermissionGroupsResourceWithStreamingResponse:
        return AsyncPermissionGroupsResourceWithStreamingResponse(self._iam.permission_groups)

    @cached_property
    def resource_groups(self) -> AsyncResourceGroupsResourceWithStreamingResponse:
        return AsyncResourceGroupsResourceWithStreamingResponse(self._iam.resource_groups)
