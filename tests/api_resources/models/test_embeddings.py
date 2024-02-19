# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from maisa import Maisa, AsyncMaisa
from tests.utils import assert_matches_type
from maisa.types.models import Embeddings

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmbeddings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Maisa) -> None:
        embedding = client.models.embeddings.create(
            texts=["string"],
        )
        assert_matches_type(Embeddings, embedding, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Maisa) -> None:
        response = client.models.embeddings.with_raw_response.create(
            texts=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = response.parse()
        assert_matches_type(Embeddings, embedding, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Maisa) -> None:
        with client.models.embeddings.with_streaming_response.create(
            texts=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = response.parse()
            assert_matches_type(Embeddings, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmbeddings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMaisa) -> None:
        embedding = await async_client.models.embeddings.create(
            texts=["string"],
        )
        assert_matches_type(Embeddings, embedding, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMaisa) -> None:
        response = await async_client.models.embeddings.with_raw_response.create(
            texts=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = await response.parse()
        assert_matches_type(Embeddings, embedding, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMaisa) -> None:
        async with async_client.models.embeddings.with_streaming_response.create(
            texts=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = await response.parse()
            assert_matches_type(Embeddings, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True
