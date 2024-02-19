# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from maisa import Maisa, AsyncMaisa
from maisa.types import ModelRerankResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_rerank(self, client: Maisa) -> None:
        model = client.models.rerank(
            sentences=["The light bulb was invented by Thomas Edison", "It's a nice day, isn't it"],
            source_sentence="Who invented the light bulb?",
        )
        assert_matches_type(ModelRerankResponse, model, path=["response"])

    @parametrize
    def test_raw_response_rerank(self, client: Maisa) -> None:
        response = client.models.with_raw_response.rerank(
            sentences=["The light bulb was invented by Thomas Edison", "It's a nice day, isn't it"],
            source_sentence="Who invented the light bulb?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelRerankResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_rerank(self, client: Maisa) -> None:
        with client.models.with_streaming_response.rerank(
            sentences=["The light bulb was invented by Thomas Edison", "It's a nice day, isn't it"],
            source_sentence="Who invented the light bulb?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelRerankResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_rerank(self, async_client: AsyncMaisa) -> None:
        model = await async_client.models.rerank(
            sentences=["The light bulb was invented by Thomas Edison", "It's a nice day, isn't it"],
            source_sentence="Who invented the light bulb?",
        )
        assert_matches_type(ModelRerankResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_rerank(self, async_client: AsyncMaisa) -> None:
        response = await async_client.models.with_raw_response.rerank(
            sentences=["The light bulb was invented by Thomas Edison", "It's a nice day, isn't it"],
            source_sentence="Who invented the light bulb?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelRerankResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_rerank(self, async_client: AsyncMaisa) -> None:
        async with async_client.models.with_streaming_response.rerank(
            sentences=["The light bulb was invented by Thomas Edison", "It's a nice day, isn't it"],
            source_sentence="Who invented the light bulb?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelRerankResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True
