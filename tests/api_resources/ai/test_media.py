# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from maisa import Maisa, AsyncMaisa
from tests.utils import assert_matches_type
from maisa.types.ai import (
    MediaCompareResponse,
    MediaExtractResponse,
    MediaSummarizeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMedia:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_compare(self, client: Maisa) -> None:
        media = client.ai.media.compare(
            file1=b"raw file contents",
            file2=b"raw file contents",
            model={
                "variables": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person.",
                    }
                }
            },
        )
        assert_matches_type(MediaCompareResponse, media, path=["response"])

    @parametrize
    def test_method_compare_with_all_params(self, client: Maisa) -> None:
        media = client.ai.media.compare(
            file1=b"raw file contents",
            file2=b"raw file contents",
            model={
                "prompt": "Compare the value for end customer.",
                "variables": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person.",
                    }
                },
                "lang": "en",
                "metadata_media1": {"keywords": ["writing", "author"]},
                "metadata_media2": {"keywords": ["music", "band"]},
            },
        )
        assert_matches_type(MediaCompareResponse, media, path=["response"])

    @parametrize
    def test_raw_response_compare(self, client: Maisa) -> None:
        response = client.ai.media.with_raw_response.compare(
            file1=b"raw file contents",
            file2=b"raw file contents",
            model={
                "variables": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person.",
                    }
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaCompareResponse, media, path=["response"])

    @parametrize
    def test_streaming_response_compare(self, client: Maisa) -> None:
        with client.ai.media.with_streaming_response.compare(
            file1=b"raw file contents",
            file2=b"raw file contents",
            model={
                "variables": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person.",
                    }
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaCompareResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_extract(self, client: Maisa) -> None:
        media = client.ai.media.extract(
            file=b"raw file contents",
            model={
                "variables": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person.",
                    }
                }
            },
        )
        assert_matches_type(MediaExtractResponse, media, path=["response"])

    @parametrize
    def test_method_extract_with_all_params(self, client: Maisa) -> None:
        media = client.ai.media.extract(
            file=b"raw file contents",
            model={
                "variables": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person.",
                    }
                },
                "lang": "en",
                "metadata": {"keywords": ["writing", "author"]},
            },
        )
        assert_matches_type(MediaExtractResponse, media, path=["response"])

    @parametrize
    def test_raw_response_extract(self, client: Maisa) -> None:
        response = client.ai.media.with_raw_response.extract(
            file=b"raw file contents",
            model={
                "variables": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person.",
                    }
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaExtractResponse, media, path=["response"])

    @parametrize
    def test_streaming_response_extract(self, client: Maisa) -> None:
        with client.ai.media.with_streaming_response.extract(
            file=b"raw file contents",
            model={
                "variables": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person.",
                    }
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaExtractResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_summarize(self, client: Maisa) -> None:
        media = client.ai.media.summarize(
            file=b"raw file contents",
            model={},
        )
        assert_matches_type(MediaSummarizeResponse, media, path=["response"])

    @parametrize
    def test_method_summarize_with_all_params(self, client: Maisa) -> None:
        media = client.ai.media.summarize(
            file=b"raw file contents",
            model={
                "format": "paragraph",
                "length": "long",
                "lang": "en",
                "summary_hint": "Example summary of the text...",
                "metadata": {"keywords": ["writing", "author"]},
            },
        )
        assert_matches_type(MediaSummarizeResponse, media, path=["response"])

    @parametrize
    def test_raw_response_summarize(self, client: Maisa) -> None:
        response = client.ai.media.with_raw_response.summarize(
            file=b"raw file contents",
            model={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaSummarizeResponse, media, path=["response"])

    @parametrize
    def test_streaming_response_summarize(self, client: Maisa) -> None:
        with client.ai.media.with_streaming_response.summarize(
            file=b"raw file contents",
            model={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaSummarizeResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMedia:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_compare(self, async_client: AsyncMaisa) -> None:
        media = await async_client.ai.media.compare(
            file1=b"raw file contents",
            file2=b"raw file contents",
            model={
                "variables": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person.",
                    }
                }
            },
        )
        assert_matches_type(MediaCompareResponse, media, path=["response"])

    @parametrize
    async def test_method_compare_with_all_params(self, async_client: AsyncMaisa) -> None:
        media = await async_client.ai.media.compare(
            file1=b"raw file contents",
            file2=b"raw file contents",
            model={
                "prompt": "Compare the value for end customer.",
                "variables": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person.",
                    }
                },
                "lang": "en",
                "metadata_media1": {"keywords": ["writing", "author"]},
                "metadata_media2": {"keywords": ["music", "band"]},
            },
        )
        assert_matches_type(MediaCompareResponse, media, path=["response"])

    @parametrize
    async def test_raw_response_compare(self, async_client: AsyncMaisa) -> None:
        response = await async_client.ai.media.with_raw_response.compare(
            file1=b"raw file contents",
            file2=b"raw file contents",
            model={
                "variables": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person.",
                    }
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaCompareResponse, media, path=["response"])

    @parametrize
    async def test_streaming_response_compare(self, async_client: AsyncMaisa) -> None:
        async with async_client.ai.media.with_streaming_response.compare(
            file1=b"raw file contents",
            file2=b"raw file contents",
            model={
                "variables": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person.",
                    }
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaCompareResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_extract(self, async_client: AsyncMaisa) -> None:
        media = await async_client.ai.media.extract(
            file=b"raw file contents",
            model={
                "variables": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person.",
                    }
                }
            },
        )
        assert_matches_type(MediaExtractResponse, media, path=["response"])

    @parametrize
    async def test_method_extract_with_all_params(self, async_client: AsyncMaisa) -> None:
        media = await async_client.ai.media.extract(
            file=b"raw file contents",
            model={
                "variables": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person.",
                    }
                },
                "lang": "en",
                "metadata": {"keywords": ["writing", "author"]},
            },
        )
        assert_matches_type(MediaExtractResponse, media, path=["response"])

    @parametrize
    async def test_raw_response_extract(self, async_client: AsyncMaisa) -> None:
        response = await async_client.ai.media.with_raw_response.extract(
            file=b"raw file contents",
            model={
                "variables": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person.",
                    }
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaExtractResponse, media, path=["response"])

    @parametrize
    async def test_streaming_response_extract(self, async_client: AsyncMaisa) -> None:
        async with async_client.ai.media.with_streaming_response.extract(
            file=b"raw file contents",
            model={
                "variables": {
                    "name": {
                        "type": "string",
                        "description": "The name of the person.",
                    }
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaExtractResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_summarize(self, async_client: AsyncMaisa) -> None:
        media = await async_client.ai.media.summarize(
            file=b"raw file contents",
            model={},
        )
        assert_matches_type(MediaSummarizeResponse, media, path=["response"])

    @parametrize
    async def test_method_summarize_with_all_params(self, async_client: AsyncMaisa) -> None:
        media = await async_client.ai.media.summarize(
            file=b"raw file contents",
            model={
                "format": "paragraph",
                "length": "long",
                "lang": "en",
                "summary_hint": "Example summary of the text...",
                "metadata": {"keywords": ["writing", "author"]},
            },
        )
        assert_matches_type(MediaSummarizeResponse, media, path=["response"])

    @parametrize
    async def test_raw_response_summarize(self, async_client: AsyncMaisa) -> None:
        response = await async_client.ai.media.with_raw_response.summarize(
            file=b"raw file contents",
            model={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaSummarizeResponse, media, path=["response"])

    @parametrize
    async def test_streaming_response_summarize(self, async_client: AsyncMaisa) -> None:
        async with async_client.ai.media.with_streaming_response.summarize(
            file=b"raw file contents",
            model={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaSummarizeResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True
