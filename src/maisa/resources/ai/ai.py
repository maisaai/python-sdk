# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from .media import (
    Media,
    AsyncMedia,
    MediaWithRawResponse,
    AsyncMediaWithRawResponse,
    MediaWithStreamingResponse,
    AsyncMediaWithStreamingResponse,
)
from ...types import (
    AICompareResponse,
    AIExtractResponse,
    AISummarizeResponse,
    ai_compare_params,
    ai_extract_params,
    ai_summarize_params,
)
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

__all__ = ["AI", "AsyncAI"]


class AI(SyncAPIResource):
    @cached_property
    def media(self) -> Media:
        return Media(self._client)

    @cached_property
    def with_raw_response(self) -> AIWithRawResponse:
        return AIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AIWithStreamingResponse:
        return AIWithStreamingResponse(self)

    def compare(
        self,
        *,
        text1: str,
        text2: str,
        variables: Dict[str, ai_compare_params.Variables],
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AICompareResponse:
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
            "/v1/ai/compare",
            body=maybe_transform(
                {
                    "text1": text1,
                    "text2": text2,
                    "variables": variables,
                    "lang": lang,
                    "prompt": prompt,
                },
                ai_compare_params.AICompareParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICompareResponse,
        )

    def extract(
        self,
        *,
        text: str,
        variables: Dict[str, ai_extract_params.Variables],
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIExtractResponse:
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
            "/v1/ai/extract",
            body=maybe_transform(
                {
                    "text": text,
                    "variables": variables,
                    "lang": lang,
                },
                ai_extract_params.AIExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIExtractResponse,
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
    ) -> AISummarizeResponse:
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
            "/v1/ai/summarize",
            body=maybe_transform(
                {
                    "text": text,
                    "format": format,
                    "lang": lang,
                    "length": length,
                    "summary_hint": summary_hint,
                },
                ai_summarize_params.AISummarizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISummarizeResponse,
        )


class AsyncAI(AsyncAPIResource):
    @cached_property
    def media(self) -> AsyncMedia:
        return AsyncMedia(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAIWithRawResponse:
        return AsyncAIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAIWithStreamingResponse:
        return AsyncAIWithStreamingResponse(self)

    async def compare(
        self,
        *,
        text1: str,
        text2: str,
        variables: Dict[str, ai_compare_params.Variables],
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AICompareResponse:
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
            "/v1/ai/compare",
            body=maybe_transform(
                {
                    "text1": text1,
                    "text2": text2,
                    "variables": variables,
                    "lang": lang,
                    "prompt": prompt,
                },
                ai_compare_params.AICompareParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICompareResponse,
        )

    async def extract(
        self,
        *,
        text: str,
        variables: Dict[str, ai_extract_params.Variables],
        lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIExtractResponse:
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
            "/v1/ai/extract",
            body=maybe_transform(
                {
                    "text": text,
                    "variables": variables,
                    "lang": lang,
                },
                ai_extract_params.AIExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIExtractResponse,
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
    ) -> AISummarizeResponse:
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
            "/v1/ai/summarize",
            body=maybe_transform(
                {
                    "text": text,
                    "format": format,
                    "lang": lang,
                    "length": length,
                    "summary_hint": summary_hint,
                },
                ai_summarize_params.AISummarizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISummarizeResponse,
        )


class AIWithRawResponse:
    def __init__(self, ai: AI) -> None:
        self._ai = ai

        self.compare = to_raw_response_wrapper(
            ai.compare,
        )
        self.extract = to_raw_response_wrapper(
            ai.extract,
        )
        self.summarize = to_raw_response_wrapper(
            ai.summarize,
        )

    @cached_property
    def media(self) -> MediaWithRawResponse:
        return MediaWithRawResponse(self._ai.media)


class AsyncAIWithRawResponse:
    def __init__(self, ai: AsyncAI) -> None:
        self._ai = ai

        self.compare = async_to_raw_response_wrapper(
            ai.compare,
        )
        self.extract = async_to_raw_response_wrapper(
            ai.extract,
        )
        self.summarize = async_to_raw_response_wrapper(
            ai.summarize,
        )

    @cached_property
    def media(self) -> AsyncMediaWithRawResponse:
        return AsyncMediaWithRawResponse(self._ai.media)


class AIWithStreamingResponse:
    def __init__(self, ai: AI) -> None:
        self._ai = ai

        self.compare = to_streamed_response_wrapper(
            ai.compare,
        )
        self.extract = to_streamed_response_wrapper(
            ai.extract,
        )
        self.summarize = to_streamed_response_wrapper(
            ai.summarize,
        )

    @cached_property
    def media(self) -> MediaWithStreamingResponse:
        return MediaWithStreamingResponse(self._ai.media)


class AsyncAIWithStreamingResponse:
    def __init__(self, ai: AsyncAI) -> None:
        self._ai = ai

        self.compare = async_to_streamed_response_wrapper(
            ai.compare,
        )
        self.extract = async_to_streamed_response_wrapper(
            ai.extract,
        )
        self.summarize = async_to_streamed_response_wrapper(
            ai.summarize,
        )

    @cached_property
    def media(self) -> AsyncMediaWithStreamingResponse:
        return AsyncMediaWithStreamingResponse(self._ai.media)
