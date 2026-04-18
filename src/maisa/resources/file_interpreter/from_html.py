# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..._files import deepcopy_with_paths
from ..._types import Body, Query, Headers, NotGiven, FileTypes, not_given
from ..._utils import extract_files, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.file_interpreter import from_html_create_params

__all__ = ["FromHTMLResource", "AsyncFromHTMLResource"]


class FromHTMLResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FromHTMLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/maisaai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return FromHTMLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FromHTMLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/maisaai/python-sdk#with_streaming_response
        """
        return FromHTMLResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Interprets html file and returns a markdown file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths({"file": file}, [["file"]])
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
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


class AsyncFromHTMLResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFromHTMLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/maisaai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFromHTMLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFromHTMLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/maisaai/python-sdk#with_streaming_response
        """
        return AsyncFromHTMLResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Interprets html file and returns a markdown file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths({"file": file}, [["file"]])
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
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


class FromHTMLResourceWithRawResponse:
    def __init__(self, from_html: FromHTMLResource) -> None:
        self._from_html = from_html

        self.create = to_raw_response_wrapper(
            from_html.create,
        )


class AsyncFromHTMLResourceWithRawResponse:
    def __init__(self, from_html: AsyncFromHTMLResource) -> None:
        self._from_html = from_html

        self.create = async_to_raw_response_wrapper(
            from_html.create,
        )


class FromHTMLResourceWithStreamingResponse:
    def __init__(self, from_html: FromHTMLResource) -> None:
        self._from_html = from_html

        self.create = to_streamed_response_wrapper(
            from_html.create,
        )


class AsyncFromHTMLResourceWithStreamingResponse:
    def __init__(self, from_html: AsyncFromHTMLResource) -> None:
        self._from_html = from_html

        self.create = async_to_streamed_response_wrapper(
            from_html.create,
        )
