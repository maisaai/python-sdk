# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from maisa import Maisa, AsyncMaisa
from tests.utils import assert_matches_type
from maisa.types.mainet import Search

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Maisa) -> None:
        search = client.mainet.search.create(
            text="Plato, the philosopher, was born in Athens.",
        )
        assert_matches_type(Search, search, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Maisa) -> None:
        response = client.mainet.search.with_raw_response.create(
            text="Plato, the philosopher, was born in Athens.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(Search, search, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Maisa) -> None:
        with client.mainet.search.with_streaming_response.create(
            text="Plato, the philosopher, was born in Athens.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(Search, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMaisa) -> None:
        search = await async_client.mainet.search.create(
            text="Plato, the philosopher, was born in Athens.",
        )
        assert_matches_type(Search, search, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMaisa) -> None:
        response = await async_client.mainet.search.with_raw_response.create(
            text="Plato, the philosopher, was born in Athens.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(Search, search, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMaisa) -> None:
        async with async_client.mainet.search.with_streaming_response.create(
            text="Plato, the philosopher, was born in Athens.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(Search, search, path=["response"])

        assert cast(Any, response.is_closed) is True
