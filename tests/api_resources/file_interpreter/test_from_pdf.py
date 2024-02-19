# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from maisa import Maisa, AsyncMaisa
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFromPdf:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Maisa) -> None:
        from_pdf = client.file_interpreter.from_pdf.create(
            file=b"raw file contents",
        )
        assert_matches_type(object, from_pdf, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Maisa) -> None:
        from_pdf = client.file_interpreter.from_pdf.create(
            file=b"raw file contents",
            max_pages=0,
        )
        assert_matches_type(object, from_pdf, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Maisa) -> None:
        response = client.file_interpreter.from_pdf.with_raw_response.create(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        from_pdf = response.parse()
        assert_matches_type(object, from_pdf, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Maisa) -> None:
        with client.file_interpreter.from_pdf.with_streaming_response.create(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            from_pdf = response.parse()
            assert_matches_type(object, from_pdf, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFromPdf:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMaisa) -> None:
        from_pdf = await async_client.file_interpreter.from_pdf.create(
            file=b"raw file contents",
        )
        assert_matches_type(object, from_pdf, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMaisa) -> None:
        from_pdf = await async_client.file_interpreter.from_pdf.create(
            file=b"raw file contents",
            max_pages=0,
        )
        assert_matches_type(object, from_pdf, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMaisa) -> None:
        response = await async_client.file_interpreter.from_pdf.with_raw_response.create(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        from_pdf = await response.parse()
        assert_matches_type(object, from_pdf, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMaisa) -> None:
        async with async_client.file_interpreter.from_pdf.with_streaming_response.create(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            from_pdf = await response.parse()
            assert_matches_type(object, from_pdf, path=["response"])

        assert cast(Any, response.is_closed) is True
