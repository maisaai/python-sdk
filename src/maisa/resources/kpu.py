# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Mapping, cast

import httpx

from ..types import KpuRunResponse, kpu_run_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)

__all__ = ["Kpu", "AsyncKpu"]


class Kpu(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KpuWithRawResponse:
        return KpuWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KpuWithStreamingResponse:
        return KpuWithStreamingResponse(self)

    def run(
        self,
        *,
        query: str,
        explain_steps: bool | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        file: List[FileTypes] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KpuRunResponse:
        """
        Executes the KPU in sync, sending the response when the KPU execution is done.

        Args:
          query: User text with the query or request to be commanded to the KPU.

          explain_steps: If true, the KPU will explain in natural language the steps of each step of each
              intent. Enabling this feature can slow down the KPU execution, and increase the
              usage metric.

          retries: Number of retries in case of failure. Retries are sequential, and each failed
              intent yields a learning for the next intent. This feature is experimental.

          file: Files to be used in the KPU execution. Files can be of any type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "query": query,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file", "<array>"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/kpu/run",
            body=maybe_transform(body, kpu_run_params.KpuRunParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "explain_steps": explain_steps,
                        "retries": retries,
                    },
                    kpu_run_params.KpuRunParams,
                ),
            ),
            cast_to=KpuRunResponse,
        )


class AsyncKpu(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKpuWithRawResponse:
        return AsyncKpuWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKpuWithStreamingResponse:
        return AsyncKpuWithStreamingResponse(self)

    async def run(
        self,
        *,
        query: str,
        explain_steps: bool | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        file: List[FileTypes] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KpuRunResponse:
        """
        Executes the KPU in sync, sending the response when the KPU execution is done.

        Args:
          query: User text with the query or request to be commanded to the KPU.

          explain_steps: If true, the KPU will explain in natural language the steps of each step of each
              intent. Enabling this feature can slow down the KPU execution, and increase the
              usage metric.

          retries: Number of retries in case of failure. Retries are sequential, and each failed
              intent yields a learning for the next intent. This feature is experimental.

          file: Files to be used in the KPU execution. Files can be of any type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "query": query,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file", "<array>"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/kpu/run",
            body=await async_maybe_transform(body, kpu_run_params.KpuRunParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "explain_steps": explain_steps,
                        "retries": retries,
                    },
                    kpu_run_params.KpuRunParams,
                ),
            ),
            cast_to=KpuRunResponse,
        )


class KpuWithRawResponse:
    def __init__(self, kpu: Kpu) -> None:
        self._kpu = kpu

        self.run = to_raw_response_wrapper(
            kpu.run,
        )


class AsyncKpuWithRawResponse:
    def __init__(self, kpu: AsyncKpu) -> None:
        self._kpu = kpu

        self.run = async_to_raw_response_wrapper(
            kpu.run,
        )


class KpuWithStreamingResponse:
    def __init__(self, kpu: Kpu) -> None:
        self._kpu = kpu

        self.run = to_streamed_response_wrapper(
            kpu.run,
        )


class AsyncKpuWithStreamingResponse:
    def __init__(self, kpu: AsyncKpu) -> None:
        self._kpu = kpu

        self.run = async_to_streamed_response_wrapper(
            kpu.run,
        )
