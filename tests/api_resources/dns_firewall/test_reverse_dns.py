# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.dns_firewall import ReverseDNSGetResponse, ReverseDNSEditResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReverseDNS:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        reverse_dns = client.dns_firewall.reverse_dns.edit(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ReverseDNSEditResponse], reverse_dns, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        reverse_dns = client.dns_firewall.reverse_dns.edit(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ptr={"foo": "string"},
        )
        assert_matches_type(Optional[ReverseDNSEditResponse], reverse_dns, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.dns_firewall.reverse_dns.with_raw_response.edit(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reverse_dns = response.parse()
        assert_matches_type(Optional[ReverseDNSEditResponse], reverse_dns, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.dns_firewall.reverse_dns.with_streaming_response.edit(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reverse_dns = response.parse()
            assert_matches_type(Optional[ReverseDNSEditResponse], reverse_dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns_firewall.reverse_dns.with_raw_response.edit(
                dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            client.dns_firewall.reverse_dns.with_raw_response.edit(
                dns_firewall_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        reverse_dns = client.dns_firewall.reverse_dns.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ReverseDNSGetResponse], reverse_dns, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dns_firewall.reverse_dns.with_raw_response.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reverse_dns = response.parse()
        assert_matches_type(Optional[ReverseDNSGetResponse], reverse_dns, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dns_firewall.reverse_dns.with_streaming_response.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reverse_dns = response.parse()
            assert_matches_type(Optional[ReverseDNSGetResponse], reverse_dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns_firewall.reverse_dns.with_raw_response.get(
                dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            client.dns_firewall.reverse_dns.with_raw_response.get(
                dns_firewall_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncReverseDNS:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        reverse_dns = await async_client.dns_firewall.reverse_dns.edit(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ReverseDNSEditResponse], reverse_dns, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        reverse_dns = await async_client.dns_firewall.reverse_dns.edit(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ptr={"foo": "string"},
        )
        assert_matches_type(Optional[ReverseDNSEditResponse], reverse_dns, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_firewall.reverse_dns.with_raw_response.edit(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reverse_dns = await response.parse()
        assert_matches_type(Optional[ReverseDNSEditResponse], reverse_dns, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_firewall.reverse_dns.with_streaming_response.edit(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reverse_dns = await response.parse()
            assert_matches_type(Optional[ReverseDNSEditResponse], reverse_dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns_firewall.reverse_dns.with_raw_response.edit(
                dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            await async_client.dns_firewall.reverse_dns.with_raw_response.edit(
                dns_firewall_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        reverse_dns = await async_client.dns_firewall.reverse_dns.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ReverseDNSGetResponse], reverse_dns, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_firewall.reverse_dns.with_raw_response.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reverse_dns = await response.parse()
        assert_matches_type(Optional[ReverseDNSGetResponse], reverse_dns, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_firewall.reverse_dns.with_streaming_response.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reverse_dns = await response.parse()
            assert_matches_type(Optional[ReverseDNSGetResponse], reverse_dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns_firewall.reverse_dns.with_raw_response.get(
                dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            await async_client.dns_firewall.reverse_dns.with_raw_response.get(
                dns_firewall_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
