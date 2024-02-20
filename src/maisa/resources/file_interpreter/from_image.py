# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Mapping, cast

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
from ...types.file_interpreter import FromImage, from_image_create_params

__all__ = ["FromImageResource", "AsyncFromImageResource"]


class FromImageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FromImageResourceWithRawResponse:
        return FromImageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FromImageResourceWithStreamingResponse:
        return FromImageResourceWithStreamingResponse(self)

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
    ) -> FromImage:
        """
        Interprets an image file and returns a description of the image.

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
            "/v1/file-interpreter/from-image",
            body=maybe_transform(body, from_image_create_params.FromImageCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FromImage,
        )


class AsyncFromImageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFromImageResourceWithRawResponse:
        return AsyncFromImageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFromImageResourceWithStreamingResponse:
        return AsyncFromImageResourceWithStreamingResponse(self)

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
    ) -> FromImage:
        """
        Interprets an image file and returns a description of the image.

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
            "/v1/file-interpreter/from-image",
            body=maybe_transform(body, from_image_create_params.FromImageCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FromImage,
        )


class FromImageResourceWithRawResponse:
    def __init__(self, from_image: FromImageResource) -> None:
        self._from_image = from_image

        self.create = to_raw_response_wrapper(
            from_image.create,
        )


class AsyncFromImageResourceWithRawResponse:
    def __init__(self, from_image: AsyncFromImageResource) -> None:
        self._from_image = from_image

        self.create = async_to_raw_response_wrapper(
            from_image.create,
        )


class FromImageResourceWithStreamingResponse:
    def __init__(self, from_image: FromImageResource) -> None:
        self._from_image = from_image

        self.create = to_streamed_response_wrapper(
            from_image.create,
        )


class AsyncFromImageResourceWithStreamingResponse:
    def __init__(self, from_image: AsyncFromImageResource) -> None:
        self._from_image = from_image

        self.create = async_to_streamed_response_wrapper(
            from_image.create,
        )
