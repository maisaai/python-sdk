# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
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
from ...types.models import Rerank, rerank_create_params

__all__ = ["RerankResource", "AsyncRerankResource"]


class RerankResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RerankResourceWithRawResponse:
        return RerankResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RerankResourceWithStreamingResponse:
        return RerankResourceWithStreamingResponse(self)

    def create(
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
    ) -> Rerank:
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
                rerank_create_params.RerankCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Rerank,
        )


class AsyncRerankResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRerankResourceWithRawResponse:
        return AsyncRerankResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRerankResourceWithStreamingResponse:
        return AsyncRerankResourceWithStreamingResponse(self)

    async def create(
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
    ) -> Rerank:
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
                rerank_create_params.RerankCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Rerank,
        )


class RerankResourceWithRawResponse:
    def __init__(self, rerank: RerankResource) -> None:
        self._rerank = rerank

        self.create = to_raw_response_wrapper(
            rerank.create,
        )


class AsyncRerankResourceWithRawResponse:
    def __init__(self, rerank: AsyncRerankResource) -> None:
        self._rerank = rerank

        self.create = async_to_raw_response_wrapper(
            rerank.create,
        )


class RerankResourceWithStreamingResponse:
    def __init__(self, rerank: RerankResource) -> None:
        self._rerank = rerank

        self.create = to_streamed_response_wrapper(
            rerank.create,
        )


class AsyncRerankResourceWithStreamingResponse:
    def __init__(self, rerank: AsyncRerankResource) -> None:
        self._rerank = rerank

        self.create = async_to_streamed_response_wrapper(
            rerank.create,
        )
