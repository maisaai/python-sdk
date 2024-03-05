# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ..._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
)
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
from ...types.file_interpreter import from_html_create_params

__all__ = ["FromHTML", "AsyncFromHTML"]


class FromHTML(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FromHTMLWithRawResponse:
        return FromHTMLWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FromHTMLWithStreamingResponse:
        return FromHTMLWithStreamingResponse(self)

    def create(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Interprets html file and returns a markdown file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/file-interpreter/from-html",
            body=maybe_transform(body, from_html_create_params.FromHTMLCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncFromHTML(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFromHTMLWithRawResponse:
        return AsyncFromHTMLWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFromHTMLWithStreamingResponse:
        return AsyncFromHTMLWithStreamingResponse(self)

    async def create(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Interprets html file and returns a markdown file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/file-interpreter/from-html",
            body=await async_maybe_transform(body, from_html_create_params.FromHTMLCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class FromHTMLWithRawResponse:
    def __init__(self, from_html: FromHTML) -> None:
        self._from_html = from_html

        self.create = to_raw_response_wrapper(
            from_html.create,
        )


class AsyncFromHTMLWithRawResponse:
    def __init__(self, from_html: AsyncFromHTML) -> None:
        self._from_html = from_html

        self.create = async_to_raw_response_wrapper(
            from_html.create,
        )


class FromHTMLWithStreamingResponse:
    def __init__(self, from_html: FromHTML) -> None:
        self._from_html = from_html

        self.create = to_streamed_response_wrapper(
            from_html.create,
        )


class AsyncFromHTMLWithStreamingResponse:
    def __init__(self, from_html: AsyncFromHTML) -> None:
        self._from_html = from_html

        self.create = async_to_streamed_response_wrapper(
            from_html.create,
        )
