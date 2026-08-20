# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from ..._files import deepcopy_with_paths
from ..._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
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
from ...types.capabilities import media_compare_params, media_extract_params, media_summarize_params
from ...types.shared.text_summary import TextSummary
from ...types.shared.text_extractor import TextExtractor
from ...types.shared.text_comparator import TextComparator

__all__ = ["MediaResource", "AsyncMediaResource"]


class MediaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/maisaai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return MediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/maisaai/python-sdk#with_streaming_response
        """
        return MediaResourceWithStreamingResponse(self)

    def compare(
        self,
        *,
        file1: FileTypes,
        file2: FileTypes,
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | Omit = omit,
        prompt: str | Omit = omit,
        variable1_description: str | Omit = omit,
        variable1_name: str | Omit = omit,
        variable1_type: Literal["string", "number", "date", "boolean"] | Omit = omit,
        variable2_description: str | Omit = omit,
        variable2_name: str | Omit = omit,
        variable2_type: Literal["string", "number", "date", "boolean"] | Omit = omit,
        variable3_description: str | Omit = omit,
        variable3_name: str | Omit = omit,
        variable3_type: Literal["string", "number", "date", "boolean"] | Omit = omit,
        variable4_description: str | Omit = omit,
        variable4_name: str | Omit = omit,
        variable4_type: Literal["string", "number", "date", "boolean"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TextComparator:
        """Compare extracts of media files based on a specific data.

        This endpoint supports
        an additional field `model` documented in this url:
        https://docs.maisa.ai/docs/capabilities-with-media-via-json-config

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
        body = deepcopy_with_paths(
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
            },
            [["file1"], ["file2"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file1"], ["file2"]])
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
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | Omit = omit,
        variable1_description: str | Omit = omit,
        variable1_name: str | Omit = omit,
        variable1_type: Literal["string", "number", "date", "boolean"] | Omit = omit,
        variable2_description: str | Omit = omit,
        variable2_name: str | Omit = omit,
        variable2_type: Literal["string", "number", "date", "boolean"] | Omit = omit,
        variable3_description: str | Omit = omit,
        variable3_name: str | Omit = omit,
        variable3_type: Literal["string", "number", "date", "boolean"] | Omit = omit,
        variable4_description: str | Omit = omit,
        variable4_name: str | Omit = omit,
        variable4_type: Literal["string", "number", "date", "boolean"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TextExtractor:
        """Extracts structured data from a file.

        The text is analyzed and the variables are
        extracted. This endpoint supports an additional field `model` documented in this
        url: https://docs.maisa.ai/docs/capabilities-with-media-via-json-config

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
        body = deepcopy_with_paths(
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
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
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
        format: Literal["paragraph", "bullet"] | Omit = omit,
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | Omit = omit,
        length: Literal["short", "medium", "long"] | Omit = omit,
        summary_hint: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TextSummary:
        """Summarizes a media file.

        This endpoint supports an additional field `model`
        documented in this url:
        https://docs.maisa.ai/docs/capabilities-with-media-via-json-config

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
        body = deepcopy_with_paths(
            {
                "file": file,
                "format": format,
                "lang": lang,
                "length": length,
                "summary_hint": summary_hint,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
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


class AsyncMediaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/maisaai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/maisaai/python-sdk#with_streaming_response
        """
        return AsyncMediaResourceWithStreamingResponse(self)

    async def compare(
        self,
        *,
        file1: FileTypes,
        file2: FileTypes,
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | Omit = omit,
        prompt: str | Omit = omit,
        variable1_description: str | Omit = omit,
        variable1_name: str | Omit = omit,
        variable1_type: Literal["string", "number", "date", "boolean"] | Omit = omit,
        variable2_description: str | Omit = omit,
        variable2_name: str | Omit = omit,
        variable2_type: Literal["string", "number", "date", "boolean"] | Omit = omit,
        variable3_description: str | Omit = omit,
        variable3_name: str | Omit = omit,
        variable3_type: Literal["string", "number", "date", "boolean"] | Omit = omit,
        variable4_description: str | Omit = omit,
        variable4_name: str | Omit = omit,
        variable4_type: Literal["string", "number", "date", "boolean"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TextComparator:
        """Compare extracts of media files based on a specific data.

        This endpoint supports
        an additional field `model` documented in this url:
        https://docs.maisa.ai/docs/capabilities-with-media-via-json-config

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
        body = deepcopy_with_paths(
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
            },
            [["file1"], ["file2"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file1"], ["file2"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/capabilities/compare/media",
            body=await async_maybe_transform(body, media_compare_params.MediaCompareParams),
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
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | Omit = omit,
        variable1_description: str | Omit = omit,
        variable1_name: str | Omit = omit,
        variable1_type: Literal["string", "number", "date", "boolean"] | Omit = omit,
        variable2_description: str | Omit = omit,
        variable2_name: str | Omit = omit,
        variable2_type: Literal["string", "number", "date", "boolean"] | Omit = omit,
        variable3_description: str | Omit = omit,
        variable3_name: str | Omit = omit,
        variable3_type: Literal["string", "number", "date", "boolean"] | Omit = omit,
        variable4_description: str | Omit = omit,
        variable4_name: str | Omit = omit,
        variable4_type: Literal["string", "number", "date", "boolean"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TextExtractor:
        """Extracts structured data from a file.

        The text is analyzed and the variables are
        extracted. This endpoint supports an additional field `model` documented in this
        url: https://docs.maisa.ai/docs/capabilities-with-media-via-json-config

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
        body = deepcopy_with_paths(
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
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/capabilities/extract/media",
            body=await async_maybe_transform(body, media_extract_params.MediaExtractParams),
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
        format: Literal["paragraph", "bullet"] | Omit = omit,
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | Omit = omit,
        length: Literal["short", "medium", "long"] | Omit = omit,
        summary_hint: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TextSummary:
        """Summarizes a media file.

        This endpoint supports an additional field `model`
        documented in this url:
        https://docs.maisa.ai/docs/capabilities-with-media-via-json-config

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
        body = deepcopy_with_paths(
            {
                "file": file,
                "format": format,
                "lang": lang,
                "length": length,
                "summary_hint": summary_hint,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/capabilities/summarize/media",
            body=await async_maybe_transform(body, media_summarize_params.MediaSummarizeParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TextSummary,
        )


class MediaResourceWithRawResponse:
    def __init__(self, media: MediaResource) -> None:
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


class AsyncMediaResourceWithRawResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
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


class MediaResourceWithStreamingResponse:
    def __init__(self, media: MediaResource) -> None:
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


class AsyncMediaResourceWithStreamingResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
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
