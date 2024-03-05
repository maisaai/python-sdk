# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from maisa import Maisa, AsyncMaisa
from maisa.types import KpuRunResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKpu:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_run(self, client: Maisa) -> None:
        kpu = client.kpu.run(
            query="string",
        )
        assert_matches_type(KpuRunResponse, kpu, path=["response"])

    @parametrize
    def test_method_run_with_all_params(self, client: Maisa) -> None:
        kpu = client.kpu.run(
            query="string",
            explain_steps=True,
            retries=1,
            file=[b"raw file contents", b"raw file contents", b"raw file contents"],
        )
        assert_matches_type(KpuRunResponse, kpu, path=["response"])

    @parametrize
    def test_raw_response_run(self, client: Maisa) -> None:
        response = client.kpu.with_raw_response.run(
            query="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kpu = response.parse()
        assert_matches_type(KpuRunResponse, kpu, path=["response"])

    @parametrize
    def test_streaming_response_run(self, client: Maisa) -> None:
        with client.kpu.with_streaming_response.run(
            query="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kpu = response.parse()
            assert_matches_type(KpuRunResponse, kpu, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKpu:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_run(self, async_client: AsyncMaisa) -> None:
        kpu = await async_client.kpu.run(
            query="string",
        )
        assert_matches_type(KpuRunResponse, kpu, path=["response"])

    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncMaisa) -> None:
        kpu = await async_client.kpu.run(
            query="string",
            explain_steps=True,
            retries=1,
            file=[b"raw file contents", b"raw file contents", b"raw file contents"],
        )
        assert_matches_type(KpuRunResponse, kpu, path=["response"])

    @parametrize
    async def test_raw_response_run(self, async_client: AsyncMaisa) -> None:
        response = await async_client.kpu.with_raw_response.run(
            query="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kpu = await response.parse()
        assert_matches_type(KpuRunResponse, kpu, path=["response"])

    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncMaisa) -> None:
        async with async_client.kpu.with_streaming_response.run(
            query="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kpu = await response.parse()
            assert_matches_type(KpuRunResponse, kpu, path=["response"])

        assert cast(Any, response.is_closed) is True
