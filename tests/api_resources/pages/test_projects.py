# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.pages import (
    Project,
    Deployment,
    ProjectEditResponse,
    ProjectCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        project = client.pages.projects.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        project = client.pages.projects.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            build_config={
                "build_caching": True,
                "build_command": "npm run build",
                "destination_dir": "build",
                "root_dir": "/",
                "web_analytics_tag": "cee1c73f6e4743d0b5e6bb1a0bcaabcc",
                "web_analytics_token": "021e1057c18547eca7b79f2516f06o7x",
            },
            canonical_deployment={},
            deployment_configs={
                "preview": {
                    "ai_bindings": {"ai_binding": {"project_id": {}}},
                    "analytics_engine_datasets": {"analytics_engine_binding": {"dataset": "api_analytics"}},
                    "browsers": {"browser": {}},
                    "compatibility_date": "2022-01-01",
                    "compatibility_flags": ["url_standard"],
                    "d1_databases": {"d1_binding": {"id": "445e2955-951a-43f8-a35b-a4d0c8138f63"}},
                    "durable_object_namespaces": {"do_binding": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "env_vars": {
                        "environment_variable": {
                            "type": "plain_text",
                            "value": "hello world",
                        }
                    },
                    "hyperdrive_bindings": {"hyperdrive": {"id": "a76a99bc342644deb02c38d66082262a"}},
                    "kv_namespaces": {"kv_binding": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "mtls_certificates": {"mtls": {"certificate_id": "d7cdd17c-916f-4cb7-aabe-585eb382ec4e"}},
                    "placement": {"mode": "smart"},
                    "queue_producers": {"queue_producer_binding": {"name": "some-queue"}},
                    "r2_buckets": {"r2_binding": {"name": "some-bucket"}},
                    "services": {
                        "service_binding": {
                            "entrypoint": "MyHandler",
                            "environment": "production",
                            "service": "example-worker",
                        }
                    },
                    "vectorize_bindings": {"vectorize": {"index_name": "my_index"}},
                },
                "production": {
                    "ai_bindings": {"ai_binding": {"project_id": {}}},
                    "analytics_engine_datasets": {"analytics_engine_binding": {"dataset": "api_analytics"}},
                    "browsers": {"browser": {}},
                    "compatibility_date": "2022-01-01",
                    "compatibility_flags": ["url_standard"],
                    "d1_databases": {"d1_binding": {"id": "445e2955-951a-43f8-a35b-a4d0c8138f63"}},
                    "durable_object_namespaces": {"do_binding": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "env_vars": {
                        "environment_variable": {
                            "type": "plain_text",
                            "value": "hello world",
                        }
                    },
                    "hyperdrive_bindings": {"hyperdrive": {"id": "a76a99bc342644deb02c38d66082262a"}},
                    "kv_namespaces": {"kv_binding": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "mtls_certificates": {"mtls": {"certificate_id": "d7cdd17c-916f-4cb7-aabe-585eb382ec4e"}},
                    "placement": {"mode": "smart"},
                    "queue_producers": {"queue_producer_binding": {"name": "some-queue"}},
                    "r2_buckets": {"r2_binding": {"name": "some-bucket"}},
                    "services": {
                        "service_binding": {
                            "entrypoint": "MyHandler",
                            "environment": "production",
                            "service": "example-worker",
                        }
                    },
                    "vectorize_bindings": {"vectorize": {"index_name": "my_index"}},
                },
            },
            latest_deployment={},
            name="NextJS Blog",
            production_branch="main",
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.pages.projects.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.pages.projects.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.with_raw_response.create(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        project = client.pages.projects.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[Deployment], project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.pages.projects.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(SyncSinglePage[Deployment], project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.pages.projects.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(SyncSinglePage[Deployment], project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        project = client.pages.projects.delete(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.pages.projects.with_raw_response.delete(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(object, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.pages.projects.with_streaming_response.delete(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(object, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.with_raw_response.delete(
                "this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        project = client.pages.projects.edit(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "deployment_configs": {
                    "production": {
                        "compatibility_date": "2022-01-01",
                        "compatibility_flags": ["url_standard"],
                        "env_vars": {
                            "BUILD_VERSION": {"value": "3.3"},
                            "delete_this_env_var": None,
                            "secret_var": {
                                "type": "secret_text",
                                "value": "A_CMS_API_TOKEN",
                            },
                        },
                    }
                }
            },
        )
        assert_matches_type(ProjectEditResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.pages.projects.with_raw_response.edit(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "deployment_configs": {
                    "production": {
                        "compatibility_date": "2022-01-01",
                        "compatibility_flags": ["url_standard"],
                        "env_vars": {
                            "BUILD_VERSION": {"value": "3.3"},
                            "delete_this_env_var": None,
                            "secret_var": {
                                "type": "secret_text",
                                "value": "A_CMS_API_TOKEN",
                            },
                        },
                    }
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectEditResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.pages.projects.with_streaming_response.edit(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "deployment_configs": {
                    "production": {
                        "compatibility_date": "2022-01-01",
                        "compatibility_flags": ["url_standard"],
                        "env_vars": {
                            "BUILD_VERSION": {"value": "3.3"},
                            "delete_this_env_var": None,
                            "secret_var": {
                                "type": "secret_text",
                                "value": "A_CMS_API_TOKEN",
                            },
                        },
                    }
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectEditResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.with_raw_response.edit(
                "this-is-my-project-01",
                account_id="",
                body={
                    "deployment_configs": {
                        "production": {
                            "compatibility_date": "2022-01-01",
                            "compatibility_flags": ["url_standard"],
                            "env_vars": {
                                "BUILD_VERSION": {"value": "3.3"},
                                "delete_this_env_var": None,
                                "secret_var": {
                                    "type": "secret_text",
                                    "value": "A_CMS_API_TOKEN",
                                },
                            },
                        }
                    }
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.with_raw_response.edit(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={
                    "deployment_configs": {
                        "production": {
                            "compatibility_date": "2022-01-01",
                            "compatibility_flags": ["url_standard"],
                            "env_vars": {
                                "BUILD_VERSION": {"value": "3.3"},
                                "delete_this_env_var": None,
                                "secret_var": {
                                    "type": "secret_text",
                                    "value": "A_CMS_API_TOKEN",
                                },
                            },
                        }
                    }
                },
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        project = client.pages.projects.get(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.pages.projects.with_raw_response.get(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.pages.projects.with_streaming_response.get(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.with_raw_response.get(
                "this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_purge_build_cache(self, client: Cloudflare) -> None:
        project = client.pages.projects.purge_build_cache(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_purge_build_cache(self, client: Cloudflare) -> None:
        response = client.pages.projects.with_raw_response.purge_build_cache(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(object, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_purge_build_cache(self, client: Cloudflare) -> None:
        with client.pages.projects.with_streaming_response.purge_build_cache(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(object, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_purge_build_cache(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.with_raw_response.purge_build_cache(
                "this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.with_raw_response.purge_build_cache(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncProjects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        project = await async_client.pages.projects.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        project = await async_client.pages.projects.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            build_config={
                "build_caching": True,
                "build_command": "npm run build",
                "destination_dir": "build",
                "root_dir": "/",
                "web_analytics_tag": "cee1c73f6e4743d0b5e6bb1a0bcaabcc",
                "web_analytics_token": "021e1057c18547eca7b79f2516f06o7x",
            },
            canonical_deployment={},
            deployment_configs={
                "preview": {
                    "ai_bindings": {"ai_binding": {"project_id": {}}},
                    "analytics_engine_datasets": {"analytics_engine_binding": {"dataset": "api_analytics"}},
                    "browsers": {"browser": {}},
                    "compatibility_date": "2022-01-01",
                    "compatibility_flags": ["url_standard"],
                    "d1_databases": {"d1_binding": {"id": "445e2955-951a-43f8-a35b-a4d0c8138f63"}},
                    "durable_object_namespaces": {"do_binding": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "env_vars": {
                        "environment_variable": {
                            "type": "plain_text",
                            "value": "hello world",
                        }
                    },
                    "hyperdrive_bindings": {"hyperdrive": {"id": "a76a99bc342644deb02c38d66082262a"}},
                    "kv_namespaces": {"kv_binding": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "mtls_certificates": {"mtls": {"certificate_id": "d7cdd17c-916f-4cb7-aabe-585eb382ec4e"}},
                    "placement": {"mode": "smart"},
                    "queue_producers": {"queue_producer_binding": {"name": "some-queue"}},
                    "r2_buckets": {"r2_binding": {"name": "some-bucket"}},
                    "services": {
                        "service_binding": {
                            "entrypoint": "MyHandler",
                            "environment": "production",
                            "service": "example-worker",
                        }
                    },
                    "vectorize_bindings": {"vectorize": {"index_name": "my_index"}},
                },
                "production": {
                    "ai_bindings": {"ai_binding": {"project_id": {}}},
                    "analytics_engine_datasets": {"analytics_engine_binding": {"dataset": "api_analytics"}},
                    "browsers": {"browser": {}},
                    "compatibility_date": "2022-01-01",
                    "compatibility_flags": ["url_standard"],
                    "d1_databases": {"d1_binding": {"id": "445e2955-951a-43f8-a35b-a4d0c8138f63"}},
                    "durable_object_namespaces": {"do_binding": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "env_vars": {
                        "environment_variable": {
                            "type": "plain_text",
                            "value": "hello world",
                        }
                    },
                    "hyperdrive_bindings": {"hyperdrive": {"id": "a76a99bc342644deb02c38d66082262a"}},
                    "kv_namespaces": {"kv_binding": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "mtls_certificates": {"mtls": {"certificate_id": "d7cdd17c-916f-4cb7-aabe-585eb382ec4e"}},
                    "placement": {"mode": "smart"},
                    "queue_producers": {"queue_producer_binding": {"name": "some-queue"}},
                    "r2_buckets": {"r2_binding": {"name": "some-bucket"}},
                    "services": {
                        "service_binding": {
                            "entrypoint": "MyHandler",
                            "environment": "production",
                            "service": "example-worker",
                        }
                    },
                    "vectorize_bindings": {"vectorize": {"index_name": "my_index"}},
                },
            },
            latest_deployment={},
            name="NextJS Blog",
            production_branch="main",
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.with_raw_response.create(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        project = await async_client.pages.projects.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[Deployment], project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(AsyncSinglePage[Deployment], project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(AsyncSinglePage[Deployment], project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        project = await async_client.pages.projects.delete(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.with_raw_response.delete(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(object, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.with_streaming_response.delete(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(object, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.with_raw_response.delete(
                "this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        project = await async_client.pages.projects.edit(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "deployment_configs": {
                    "production": {
                        "compatibility_date": "2022-01-01",
                        "compatibility_flags": ["url_standard"],
                        "env_vars": {
                            "BUILD_VERSION": {"value": "3.3"},
                            "delete_this_env_var": None,
                            "secret_var": {
                                "type": "secret_text",
                                "value": "A_CMS_API_TOKEN",
                            },
                        },
                    }
                }
            },
        )
        assert_matches_type(ProjectEditResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.with_raw_response.edit(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "deployment_configs": {
                    "production": {
                        "compatibility_date": "2022-01-01",
                        "compatibility_flags": ["url_standard"],
                        "env_vars": {
                            "BUILD_VERSION": {"value": "3.3"},
                            "delete_this_env_var": None,
                            "secret_var": {
                                "type": "secret_text",
                                "value": "A_CMS_API_TOKEN",
                            },
                        },
                    }
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectEditResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.with_streaming_response.edit(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "deployment_configs": {
                    "production": {
                        "compatibility_date": "2022-01-01",
                        "compatibility_flags": ["url_standard"],
                        "env_vars": {
                            "BUILD_VERSION": {"value": "3.3"},
                            "delete_this_env_var": None,
                            "secret_var": {
                                "type": "secret_text",
                                "value": "A_CMS_API_TOKEN",
                            },
                        },
                    }
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectEditResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.with_raw_response.edit(
                "this-is-my-project-01",
                account_id="",
                body={
                    "deployment_configs": {
                        "production": {
                            "compatibility_date": "2022-01-01",
                            "compatibility_flags": ["url_standard"],
                            "env_vars": {
                                "BUILD_VERSION": {"value": "3.3"},
                                "delete_this_env_var": None,
                                "secret_var": {
                                    "type": "secret_text",
                                    "value": "A_CMS_API_TOKEN",
                                },
                            },
                        }
                    }
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.with_raw_response.edit(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={
                    "deployment_configs": {
                        "production": {
                            "compatibility_date": "2022-01-01",
                            "compatibility_flags": ["url_standard"],
                            "env_vars": {
                                "BUILD_VERSION": {"value": "3.3"},
                                "delete_this_env_var": None,
                                "secret_var": {
                                    "type": "secret_text",
                                    "value": "A_CMS_API_TOKEN",
                                },
                            },
                        }
                    }
                },
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        project = await async_client.pages.projects.get(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.with_raw_response.get(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.with_streaming_response.get(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.with_raw_response.get(
                "this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_purge_build_cache(self, async_client: AsyncCloudflare) -> None:
        project = await async_client.pages.projects.purge_build_cache(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_purge_build_cache(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.with_raw_response.purge_build_cache(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(object, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_purge_build_cache(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.with_streaming_response.purge_build_cache(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(object, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_purge_build_cache(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.with_raw_response.purge_build_cache(
                "this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.with_raw_response.purge_build_cache(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
