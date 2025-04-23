# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from .media import (
    MediaResource,
    AsyncMediaResource,
    MediaResourceWithRawResponse,
    AsyncMediaResourceWithRawResponse,
    MediaResourceWithStreamingResponse,
    AsyncMediaResourceWithStreamingResponse,
)
from ...types import capability_compare_params, capability_extract_params, capability_summarize_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.shared.text_summary import TextSummary
from ...types.shared.text_extractor import TextExtractor
from ...types.shared.text_comparator import TextComparator

__all__ = ["CapabilitiesResource", "AsyncCapabilitiesResource"]


class CapabilitiesResource(SyncAPIResource):
    @cached_property
    def media(self) -> MediaResource:
        return MediaResource(self._client)

    @cached_property
    def with_raw_response(self) -> CapabilitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/maisaai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return CapabilitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CapabilitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/maisaai/python-sdk#with_streaming_response
        """
        return CapabilitiesResourceWithStreamingResponse(self)

    def compare(
        self,
        *,
        text1: str,
        text2: str,
        variables: Dict[str, capability_compare_params.Variables],
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TextComparator:
        """
        Compare extracts of text based on a specific data.

        Args:
          text1: The text to be compared.

          text2: The text to be compared with.

          variables: The variables to be compared.

          lang: The language of the output. If not provided, the language used will be the same
              as the language of the text provided.

          prompt: The prompt to be used as criteria to compare the texts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/capabilities/compare",
            body=maybe_transform(
                {
                    "text1": text1,
                    "text2": text2,
                    "variables": variables,
                    "lang": lang,
                    "prompt": prompt,
                },
                capability_compare_params.CapabilityCompareParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TextComparator,
        )

    def extract(
        self,
        *,
        text: str,
        variables: Dict[str, capability_extract_params.Variables],
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TextExtractor:
        """Extracts structured data from text.

        The text is analyzed and the variables are
        extracted.

        Args:
          text: The text to be extracted from.

          variables: The variables to be extracted from the text.

          lang: The language of the output. If not provided, the language used will be the same
              as the language of the text provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/capabilities/extract",
            body=maybe_transform(
                {
                    "text": text,
                    "variables": variables,
                    "lang": lang,
                },
                capability_extract_params.CapabilityExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TextExtractor,
        )

    def summarize(
        self,
        *,
        text: str,
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
        """Summarizes a text.

        The summary is returned in the format and length specified.

        Args:
          text: The text to be summarized.

          format: Text Summary Request Format.

          lang: The language of the output. If not provided, the language used will be the same
              as the language of the text provided.

          length: Text Summary Request Length.

          summary_hint: A hint to the summarization. This can be used to provide a specific summary if
              the user has a specific summary in mind.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/capabilities/summarize",
            body=maybe_transform(
                {
                    "text": text,
                    "format": format,
                    "lang": lang,
                    "length": length,
                    "summary_hint": summary_hint,
                },
                capability_summarize_params.CapabilitySummarizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TextSummary,
        )


class AsyncCapabilitiesResource(AsyncAPIResource):
    @cached_property
    def media(self) -> AsyncMediaResource:
        return AsyncMediaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCapabilitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/maisaai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCapabilitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCapabilitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/maisaai/python-sdk#with_streaming_response
        """
        return AsyncCapabilitiesResourceWithStreamingResponse(self)

    async def compare(
        self,
        *,
        text1: str,
        text2: str,
        variables: Dict[str, capability_compare_params.Variables],
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TextComparator:
        """
        Compare extracts of text based on a specific data.

        Args:
          text1: The text to be compared.

          text2: The text to be compared with.

          variables: The variables to be compared.

          lang: The language of the output. If not provided, the language used will be the same
              as the language of the text provided.

          prompt: The prompt to be used as criteria to compare the texts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/capabilities/compare",
            body=await async_maybe_transform(
                {
                    "text1": text1,
                    "text2": text2,
                    "variables": variables,
                    "lang": lang,
                    "prompt": prompt,
                },
                capability_compare_params.CapabilityCompareParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TextComparator,
        )

    async def extract(
        self,
        *,
        text: str,
        variables: Dict[str, capability_extract_params.Variables],
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TextExtractor:
        """Extracts structured data from text.

        The text is analyzed and the variables are
        extracted.

        Args:
          text: The text to be extracted from.

          variables: The variables to be extracted from the text.

          lang: The language of the output. If not provided, the language used will be the same
              as the language of the text provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/capabilities/extract",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "variables": variables,
                    "lang": lang,
                },
                capability_extract_params.CapabilityExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TextExtractor,
        )

    async def summarize(
        self,
        *,
        text: str,
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
        """Summarizes a text.

        The summary is returned in the format and length specified.

        Args:
          text: The text to be summarized.

          format: Text Summary Request Format.

          lang: The language of the output. If not provided, the language used will be the same
              as the language of the text provided.

          length: Text Summary Request Length.

          summary_hint: A hint to the summarization. This can be used to provide a specific summary if
              the user has a specific summary in mind.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/capabilities/summarize",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "format": format,
                    "lang": lang,
                    "length": length,
                    "summary_hint": summary_hint,
                },
                capability_summarize_params.CapabilitySummarizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TextSummary,
        )


class CapabilitiesResourceWithRawResponse:
    def __init__(self, capabilities: CapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.compare = to_raw_response_wrapper(
            capabilities.compare,
        )
        self.extract = to_raw_response_wrapper(
            capabilities.extract,
        )
        self.summarize = to_raw_response_wrapper(
            capabilities.summarize,
        )

    @cached_property
    def media(self) -> MediaResourceWithRawResponse:
        return MediaResourceWithRawResponse(self._capabilities.media)


class AsyncCapabilitiesResourceWithRawResponse:
    def __init__(self, capabilities: AsyncCapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.compare = async_to_raw_response_wrapper(
            capabilities.compare,
        )
        self.extract = async_to_raw_response_wrapper(
            capabilities.extract,
        )
        self.summarize = async_to_raw_response_wrapper(
            capabilities.summarize,
        )

    @cached_property
    def media(self) -> AsyncMediaResourceWithRawResponse:
        return AsyncMediaResourceWithRawResponse(self._capabilities.media)


class CapabilitiesResourceWithStreamingResponse:
    def __init__(self, capabilities: CapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.compare = to_streamed_response_wrapper(
            capabilities.compare,
        )
        self.extract = to_streamed_response_wrapper(
            capabilities.extract,
        )
        self.summarize = to_streamed_response_wrapper(
            capabilities.summarize,
        )

    @cached_property
    def media(self) -> MediaResourceWithStreamingResponse:
        return MediaResourceWithStreamingResponse(self._capabilities.media)


class AsyncCapabilitiesResourceWithStreamingResponse:
    def __init__(self, capabilities: AsyncCapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.compare = async_to_streamed_response_wrapper(
            capabilities.compare,
        )
        self.extract = async_to_streamed_response_wrapper(
            capabilities.extract,
        )
        self.summarize = async_to_streamed_response_wrapper(
            capabilities.summarize,
        )

    @cached_property
    def media(self) -> AsyncMediaResourceWithStreamingResponse:
        return AsyncMediaResourceWithStreamingResponse(self._capabilities.media)
