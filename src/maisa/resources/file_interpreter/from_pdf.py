# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Mapping, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ..._utils import extract_files, maybe_transform, deepcopy_minimal
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
from ...types.file_interpreter import from_pdf_create_params

__all__ = ["FromPdf", "AsyncFromPdf"]


class FromPdf(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FromPdfWithRawResponse:
        return FromPdfWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FromPdfWithStreamingResponse:
        return FromPdfWithStreamingResponse(self)

    def create(
        self,
        *,
        file: FileTypes,
        max_pages: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        if files:
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


class AsyncFromPdf(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFromPdfWithRawResponse:
        return AsyncFromPdfWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFromPdfWithStreamingResponse:
        return AsyncFromPdfWithStreamingResponse(self)

    async def create(
        self,
        *,
        file: FileTypes,
        max_pages: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
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


class FromPdfWithRawResponse:
    def __init__(self, from_pdf: FromPdf) -> None:
        self._from_pdf = from_pdf

        self.create = to_raw_response_wrapper(
            from_pdf.create,
        )


class AsyncFromPdfWithRawResponse:
    def __init__(self, from_pdf: AsyncFromPdf) -> None:
        self._from_pdf = from_pdf

        self.create = async_to_raw_response_wrapper(
            from_pdf.create,
        )


class FromPdfWithStreamingResponse:
    def __init__(self, from_pdf: FromPdf) -> None:
        self._from_pdf = from_pdf

        self.create = to_streamed_response_wrapper(
            from_pdf.create,
        )


class AsyncFromPdfWithStreamingResponse:
    def __init__(self, from_pdf: AsyncFromPdf) -> None:
        self._from_pdf = from_pdf

        self.create = async_to_streamed_response_wrapper(
            from_pdf.create,
        )
