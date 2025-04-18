# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.leaked_credential_checks import (
    DetectionListResponse,
    DetectionCreateResponse,
    DetectionUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDetections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        detection = client.leaked_credential_checks.detections.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DetectionCreateResponse, detection, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        detection = client.leaked_credential_checks.detections.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            password='lookup_json_string(http.request.body.raw, "secret")',
            username='lookup_json_string(http.request.body.raw, "user")',
        )
        assert_matches_type(DetectionCreateResponse, detection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.leaked_credential_checks.detections.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detection = response.parse()
        assert_matches_type(DetectionCreateResponse, detection, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.leaked_credential_checks.detections.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detection = response.parse()
            assert_matches_type(DetectionCreateResponse, detection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.leaked_credential_checks.detections.with_raw_response.create(
                zone_id="",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        detection = client.leaked_credential_checks.detections.update(
            detection_id="18a14bafaa8eb1df04ce683ec18c765e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DetectionUpdateResponse, detection, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        detection = client.leaked_credential_checks.detections.update(
            detection_id="18a14bafaa8eb1df04ce683ec18c765e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            password='lookup_json_string(http.request.body.raw, "secret")',
            username='lookup_json_string(http.request.body.raw, "user")',
        )
        assert_matches_type(DetectionUpdateResponse, detection, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.leaked_credential_checks.detections.with_raw_response.update(
            detection_id="18a14bafaa8eb1df04ce683ec18c765e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detection = response.parse()
        assert_matches_type(DetectionUpdateResponse, detection, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.leaked_credential_checks.detections.with_streaming_response.update(
            detection_id="18a14bafaa8eb1df04ce683ec18c765e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detection = response.parse()
            assert_matches_type(DetectionUpdateResponse, detection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.leaked_credential_checks.detections.with_raw_response.update(
                detection_id="18a14bafaa8eb1df04ce683ec18c765e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `detection_id` but received ''"):
            client.leaked_credential_checks.detections.with_raw_response.update(
                detection_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        detection = client.leaked_credential_checks.detections.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[DetectionListResponse], detection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.leaked_credential_checks.detections.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detection = response.parse()
        assert_matches_type(SyncSinglePage[DetectionListResponse], detection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.leaked_credential_checks.detections.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detection = response.parse()
            assert_matches_type(SyncSinglePage[DetectionListResponse], detection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.leaked_credential_checks.detections.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        detection = client.leaked_credential_checks.detections.delete(
            detection_id="18a14bafaa8eb1df04ce683ec18c765e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, detection, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.leaked_credential_checks.detections.with_raw_response.delete(
            detection_id="18a14bafaa8eb1df04ce683ec18c765e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detection = response.parse()
        assert_matches_type(object, detection, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.leaked_credential_checks.detections.with_streaming_response.delete(
            detection_id="18a14bafaa8eb1df04ce683ec18c765e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detection = response.parse()
            assert_matches_type(object, detection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.leaked_credential_checks.detections.with_raw_response.delete(
                detection_id="18a14bafaa8eb1df04ce683ec18c765e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `detection_id` but received ''"):
            client.leaked_credential_checks.detections.with_raw_response.delete(
                detection_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncDetections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        detection = await async_client.leaked_credential_checks.detections.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DetectionCreateResponse, detection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        detection = await async_client.leaked_credential_checks.detections.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            password='lookup_json_string(http.request.body.raw, "secret")',
            username='lookup_json_string(http.request.body.raw, "user")',
        )
        assert_matches_type(DetectionCreateResponse, detection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.leaked_credential_checks.detections.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detection = await response.parse()
        assert_matches_type(DetectionCreateResponse, detection, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.leaked_credential_checks.detections.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detection = await response.parse()
            assert_matches_type(DetectionCreateResponse, detection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.leaked_credential_checks.detections.with_raw_response.create(
                zone_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        detection = await async_client.leaked_credential_checks.detections.update(
            detection_id="18a14bafaa8eb1df04ce683ec18c765e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DetectionUpdateResponse, detection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        detection = await async_client.leaked_credential_checks.detections.update(
            detection_id="18a14bafaa8eb1df04ce683ec18c765e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            password='lookup_json_string(http.request.body.raw, "secret")',
            username='lookup_json_string(http.request.body.raw, "user")',
        )
        assert_matches_type(DetectionUpdateResponse, detection, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.leaked_credential_checks.detections.with_raw_response.update(
            detection_id="18a14bafaa8eb1df04ce683ec18c765e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detection = await response.parse()
        assert_matches_type(DetectionUpdateResponse, detection, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.leaked_credential_checks.detections.with_streaming_response.update(
            detection_id="18a14bafaa8eb1df04ce683ec18c765e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detection = await response.parse()
            assert_matches_type(DetectionUpdateResponse, detection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.leaked_credential_checks.detections.with_raw_response.update(
                detection_id="18a14bafaa8eb1df04ce683ec18c765e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `detection_id` but received ''"):
            await async_client.leaked_credential_checks.detections.with_raw_response.update(
                detection_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        detection = await async_client.leaked_credential_checks.detections.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[DetectionListResponse], detection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.leaked_credential_checks.detections.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detection = await response.parse()
        assert_matches_type(AsyncSinglePage[DetectionListResponse], detection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.leaked_credential_checks.detections.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detection = await response.parse()
            assert_matches_type(AsyncSinglePage[DetectionListResponse], detection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.leaked_credential_checks.detections.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        detection = await async_client.leaked_credential_checks.detections.delete(
            detection_id="18a14bafaa8eb1df04ce683ec18c765e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, detection, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.leaked_credential_checks.detections.with_raw_response.delete(
            detection_id="18a14bafaa8eb1df04ce683ec18c765e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detection = await response.parse()
        assert_matches_type(object, detection, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.leaked_credential_checks.detections.with_streaming_response.delete(
            detection_id="18a14bafaa8eb1df04ce683ec18c765e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detection = await response.parse()
            assert_matches_type(object, detection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.leaked_credential_checks.detections.with_raw_response.delete(
                detection_id="18a14bafaa8eb1df04ce683ec18c765e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `detection_id` but received ''"):
            await async_client.leaked_credential_checks.detections.with_raw_response.delete(
                detection_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
