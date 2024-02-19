# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .search import (
    SearchResource,
    AsyncSearchResource,
    SearchResourceWithRawResponse,
    AsyncSearchResourceWithRawResponse,
    SearchResourceWithStreamingResponse,
    AsyncSearchResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Mainet", "AsyncMainet"]


class Mainet(SyncAPIResource):
    @cached_property
    def search(self) -> SearchResource:
        return SearchResource(self._client)

    @cached_property
    def with_raw_response(self) -> MainetWithRawResponse:
        return MainetWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MainetWithStreamingResponse:
        return MainetWithStreamingResponse(self)


class AsyncMainet(AsyncAPIResource):
    @cached_property
    def search(self) -> AsyncSearchResource:
        return AsyncSearchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMainetWithRawResponse:
        return AsyncMainetWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMainetWithStreamingResponse:
        return AsyncMainetWithStreamingResponse(self)


class MainetWithRawResponse:
    def __init__(self, mainet: Mainet) -> None:
        self._mainet = mainet

    @cached_property
    def search(self) -> SearchResourceWithRawResponse:
        return SearchResourceWithRawResponse(self._mainet.search)


class AsyncMainetWithRawResponse:
    def __init__(self, mainet: AsyncMainet) -> None:
        self._mainet = mainet

    @cached_property
    def search(self) -> AsyncSearchResourceWithRawResponse:
        return AsyncSearchResourceWithRawResponse(self._mainet.search)


class MainetWithStreamingResponse:
    def __init__(self, mainet: Mainet) -> None:
        self._mainet = mainet

    @cached_property
    def search(self) -> SearchResourceWithStreamingResponse:
        return SearchResourceWithStreamingResponse(self._mainet.search)


class AsyncMainetWithStreamingResponse:
    def __init__(self, mainet: AsyncMainet) -> None:
        self._mainet = mainet

    @cached_property
    def search(self) -> AsyncSearchResourceWithStreamingResponse:
        return AsyncSearchResourceWithStreamingResponse(self._mainet.search)
