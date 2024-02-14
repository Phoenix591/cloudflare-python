# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Type, cast, overload

import httpx

from .keys import (
    Keys,
    AsyncKeys,
    KeysWithRawResponse,
    AsyncKeysWithRawResponse,
    KeysWithStreamingResponse,
    AsyncKeysWithStreamingResponse,
)
from .blobs import (
    Blobs,
    AsyncBlobs,
    BlobsWithRawResponse,
    AsyncBlobsWithRawResponse,
    BlobsWithStreamingResponse,
    AsyncBlobsWithStreamingResponse,
)
from .stats import (
    Stats,
    AsyncStats,
    StatsWithRawResponse,
    AsyncStatsWithRawResponse,
    StatsWithStreamingResponse,
    AsyncStatsWithStreamingResponse,
)
from .variants import (
    Variants,
    AsyncVariants,
    VariantsWithRawResponse,
    AsyncVariantsWithRawResponse,
    VariantsWithStreamingResponse,
    AsyncVariantsWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import required_args, maybe_transform
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
from ....types.images import (
    V1GetResponse,
    V1DeleteResponse,
    V1UpdateResponse,
    V1CloudflareImagesListImagesResponse,
    V1CloudflareImagesUploadAnImageViaURLResponse,
    v1_update_params,
    v1_cloudflare_images_list_images_params,
    v1_cloudflare_images_upload_an_image_via_url_params,
)

__all__ = ["V1s", "AsyncV1s"]


class V1s(SyncAPIResource):
    @cached_property
    def keys(self) -> Keys:
        return Keys(self._client)

    @cached_property
    def stats(self) -> Stats:
        return Stats(self._client)

    @cached_property
    def variants(self) -> Variants:
        return Variants(self._client)

    @cached_property
    def blobs(self) -> Blobs:
        return Blobs(self._client)

    @cached_property
    def with_raw_response(self) -> V1sWithRawResponse:
        return V1sWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1sWithStreamingResponse:
        return V1sWithStreamingResponse(self)

    def update(
        self,
        image_id: str,
        *,
        account_id: str,
        metadata: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1UpdateResponse:
        """Update image access control.

        On access control change, all copies of the image
        are purged from cache.

        Args:
          account_id: Account identifier tag.

          image_id: Image unique identifier.

          metadata: User modifiable key-value store. Can be used for keeping references to another
              system of record for managing images. No change if not specified.

          require_signed_urls: Indicates whether the image can be accessed using only its UID. If set to
              `true`, a signed token needs to be generated with a signing key to view the
              image. Returns a new UID on a change. No change if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return self._patch(
            f"/accounts/{account_id}/images/v1/{image_id}",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "require_signed_urls": require_signed_urls,
                },
                v1_update_params.V1UpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[V1UpdateResponse], ResultWrapper[V1UpdateResponse]),
        )

    def delete(
        self,
        image_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1DeleteResponse:
        """Delete an image on Cloudflare Images.

        On success, all copies of the image are
        deleted and purged from cache.

        Args:
          account_id: Account identifier tag.

          image_id: Image unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return cast(
            V1DeleteResponse,
            self._delete(
                f"/accounts/{account_id}/images/v1/{image_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[V1DeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def cloudflare_images_list_images(
        self,
        account_id: str,
        *,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1CloudflareImagesListImagesResponse:
        """List up to 100 images with one request.

        Use the optional parameters below to get
        a specific range of images.

        Args:
          account_id: Account identifier tag.

          page: Page number of paginated results.

          per_page: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/images/v1",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    v1_cloudflare_images_list_images_params.V1CloudflareImagesListImagesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[V1CloudflareImagesListImagesResponse], ResultWrapper[V1CloudflareImagesListImagesResponse]
            ),
        )

    @overload
    def cloudflare_images_upload_an_image_via_url(
        self,
        account_id: str,
        *,
        file: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1CloudflareImagesUploadAnImageViaURLResponse:
        """
        Upload an image with up to 10 Megabytes using a single HTTP POST
        (multipart/form-data) request. An image can be uploaded by sending an image file
        or passing an accessible to an API url.

        Args:
          account_id: Account identifier tag.

          file: An image binary data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def cloudflare_images_upload_an_image_via_url(
        self,
        account_id: str,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1CloudflareImagesUploadAnImageViaURLResponse:
        """
        Upload an image with up to 10 Megabytes using a single HTTP POST
        (multipart/form-data) request. An image can be uploaded by sending an image file
        or passing an accessible to an API url.

        Args:
          account_id: Account identifier tag.

          url: A URL to fetch an image from origin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["file"], ["url"])
    def cloudflare_images_upload_an_image_via_url(
        self,
        account_id: str,
        *,
        file: object | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1CloudflareImagesUploadAnImageViaURLResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/images/v1",
            body=maybe_transform(
                {
                    "file": file,
                    "url": url,
                },
                v1_cloudflare_images_upload_an_image_via_url_params.V1CloudflareImagesUploadAnImageViaURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[V1CloudflareImagesUploadAnImageViaURLResponse],
                ResultWrapper[V1CloudflareImagesUploadAnImageViaURLResponse],
            ),
        )

    def get(
        self,
        image_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1GetResponse:
        """
        Fetch details for a single image.

        Args:
          account_id: Account identifier tag.

          image_id: Image unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return self._get(
            f"/accounts/{account_id}/images/v1/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[V1GetResponse], ResultWrapper[V1GetResponse]),
        )


class AsyncV1s(AsyncAPIResource):
    @cached_property
    def keys(self) -> AsyncKeys:
        return AsyncKeys(self._client)

    @cached_property
    def stats(self) -> AsyncStats:
        return AsyncStats(self._client)

    @cached_property
    def variants(self) -> AsyncVariants:
        return AsyncVariants(self._client)

    @cached_property
    def blobs(self) -> AsyncBlobs:
        return AsyncBlobs(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1sWithRawResponse:
        return AsyncV1sWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1sWithStreamingResponse:
        return AsyncV1sWithStreamingResponse(self)

    async def update(
        self,
        image_id: str,
        *,
        account_id: str,
        metadata: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1UpdateResponse:
        """Update image access control.

        On access control change, all copies of the image
        are purged from cache.

        Args:
          account_id: Account identifier tag.

          image_id: Image unique identifier.

          metadata: User modifiable key-value store. Can be used for keeping references to another
              system of record for managing images. No change if not specified.

          require_signed_urls: Indicates whether the image can be accessed using only its UID. If set to
              `true`, a signed token needs to be generated with a signing key to view the
              image. Returns a new UID on a change. No change if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/images/v1/{image_id}",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "require_signed_urls": require_signed_urls,
                },
                v1_update_params.V1UpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[V1UpdateResponse], ResultWrapper[V1UpdateResponse]),
        )

    async def delete(
        self,
        image_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1DeleteResponse:
        """Delete an image on Cloudflare Images.

        On success, all copies of the image are
        deleted and purged from cache.

        Args:
          account_id: Account identifier tag.

          image_id: Image unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return cast(
            V1DeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/images/v1/{image_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[V1DeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def cloudflare_images_list_images(
        self,
        account_id: str,
        *,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1CloudflareImagesListImagesResponse:
        """List up to 100 images with one request.

        Use the optional parameters below to get
        a specific range of images.

        Args:
          account_id: Account identifier tag.

          page: Page number of paginated results.

          per_page: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/images/v1",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    v1_cloudflare_images_list_images_params.V1CloudflareImagesListImagesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[V1CloudflareImagesListImagesResponse], ResultWrapper[V1CloudflareImagesListImagesResponse]
            ),
        )

    @overload
    async def cloudflare_images_upload_an_image_via_url(
        self,
        account_id: str,
        *,
        file: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1CloudflareImagesUploadAnImageViaURLResponse:
        """
        Upload an image with up to 10 Megabytes using a single HTTP POST
        (multipart/form-data) request. An image can be uploaded by sending an image file
        or passing an accessible to an API url.

        Args:
          account_id: Account identifier tag.

          file: An image binary data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def cloudflare_images_upload_an_image_via_url(
        self,
        account_id: str,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1CloudflareImagesUploadAnImageViaURLResponse:
        """
        Upload an image with up to 10 Megabytes using a single HTTP POST
        (multipart/form-data) request. An image can be uploaded by sending an image file
        or passing an accessible to an API url.

        Args:
          account_id: Account identifier tag.

          url: A URL to fetch an image from origin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["file"], ["url"])
    async def cloudflare_images_upload_an_image_via_url(
        self,
        account_id: str,
        *,
        file: object | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1CloudflareImagesUploadAnImageViaURLResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/images/v1",
            body=maybe_transform(
                {
                    "file": file,
                    "url": url,
                },
                v1_cloudflare_images_upload_an_image_via_url_params.V1CloudflareImagesUploadAnImageViaURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[V1CloudflareImagesUploadAnImageViaURLResponse],
                ResultWrapper[V1CloudflareImagesUploadAnImageViaURLResponse],
            ),
        )

    async def get(
        self,
        image_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1GetResponse:
        """
        Fetch details for a single image.

        Args:
          account_id: Account identifier tag.

          image_id: Image unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return await self._get(
            f"/accounts/{account_id}/images/v1/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[V1GetResponse], ResultWrapper[V1GetResponse]),
        )


class V1sWithRawResponse:
    def __init__(self, v1s: V1s) -> None:
        self._v1s = v1s

        self.update = to_raw_response_wrapper(
            v1s.update,
        )
        self.delete = to_raw_response_wrapper(
            v1s.delete,
        )
        self.cloudflare_images_list_images = to_raw_response_wrapper(
            v1s.cloudflare_images_list_images,
        )
        self.cloudflare_images_upload_an_image_via_url = to_raw_response_wrapper(
            v1s.cloudflare_images_upload_an_image_via_url,
        )
        self.get = to_raw_response_wrapper(
            v1s.get,
        )

    @cached_property
    def keys(self) -> KeysWithRawResponse:
        return KeysWithRawResponse(self._v1s.keys)

    @cached_property
    def stats(self) -> StatsWithRawResponse:
        return StatsWithRawResponse(self._v1s.stats)

    @cached_property
    def variants(self) -> VariantsWithRawResponse:
        return VariantsWithRawResponse(self._v1s.variants)

    @cached_property
    def blobs(self) -> BlobsWithRawResponse:
        return BlobsWithRawResponse(self._v1s.blobs)


class AsyncV1sWithRawResponse:
    def __init__(self, v1s: AsyncV1s) -> None:
        self._v1s = v1s

        self.update = async_to_raw_response_wrapper(
            v1s.update,
        )
        self.delete = async_to_raw_response_wrapper(
            v1s.delete,
        )
        self.cloudflare_images_list_images = async_to_raw_response_wrapper(
            v1s.cloudflare_images_list_images,
        )
        self.cloudflare_images_upload_an_image_via_url = async_to_raw_response_wrapper(
            v1s.cloudflare_images_upload_an_image_via_url,
        )
        self.get = async_to_raw_response_wrapper(
            v1s.get,
        )

    @cached_property
    def keys(self) -> AsyncKeysWithRawResponse:
        return AsyncKeysWithRawResponse(self._v1s.keys)

    @cached_property
    def stats(self) -> AsyncStatsWithRawResponse:
        return AsyncStatsWithRawResponse(self._v1s.stats)

    @cached_property
    def variants(self) -> AsyncVariantsWithRawResponse:
        return AsyncVariantsWithRawResponse(self._v1s.variants)

    @cached_property
    def blobs(self) -> AsyncBlobsWithRawResponse:
        return AsyncBlobsWithRawResponse(self._v1s.blobs)


class V1sWithStreamingResponse:
    def __init__(self, v1s: V1s) -> None:
        self._v1s = v1s

        self.update = to_streamed_response_wrapper(
            v1s.update,
        )
        self.delete = to_streamed_response_wrapper(
            v1s.delete,
        )
        self.cloudflare_images_list_images = to_streamed_response_wrapper(
            v1s.cloudflare_images_list_images,
        )
        self.cloudflare_images_upload_an_image_via_url = to_streamed_response_wrapper(
            v1s.cloudflare_images_upload_an_image_via_url,
        )
        self.get = to_streamed_response_wrapper(
            v1s.get,
        )

    @cached_property
    def keys(self) -> KeysWithStreamingResponse:
        return KeysWithStreamingResponse(self._v1s.keys)

    @cached_property
    def stats(self) -> StatsWithStreamingResponse:
        return StatsWithStreamingResponse(self._v1s.stats)

    @cached_property
    def variants(self) -> VariantsWithStreamingResponse:
        return VariantsWithStreamingResponse(self._v1s.variants)

    @cached_property
    def blobs(self) -> BlobsWithStreamingResponse:
        return BlobsWithStreamingResponse(self._v1s.blobs)


class AsyncV1sWithStreamingResponse:
    def __init__(self, v1s: AsyncV1s) -> None:
        self._v1s = v1s

        self.update = async_to_streamed_response_wrapper(
            v1s.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            v1s.delete,
        )
        self.cloudflare_images_list_images = async_to_streamed_response_wrapper(
            v1s.cloudflare_images_list_images,
        )
        self.cloudflare_images_upload_an_image_via_url = async_to_streamed_response_wrapper(
            v1s.cloudflare_images_upload_an_image_via_url,
        )
        self.get = async_to_streamed_response_wrapper(
            v1s.get,
        )

    @cached_property
    def keys(self) -> AsyncKeysWithStreamingResponse:
        return AsyncKeysWithStreamingResponse(self._v1s.keys)

    @cached_property
    def stats(self) -> AsyncStatsWithStreamingResponse:
        return AsyncStatsWithStreamingResponse(self._v1s.stats)

    @cached_property
    def variants(self) -> AsyncVariantsWithStreamingResponse:
        return AsyncVariantsWithStreamingResponse(self._v1s.variants)

    @cached_property
    def blobs(self) -> AsyncBlobsWithStreamingResponse:
        return AsyncBlobsWithStreamingResponse(self._v1s.blobs)
