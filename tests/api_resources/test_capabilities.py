# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from maisa import Maisa, AsyncMaisa
from tests.utils import assert_matches_type
from maisa.types.shared import TextSummary, TextExtractor, TextComparator

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCapabilities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_compare(self, client: Maisa) -> None:
        capability = client.capabilities.compare(
            text1="Lorem Ipsum dolor sit amet",
            text2="Sed ut perspiciatis unde omnis",
            variables={
                "name": {
                    "type": "string",
                    "description": "The name of the person.",
                }
            },
        )
        assert_matches_type(TextComparator, capability, path=["response"])

    @parametrize
    def test_method_compare_with_all_params(self, client: Maisa) -> None:
        capability = client.capabilities.compare(
            text1="Lorem Ipsum dolor sit amet",
            text2="Sed ut perspiciatis unde omnis",
            variables={
                "name": {
                    "type": "string",
                    "description": "The name of the person.",
                }
            },
            lang="en",
            prompt="Compare the value for end customer.",
        )
        assert_matches_type(TextComparator, capability, path=["response"])

    @parametrize
    def test_raw_response_compare(self, client: Maisa) -> None:
        response = client.capabilities.with_raw_response.compare(
            text1="Lorem Ipsum dolor sit amet",
            text2="Sed ut perspiciatis unde omnis",
            variables={
                "name": {
                    "type": "string",
                    "description": "The name of the person.",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = response.parse()
        assert_matches_type(TextComparator, capability, path=["response"])

    @parametrize
    def test_streaming_response_compare(self, client: Maisa) -> None:
        with client.capabilities.with_streaming_response.compare(
            text1="Lorem Ipsum dolor sit amet",
            text2="Sed ut perspiciatis unde omnis",
            variables={
                "name": {
                    "type": "string",
                    "description": "The name of the person.",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = response.parse()
            assert_matches_type(TextComparator, capability, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_extract(self, client: Maisa) -> None:
        capability = client.capabilities.extract(
            text="Example long text...",
            variables={
                "name": {
                    "type": "string",
                    "description": "The name of the person.",
                }
            },
        )
        assert_matches_type(TextExtractor, capability, path=["response"])

    @parametrize
    def test_method_extract_with_all_params(self, client: Maisa) -> None:
        capability = client.capabilities.extract(
            text="Example long text...",
            variables={
                "name": {
                    "type": "string",
                    "description": "The name of the person.",
                }
            },
            lang="en",
        )
        assert_matches_type(TextExtractor, capability, path=["response"])

    @parametrize
    def test_raw_response_extract(self, client: Maisa) -> None:
        response = client.capabilities.with_raw_response.extract(
            text="Example long text...",
            variables={
                "name": {
                    "type": "string",
                    "description": "The name of the person.",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = response.parse()
        assert_matches_type(TextExtractor, capability, path=["response"])

    @parametrize
    def test_streaming_response_extract(self, client: Maisa) -> None:
        with client.capabilities.with_streaming_response.extract(
            text="Example long text...",
            variables={
                "name": {
                    "type": "string",
                    "description": "The name of the person.",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = response.parse()
            assert_matches_type(TextExtractor, capability, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_summarize(self, client: Maisa) -> None:
        capability = client.capabilities.summarize(
            text="Example long text...",
        )
        assert_matches_type(TextSummary, capability, path=["response"])

    @parametrize
    def test_method_summarize_with_all_params(self, client: Maisa) -> None:
        capability = client.capabilities.summarize(
            text="Example long text...",
            format="paragraph",
            lang="en",
            length="medium",
            summary_hint="Example summary of the text...",
        )
        assert_matches_type(TextSummary, capability, path=["response"])

    @parametrize
    def test_raw_response_summarize(self, client: Maisa) -> None:
        response = client.capabilities.with_raw_response.summarize(
            text="Example long text...",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = response.parse()
        assert_matches_type(TextSummary, capability, path=["response"])

    @parametrize
    def test_streaming_response_summarize(self, client: Maisa) -> None:
        with client.capabilities.with_streaming_response.summarize(
            text="Example long text...",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = response.parse()
            assert_matches_type(TextSummary, capability, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCapabilities:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_compare(self, async_client: AsyncMaisa) -> None:
        capability = await async_client.capabilities.compare(
            text1="Lorem Ipsum dolor sit amet",
            text2="Sed ut perspiciatis unde omnis",
            variables={
                "name": {
                    "type": "string",
                    "description": "The name of the person.",
                }
            },
        )
        assert_matches_type(TextComparator, capability, path=["response"])

    @parametrize
    async def test_method_compare_with_all_params(self, async_client: AsyncMaisa) -> None:
        capability = await async_client.capabilities.compare(
            text1="Lorem Ipsum dolor sit amet",
            text2="Sed ut perspiciatis unde omnis",
            variables={
                "name": {
                    "type": "string",
                    "description": "The name of the person.",
                }
            },
            lang="en",
            prompt="Compare the value for end customer.",
        )
        assert_matches_type(TextComparator, capability, path=["response"])

    @parametrize
    async def test_raw_response_compare(self, async_client: AsyncMaisa) -> None:
        response = await async_client.capabilities.with_raw_response.compare(
            text1="Lorem Ipsum dolor sit amet",
            text2="Sed ut perspiciatis unde omnis",
            variables={
                "name": {
                    "type": "string",
                    "description": "The name of the person.",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = await response.parse()
        assert_matches_type(TextComparator, capability, path=["response"])

    @parametrize
    async def test_streaming_response_compare(self, async_client: AsyncMaisa) -> None:
        async with async_client.capabilities.with_streaming_response.compare(
            text1="Lorem Ipsum dolor sit amet",
            text2="Sed ut perspiciatis unde omnis",
            variables={
                "name": {
                    "type": "string",
                    "description": "The name of the person.",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = await response.parse()
            assert_matches_type(TextComparator, capability, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_extract(self, async_client: AsyncMaisa) -> None:
        capability = await async_client.capabilities.extract(
            text="Example long text...",
            variables={
                "name": {
                    "type": "string",
                    "description": "The name of the person.",
                }
            },
        )
        assert_matches_type(TextExtractor, capability, path=["response"])

    @parametrize
    async def test_method_extract_with_all_params(self, async_client: AsyncMaisa) -> None:
        capability = await async_client.capabilities.extract(
            text="Example long text...",
            variables={
                "name": {
                    "type": "string",
                    "description": "The name of the person.",
                }
            },
            lang="en",
        )
        assert_matches_type(TextExtractor, capability, path=["response"])

    @parametrize
    async def test_raw_response_extract(self, async_client: AsyncMaisa) -> None:
        response = await async_client.capabilities.with_raw_response.extract(
            text="Example long text...",
            variables={
                "name": {
                    "type": "string",
                    "description": "The name of the person.",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = await response.parse()
        assert_matches_type(TextExtractor, capability, path=["response"])

    @parametrize
    async def test_streaming_response_extract(self, async_client: AsyncMaisa) -> None:
        async with async_client.capabilities.with_streaming_response.extract(
            text="Example long text...",
            variables={
                "name": {
                    "type": "string",
                    "description": "The name of the person.",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = await response.parse()
            assert_matches_type(TextExtractor, capability, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_summarize(self, async_client: AsyncMaisa) -> None:
        capability = await async_client.capabilities.summarize(
            text="Example long text...",
        )
        assert_matches_type(TextSummary, capability, path=["response"])

    @parametrize
    async def test_method_summarize_with_all_params(self, async_client: AsyncMaisa) -> None:
        capability = await async_client.capabilities.summarize(
            text="Example long text...",
            format="paragraph",
            lang="en",
            length="medium",
            summary_hint="Example summary of the text...",
        )
        assert_matches_type(TextSummary, capability, path=["response"])

    @parametrize
    async def test_raw_response_summarize(self, async_client: AsyncMaisa) -> None:
        response = await async_client.capabilities.with_raw_response.summarize(
            text="Example long text...",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = await response.parse()
        assert_matches_type(TextSummary, capability, path=["response"])

    @parametrize
    async def test_streaming_response_summarize(self, async_client: AsyncMaisa) -> None:
        async with async_client.capabilities.with_streaming_response.summarize(
            text="Example long text...",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = await response.parse()
            assert_matches_type(TextSummary, capability, path=["response"])

        assert cast(Any, response.is_closed) is True
