# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

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
from ...types.mainet import Search, search_create_params

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        return SearchResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Search:
        """
        Finds content in mainet network

        Args:
          text: The text or query to search for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/mainet/search",
            body=maybe_transform({"text": text}, search_create_params.SearchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Search,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        return AsyncSearchResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Search:
        """
        Finds content in mainet network

        Args:
          text: The text or query to search for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/mainet/search",
            body=maybe_transform({"text": text}, search_create_params.SearchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Search,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.create = to_raw_response_wrapper(
            search.create,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.create = async_to_raw_response_wrapper(
            search.create,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.create = to_streamed_response_wrapper(
            search.create,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.create = async_to_streamed_response_wrapper(
            search.create,
        )
