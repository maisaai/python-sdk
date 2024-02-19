# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ..._utils import extract_files, maybe_transform, deepcopy_minimal
from ..._compat import cached_property
from ...types.ai import (
    MediaCompareResponse,
    MediaExtractResponse,
    MediaSummarizeResponse,
    media_compare_params,
    media_extract_params,
    media_summarize_params,
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

__all__ = ["Media", "AsyncMedia"]


class Media(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MediaWithRawResponse:
        return MediaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MediaWithStreamingResponse:
        return MediaWithStreamingResponse(self)

    def compare(
        self,
        *,
        file1: FileTypes,
        file2: FileTypes,
        model: media_compare_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaCompareResponse:
        """
        Compare extracts of media files based on a specific data.

        Args:
          model: Media Comparator Request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file1": file1,
                "file2": file2,
                "model": model,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file1"], ["file2"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/ai/compare/media",
            body=maybe_transform(body, media_compare_params.MediaCompareParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaCompareResponse,
        )

    def extract(
        self,
        *,
        file: FileTypes,
        model: media_extract_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaExtractResponse:
        """Extracts structured data from a file.

        The text is analyzed and the variables are
        extracted.

        Args:
          model: Media Extraction Request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "model": model,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/ai/extract/media",
            body=maybe_transform(body, media_extract_params.MediaExtractParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaExtractResponse,
        )

    def summarize(
        self,
        *,
        file: FileTypes,
        model: media_summarize_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaSummarizeResponse:
        """
        Summarizes a media file.

        Args:
          model: Media Summary Request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "model": model,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/ai/summarize/media",
            body=maybe_transform(body, media_summarize_params.MediaSummarizeParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaSummarizeResponse,
        )


class AsyncMedia(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMediaWithRawResponse:
        return AsyncMediaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMediaWithStreamingResponse:
        return AsyncMediaWithStreamingResponse(self)

    async def compare(
        self,
        *,
        file1: FileTypes,
        file2: FileTypes,
        model: media_compare_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaCompareResponse:
        """
        Compare extracts of media files based on a specific data.

        Args:
          model: Media Comparator Request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file1": file1,
                "file2": file2,
                "model": model,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file1"], ["file2"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/ai/compare/media",
            body=maybe_transform(body, media_compare_params.MediaCompareParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaCompareResponse,
        )

    async def extract(
        self,
        *,
        file: FileTypes,
        model: media_extract_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaExtractResponse:
        """Extracts structured data from a file.

        The text is analyzed and the variables are
        extracted.

        Args:
          model: Media Extraction Request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "model": model,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/ai/extract/media",
            body=maybe_transform(body, media_extract_params.MediaExtractParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaExtractResponse,
        )

    async def summarize(
        self,
        *,
        file: FileTypes,
        model: media_summarize_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaSummarizeResponse:
        """
        Summarizes a media file.

        Args:
          model: Media Summary Request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "model": model,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/ai/summarize/media",
            body=maybe_transform(body, media_summarize_params.MediaSummarizeParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaSummarizeResponse,
        )


class MediaWithRawResponse:
    def __init__(self, media: Media) -> None:
        self._media = media

        self.compare = to_raw_response_wrapper(
            media.compare,
        )
        self.extract = to_raw_response_wrapper(
            media.extract,
        )
        self.summarize = to_raw_response_wrapper(
            media.summarize,
        )


class AsyncMediaWithRawResponse:
    def __init__(self, media: AsyncMedia) -> None:
        self._media = media

        self.compare = async_to_raw_response_wrapper(
            media.compare,
        )
        self.extract = async_to_raw_response_wrapper(
            media.extract,
        )
        self.summarize = async_to_raw_response_wrapper(
            media.summarize,
        )


class MediaWithStreamingResponse:
    def __init__(self, media: Media) -> None:
        self._media = media

        self.compare = to_streamed_response_wrapper(
            media.compare,
        )
        self.extract = to_streamed_response_wrapper(
            media.extract,
        )
        self.summarize = to_streamed_response_wrapper(
            media.summarize,
        )


class AsyncMediaWithStreamingResponse:
    def __init__(self, media: AsyncMedia) -> None:
        self._media = media

        self.compare = async_to_streamed_response_wrapper(
            media.compare,
        )
        self.extract = async_to_streamed_response_wrapper(
            media.extract,
        )
        self.summarize = async_to_streamed_response_wrapper(
            media.summarize,
        )
