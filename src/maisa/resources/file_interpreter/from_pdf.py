# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.file_interpreter import from_pdf_create_params

__all__ = ["FromPdfResource", "AsyncFromPdfResource"]


class FromPdfResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FromPdfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/maisaai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return FromPdfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FromPdfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/maisaai/python-sdk#with_streaming_response
        """
        return FromPdfResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file: FileTypes,
        max_pages: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Transform PDF to Markdown

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/file-interpreter/from-pdf",
            body=maybe_transform(body, from_pdf_create_params.FromPdfCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"max_pages": max_pages}, from_pdf_create_params.FromPdfCreateParams),
            ),
            cast_to=object,
        )


class AsyncFromPdfResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFromPdfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/maisaai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFromPdfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFromPdfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/maisaai/python-sdk#with_streaming_response
        """
        return AsyncFromPdfResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file: FileTypes,
        max_pages: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Transform PDF to Markdown

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/file-interpreter/from-pdf",
            body=await async_maybe_transform(body, from_pdf_create_params.FromPdfCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"max_pages": max_pages}, from_pdf_create_params.FromPdfCreateParams),
            ),
            cast_to=object,
        )


class FromPdfResourceWithRawResponse:
    def __init__(self, from_pdf: FromPdfResource) -> None:
        self._from_pdf = from_pdf

        self.create = to_raw_response_wrapper(
            from_pdf.create,
        )


class AsyncFromPdfResourceWithRawResponse:
    def __init__(self, from_pdf: AsyncFromPdfResource) -> None:
        self._from_pdf = from_pdf

        self.create = async_to_raw_response_wrapper(
            from_pdf.create,
        )


class FromPdfResourceWithStreamingResponse:
    def __init__(self, from_pdf: FromPdfResource) -> None:
        self._from_pdf = from_pdf

        self.create = to_streamed_response_wrapper(
            from_pdf.create,
        )


class AsyncFromPdfResourceWithStreamingResponse:
    def __init__(self, from_pdf: AsyncFromPdfResource) -> None:
        self._from_pdf = from_pdf

        self.create = async_to_streamed_response_wrapper(
            from_pdf.create,
        )
