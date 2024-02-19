# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

import httpx

from ...types import ModelRerankResponse, model_rerank_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from .embeddings import (
    Embeddings,
    AsyncEmbeddings,
    EmbeddingsWithRawResponse,
    AsyncEmbeddingsWithRawResponse,
    EmbeddingsWithStreamingResponse,
    AsyncEmbeddingsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["Models", "AsyncModels"]


class Models(SyncAPIResource):
    @cached_property
    def embeddings(self) -> Embeddings:
        return Embeddings(self._client)

    @cached_property
    def with_raw_response(self) -> ModelsWithRawResponse:
        return ModelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelsWithStreamingResponse:
        return ModelsWithStreamingResponse(self)

    def rerank(
        self,
        *,
        sentences: List[str],
        source_sentence: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelRerankResponse:
        """
        Rerank the sentences based on the similarity with the source sentence.

        Args:
          sentences: A list of sentences to be reranked.

          source_sentence: The sentence to be used as a reference to rerank the sentences.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/models/rerank",
            body=maybe_transform(
                {
                    "sentences": sentences,
                    "source_sentence": source_sentence,
                },
                model_rerank_params.ModelRerankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelRerankResponse,
        )


class AsyncModels(AsyncAPIResource):
    @cached_property
    def embeddings(self) -> AsyncEmbeddings:
        return AsyncEmbeddings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncModelsWithRawResponse:
        return AsyncModelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelsWithStreamingResponse:
        return AsyncModelsWithStreamingResponse(self)

    async def rerank(
        self,
        *,
        sentences: List[str],
        source_sentence: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelRerankResponse:
        """
        Rerank the sentences based on the similarity with the source sentence.

        Args:
          sentences: A list of sentences to be reranked.

          source_sentence: The sentence to be used as a reference to rerank the sentences.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/models/rerank",
            body=maybe_transform(
                {
                    "sentences": sentences,
                    "source_sentence": source_sentence,
                },
                model_rerank_params.ModelRerankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelRerankResponse,
        )


class ModelsWithRawResponse:
    def __init__(self, models: Models) -> None:
        self._models = models

        self.rerank = to_raw_response_wrapper(
            models.rerank,
        )

    @cached_property
    def embeddings(self) -> EmbeddingsWithRawResponse:
        return EmbeddingsWithRawResponse(self._models.embeddings)


class AsyncModelsWithRawResponse:
    def __init__(self, models: AsyncModels) -> None:
        self._models = models

        self.rerank = async_to_raw_response_wrapper(
            models.rerank,
        )

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsWithRawResponse:
        return AsyncEmbeddingsWithRawResponse(self._models.embeddings)


class ModelsWithStreamingResponse:
    def __init__(self, models: Models) -> None:
        self._models = models

        self.rerank = to_streamed_response_wrapper(
            models.rerank,
        )

    @cached_property
    def embeddings(self) -> EmbeddingsWithStreamingResponse:
        return EmbeddingsWithStreamingResponse(self._models.embeddings)


class AsyncModelsWithStreamingResponse:
    def __init__(self, models: AsyncModels) -> None:
        self._models = models

        self.rerank = async_to_streamed_response_wrapper(
            models.rerank,
        )

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsWithStreamingResponse:
        return AsyncEmbeddingsWithStreamingResponse(self._models.embeddings)
