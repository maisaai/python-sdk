# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from maisa import Maisa, AsyncMaisa
from tests.utils import assert_matches_type
from maisa.types.shared import TextSummary, TextExtractor, TextComparator

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMedia:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_compare(self, client: Maisa) -> None:
        media = client.capabilities.media.compare(
            file1=b"raw file contents",
            file2=b"raw file contents",
        )
        assert_matches_type(TextComparator, media, path=["response"])

    @parametrize
    def test_method_compare_with_all_params(self, client: Maisa) -> None:
        media = client.capabilities.media.compare(
            file1=b"raw file contents",
            file2=b"raw file contents",
            lang="en",
            prompt="Compare the value for end customer.",
            variable1_description="The name of the person.",
            variable1_name="Name",
            variable1_type="string",
            variable2_description="The name of the person.",
            variable2_name="Name",
            variable2_type="string",
            variable3_description="The name of the person.",
            variable3_name="Name",
            variable3_type="string",
            variable4_description="The name of the person.",
            variable4_name="Name",
            variable4_type="string",
        )
        assert_matches_type(TextComparator, media, path=["response"])

    @parametrize
    def test_raw_response_compare(self, client: Maisa) -> None:
        response = client.capabilities.media.with_raw_response.compare(
            file1=b"raw file contents",
            file2=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(TextComparator, media, path=["response"])

    @parametrize
    def test_streaming_response_compare(self, client: Maisa) -> None:
        with client.capabilities.media.with_streaming_response.compare(
            file1=b"raw file contents",
            file2=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(TextComparator, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_extract(self, client: Maisa) -> None:
        media = client.capabilities.media.extract(
            file=b"raw file contents",
        )
        assert_matches_type(TextExtractor, media, path=["response"])

    @parametrize
    def test_method_extract_with_all_params(self, client: Maisa) -> None:
        media = client.capabilities.media.extract(
            file=b"raw file contents",
            lang="en",
            variable1_description="The name of the person.",
            variable1_name="Name",
            variable1_type="string",
            variable2_description="The name of the person.",
            variable2_name="Name",
            variable2_type="string",
            variable3_description="The name of the person.",
            variable3_name="Name",
            variable3_type="string",
            variable4_description="The name of the person.",
            variable4_name="Name",
            variable4_type="string",
        )
        assert_matches_type(TextExtractor, media, path=["response"])

    @parametrize
    def test_raw_response_extract(self, client: Maisa) -> None:
        response = client.capabilities.media.with_raw_response.extract(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(TextExtractor, media, path=["response"])

    @parametrize
    def test_streaming_response_extract(self, client: Maisa) -> None:
        with client.capabilities.media.with_streaming_response.extract(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(TextExtractor, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_summarize(self, client: Maisa) -> None:
        media = client.capabilities.media.summarize(
            file=b"raw file contents",
        )
        assert_matches_type(TextSummary, media, path=["response"])

    @parametrize
    def test_method_summarize_with_all_params(self, client: Maisa) -> None:
        media = client.capabilities.media.summarize(
            file=b"raw file contents",
            format="paragraph",
            lang="en",
            length="short",
            summary_hint="Example summary of the text...",
        )
        assert_matches_type(TextSummary, media, path=["response"])

    @parametrize
    def test_raw_response_summarize(self, client: Maisa) -> None:
        response = client.capabilities.media.with_raw_response.summarize(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(TextSummary, media, path=["response"])

    @parametrize
    def test_streaming_response_summarize(self, client: Maisa) -> None:
        with client.capabilities.media.with_streaming_response.summarize(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(TextSummary, media, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMedia:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_compare(self, async_client: AsyncMaisa) -> None:
        media = await async_client.capabilities.media.compare(
            file1=b"raw file contents",
            file2=b"raw file contents",
        )
        assert_matches_type(TextComparator, media, path=["response"])

    @parametrize
    async def test_method_compare_with_all_params(self, async_client: AsyncMaisa) -> None:
        media = await async_client.capabilities.media.compare(
            file1=b"raw file contents",
            file2=b"raw file contents",
            lang="en",
            prompt="Compare the value for end customer.",
            variable1_description="The name of the person.",
            variable1_name="Name",
            variable1_type="string",
            variable2_description="The name of the person.",
            variable2_name="Name",
            variable2_type="string",
            variable3_description="The name of the person.",
            variable3_name="Name",
            variable3_type="string",
            variable4_description="The name of the person.",
            variable4_name="Name",
            variable4_type="string",
        )
        assert_matches_type(TextComparator, media, path=["response"])

    @parametrize
    async def test_raw_response_compare(self, async_client: AsyncMaisa) -> None:
        response = await async_client.capabilities.media.with_raw_response.compare(
            file1=b"raw file contents",
            file2=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(TextComparator, media, path=["response"])

    @parametrize
    async def test_streaming_response_compare(self, async_client: AsyncMaisa) -> None:
        async with async_client.capabilities.media.with_streaming_response.compare(
            file1=b"raw file contents",
            file2=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(TextComparator, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_extract(self, async_client: AsyncMaisa) -> None:
        media = await async_client.capabilities.media.extract(
            file=b"raw file contents",
        )
        assert_matches_type(TextExtractor, media, path=["response"])

    @parametrize
    async def test_method_extract_with_all_params(self, async_client: AsyncMaisa) -> None:
        media = await async_client.capabilities.media.extract(
            file=b"raw file contents",
            lang="en",
            variable1_description="The name of the person.",
            variable1_name="Name",
            variable1_type="string",
            variable2_description="The name of the person.",
            variable2_name="Name",
            variable2_type="string",
            variable3_description="The name of the person.",
            variable3_name="Name",
            variable3_type="string",
            variable4_description="The name of the person.",
            variable4_name="Name",
            variable4_type="string",
        )
        assert_matches_type(TextExtractor, media, path=["response"])

    @parametrize
    async def test_raw_response_extract(self, async_client: AsyncMaisa) -> None:
        response = await async_client.capabilities.media.with_raw_response.extract(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(TextExtractor, media, path=["response"])

    @parametrize
    async def test_streaming_response_extract(self, async_client: AsyncMaisa) -> None:
        async with async_client.capabilities.media.with_streaming_response.extract(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(TextExtractor, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_summarize(self, async_client: AsyncMaisa) -> None:
        media = await async_client.capabilities.media.summarize(
            file=b"raw file contents",
        )
        assert_matches_type(TextSummary, media, path=["response"])

    @parametrize
    async def test_method_summarize_with_all_params(self, async_client: AsyncMaisa) -> None:
        media = await async_client.capabilities.media.summarize(
            file=b"raw file contents",
            format="paragraph",
            lang="en",
            length="short",
            summary_hint="Example summary of the text...",
        )
        assert_matches_type(TextSummary, media, path=["response"])

    @parametrize
    async def test_raw_response_summarize(self, async_client: AsyncMaisa) -> None:
        response = await async_client.capabilities.media.with_raw_response.summarize(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(TextSummary, media, path=["response"])

    @parametrize
    async def test_streaming_response_summarize(self, async_client: AsyncMaisa) -> None:
        async with async_client.capabilities.media.with_streaming_response.summarize(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(TextSummary, media, path=["response"])

        assert cast(Any, response.is_closed) is True
