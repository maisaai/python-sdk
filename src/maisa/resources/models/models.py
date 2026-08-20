# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .embeddings import (
    EmbeddingsResource,
    AsyncEmbeddingsResource,
    EmbeddingsResourceWithRawResponse,
    AsyncEmbeddingsResourceWithRawResponse,
    EmbeddingsResourceWithStreamingResponse,
    AsyncEmbeddingsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ModelsResource", "AsyncModelsResource"]


class ModelsResource(SyncAPIResource):
    @cached_property
    def embeddings(self) -> EmbeddingsResource:
        return EmbeddingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/maisaai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/maisaai/python-sdk#with_streaming_response
        """
        return ModelsResourceWithStreamingResponse(self)


class AsyncModelsResource(AsyncAPIResource):
    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResource:
        return AsyncEmbeddingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/maisaai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/maisaai/python-sdk#with_streaming_response
        """
        return AsyncModelsResourceWithStreamingResponse(self)


class ModelsResourceWithRawResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

    @cached_property
    def embeddings(self) -> EmbeddingsResourceWithRawResponse:
        return EmbeddingsResourceWithRawResponse(self._models.embeddings)


class AsyncModelsResourceWithRawResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResourceWithRawResponse:
        return AsyncEmbeddingsResourceWithRawResponse(self._models.embeddings)


class ModelsResourceWithStreamingResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

    @cached_property
    def embeddings(self) -> EmbeddingsResourceWithStreamingResponse:
        return EmbeddingsResourceWithStreamingResponse(self._models.embeddings)


class AsyncModelsResourceWithStreamingResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResourceWithStreamingResponse:
        return AsyncEmbeddingsResourceWithStreamingResponse(self._models.embeddings)
