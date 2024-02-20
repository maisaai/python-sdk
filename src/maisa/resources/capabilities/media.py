# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

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
from ...types.shared import TextSummary, TextExtractor, TextComparator
from ...types.capabilities import media_compare_params, media_extract_params, media_summarize_params

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
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        variable1_description: str | NotGiven = NOT_GIVEN,
        variable1_name: str | NotGiven = NOT_GIVEN,
        variable1_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable2_description: str | NotGiven = NOT_GIVEN,
        variable2_name: str | NotGiven = NOT_GIVEN,
        variable2_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable3_description: str | NotGiven = NOT_GIVEN,
        variable3_name: str | NotGiven = NOT_GIVEN,
        variable3_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable4_description: str | NotGiven = NOT_GIVEN,
        variable4_name: str | NotGiven = NOT_GIVEN,
        variable4_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TextComparator:
        """Compare extracts of media files based on a specific data.

        This endpoint supports
        an additional field `model` documented in this url:
        https://dash.readme.com/project/clibrain-platform-api/v1.0/docs/capabilities-with-media-via-json-config

        Args:
          lang: The language of the output. If not provided, the language used will be the same
              as the language of the text provided.

          prompt: The prompt to be used as criteria to compare the texts.

          variable1_description: The description of the variable.

          variable1_name: The name of the variable to be compared.

          variable1_type: Text Extraction Request Variable Type.

          variable2_description: The description of the variable.

          variable2_name: The name of the variable to be compared.

          variable2_type: Text Extraction Request Variable Type.

          variable3_description: The description of the variable.

          variable3_name: The name of the variable to be compared.

          variable3_type: Text Extraction Request Variable Type.

          variable4_description: The description of the variable.

          variable4_name: The name of the variable to be compared.

          variable4_type: Text Extraction Request Variable Type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file1": file1,
                "file2": file2,
                "lang": lang,
                "prompt": prompt,
                "variable1_description": variable1_description,
                "variable1_name": variable1_name,
                "variable1_type": variable1_type,
                "variable2_description": variable2_description,
                "variable2_name": variable2_name,
                "variable2_type": variable2_type,
                "variable3_description": variable3_description,
                "variable3_name": variable3_name,
                "variable3_type": variable3_type,
                "variable4_description": variable4_description,
                "variable4_name": variable4_name,
                "variable4_type": variable4_type,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file1"], ["file2"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/capabilities/compare/media",
            body=maybe_transform(body, media_compare_params.MediaCompareParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TextComparator,
        )

    def extract(
        self,
        *,
        file: FileTypes,
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | NotGiven = NOT_GIVEN,
        variable1_description: str | NotGiven = NOT_GIVEN,
        variable1_name: str | NotGiven = NOT_GIVEN,
        variable1_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable2_description: str | NotGiven = NOT_GIVEN,
        variable2_name: str | NotGiven = NOT_GIVEN,
        variable2_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable3_description: str | NotGiven = NOT_GIVEN,
        variable3_name: str | NotGiven = NOT_GIVEN,
        variable3_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable4_description: str | NotGiven = NOT_GIVEN,
        variable4_name: str | NotGiven = NOT_GIVEN,
        variable4_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TextExtractor:
        """Extracts structured data from a file.

        The text is analyzed and the variables are
        extracted. This endpoint supports an additional field `model` documented in this
        url:
        https://dash.readme.com/project/clibrain-platform-api/v1.0/docs/capabilities-with-media-via-json-config

        Args:
          lang: The language of the output. If not provided, the language used will be the same
              as the language of the text provided.

          variable1_description: The description of the variable.

          variable1_name: The name of the variable to be extracted.

          variable1_type: Text Extraction Request Variable Type.

          variable2_description: The description of the variable.

          variable2_name: The name of the variable to be extracted.

          variable2_type: Text Extraction Request Variable Type.

          variable3_description: The description of the variable.

          variable3_name: The name of the variable to be extracted.

          variable3_type: Text Extraction Request Variable Type.

          variable4_description: The description of the variable.

          variable4_name: The name of the variable to be extracted.

          variable4_type: Text Extraction Request Variable Type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "lang": lang,
                "variable1_description": variable1_description,
                "variable1_name": variable1_name,
                "variable1_type": variable1_type,
                "variable2_description": variable2_description,
                "variable2_name": variable2_name,
                "variable2_type": variable2_type,
                "variable3_description": variable3_description,
                "variable3_name": variable3_name,
                "variable3_type": variable3_type,
                "variable4_description": variable4_description,
                "variable4_name": variable4_name,
                "variable4_type": variable4_type,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/capabilities/extract/media",
            body=maybe_transform(body, media_extract_params.MediaExtractParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TextExtractor,
        )

    def summarize(
        self,
        *,
        file: FileTypes,
        format: Literal["paragraph", "bullet"] | NotGiven = NOT_GIVEN,
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | NotGiven = NOT_GIVEN,
        length: Literal["short", "medium", "long"] | NotGiven = NOT_GIVEN,
        summary_hint: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TextSummary:
        """Summarizes a media file.

        This endpoint supports an additional field `model`
        documented in this url:
        https://dash.readme.com/project/clibrain-platform-api/v1.0/docs/capabilities-with-media-via-json-config

        Args:
          format: Text Summary Request Format.

          lang: The language of the output. If not provided, the language used will be the same
              as the language of the text provided.

          length: Text Summary Request Length.

          summary_hint: A hint to the summarization. This can be used to provide a specific

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "format": format,
                "lang": lang,
                "length": length,
                "summary_hint": summary_hint,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/capabilities/summarize/media",
            body=maybe_transform(body, media_summarize_params.MediaSummarizeParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TextSummary,
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
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        variable1_description: str | NotGiven = NOT_GIVEN,
        variable1_name: str | NotGiven = NOT_GIVEN,
        variable1_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable2_description: str | NotGiven = NOT_GIVEN,
        variable2_name: str | NotGiven = NOT_GIVEN,
        variable2_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable3_description: str | NotGiven = NOT_GIVEN,
        variable3_name: str | NotGiven = NOT_GIVEN,
        variable3_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable4_description: str | NotGiven = NOT_GIVEN,
        variable4_name: str | NotGiven = NOT_GIVEN,
        variable4_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TextComparator:
        """Compare extracts of media files based on a specific data.

        This endpoint supports
        an additional field `model` documented in this url:
        https://dash.readme.com/project/clibrain-platform-api/v1.0/docs/capabilities-with-media-via-json-config

        Args:
          lang: The language of the output. If not provided, the language used will be the same
              as the language of the text provided.

          prompt: The prompt to be used as criteria to compare the texts.

          variable1_description: The description of the variable.

          variable1_name: The name of the variable to be compared.

          variable1_type: Text Extraction Request Variable Type.

          variable2_description: The description of the variable.

          variable2_name: The name of the variable to be compared.

          variable2_type: Text Extraction Request Variable Type.

          variable3_description: The description of the variable.

          variable3_name: The name of the variable to be compared.

          variable3_type: Text Extraction Request Variable Type.

          variable4_description: The description of the variable.

          variable4_name: The name of the variable to be compared.

          variable4_type: Text Extraction Request Variable Type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file1": file1,
                "file2": file2,
                "lang": lang,
                "prompt": prompt,
                "variable1_description": variable1_description,
                "variable1_name": variable1_name,
                "variable1_type": variable1_type,
                "variable2_description": variable2_description,
                "variable2_name": variable2_name,
                "variable2_type": variable2_type,
                "variable3_description": variable3_description,
                "variable3_name": variable3_name,
                "variable3_type": variable3_type,
                "variable4_description": variable4_description,
                "variable4_name": variable4_name,
                "variable4_type": variable4_type,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file1"], ["file2"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/capabilities/compare/media",
            body=maybe_transform(body, media_compare_params.MediaCompareParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TextComparator,
        )

    async def extract(
        self,
        *,
        file: FileTypes,
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | NotGiven = NOT_GIVEN,
        variable1_description: str | NotGiven = NOT_GIVEN,
        variable1_name: str | NotGiven = NOT_GIVEN,
        variable1_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable2_description: str | NotGiven = NOT_GIVEN,
        variable2_name: str | NotGiven = NOT_GIVEN,
        variable2_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable3_description: str | NotGiven = NOT_GIVEN,
        variable3_name: str | NotGiven = NOT_GIVEN,
        variable3_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        variable4_description: str | NotGiven = NOT_GIVEN,
        variable4_name: str | NotGiven = NOT_GIVEN,
        variable4_type: Literal["string", "number", "date", "boolean"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TextExtractor:
        """Extracts structured data from a file.

        The text is analyzed and the variables are
        extracted. This endpoint supports an additional field `model` documented in this
        url:
        https://dash.readme.com/project/clibrain-platform-api/v1.0/docs/capabilities-with-media-via-json-config

        Args:
          lang: The language of the output. If not provided, the language used will be the same
              as the language of the text provided.

          variable1_description: The description of the variable.

          variable1_name: The name of the variable to be extracted.

          variable1_type: Text Extraction Request Variable Type.

          variable2_description: The description of the variable.

          variable2_name: The name of the variable to be extracted.

          variable2_type: Text Extraction Request Variable Type.

          variable3_description: The description of the variable.

          variable3_name: The name of the variable to be extracted.

          variable3_type: Text Extraction Request Variable Type.

          variable4_description: The description of the variable.

          variable4_name: The name of the variable to be extracted.

          variable4_type: Text Extraction Request Variable Type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "lang": lang,
                "variable1_description": variable1_description,
                "variable1_name": variable1_name,
                "variable1_type": variable1_type,
                "variable2_description": variable2_description,
                "variable2_name": variable2_name,
                "variable2_type": variable2_type,
                "variable3_description": variable3_description,
                "variable3_name": variable3_name,
                "variable3_type": variable3_type,
                "variable4_description": variable4_description,
                "variable4_name": variable4_name,
                "variable4_type": variable4_type,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/capabilities/extract/media",
            body=maybe_transform(body, media_extract_params.MediaExtractParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TextExtractor,
        )

    async def summarize(
        self,
        *,
        file: FileTypes,
        format: Literal["paragraph", "bullet"] | NotGiven = NOT_GIVEN,
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | NotGiven = NOT_GIVEN,
        length: Literal["short", "medium", "long"] | NotGiven = NOT_GIVEN,
        summary_hint: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TextSummary:
        """Summarizes a media file.

        This endpoint supports an additional field `model`
        documented in this url:
        https://dash.readme.com/project/clibrain-platform-api/v1.0/docs/capabilities-with-media-via-json-config

        Args:
          format: Text Summary Request Format.

          lang: The language of the output. If not provided, the language used will be the same
              as the language of the text provided.

          length: Text Summary Request Length.

          summary_hint: A hint to the summarization. This can be used to provide a specific

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "format": format,
                "lang": lang,
                "length": length,
                "summary_hint": summary_hint,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/capabilities/summarize/media",
            body=maybe_transform(body, media_summarize_params.MediaSummarizeParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TextSummary,
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
