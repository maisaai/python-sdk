# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .from_pdf import (
    FromPdfResource,
    AsyncFromPdfResource,
    FromPdfResourceWithRawResponse,
    AsyncFromPdfResourceWithRawResponse,
    FromPdfResourceWithStreamingResponse,
    AsyncFromPdfResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .from_docx import (
    FromDocxResource,
    AsyncFromDocxResource,
    FromDocxResourceWithRawResponse,
    AsyncFromDocxResourceWithRawResponse,
    FromDocxResourceWithStreamingResponse,
    AsyncFromDocxResourceWithStreamingResponse,
)
from .from_html import (
    FromHTMLResource,
    AsyncFromHTMLResource,
    FromHTMLResourceWithRawResponse,
    AsyncFromHTMLResourceWithRawResponse,
    FromHTMLResourceWithStreamingResponse,
    AsyncFromHTMLResourceWithStreamingResponse,
)
from .from_audio import (
    FromAudioResource,
    AsyncFromAudioResource,
    FromAudioResourceWithRawResponse,
    AsyncFromAudioResourceWithRawResponse,
    FromAudioResourceWithStreamingResponse,
    AsyncFromAudioResourceWithStreamingResponse,
)
from .from_image import (
    FromImageResource,
    AsyncFromImageResource,
    FromImageResourceWithRawResponse,
    AsyncFromImageResourceWithRawResponse,
    FromImageResourceWithStreamingResponse,
    AsyncFromImageResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["FileInterpreterResource", "AsyncFileInterpreterResource"]


class FileInterpreterResource(SyncAPIResource):
    @cached_property
    def from_pdf(self) -> FromPdfResource:
        return FromPdfResource(self._client)

    @cached_property
    def from_docx(self) -> FromDocxResource:
        return FromDocxResource(self._client)

    @cached_property
    def from_html(self) -> FromHTMLResource:
        return FromHTMLResource(self._client)

    @cached_property
    def from_image(self) -> FromImageResource:
        return FromImageResource(self._client)

    @cached_property
    def from_audio(self) -> FromAudioResource:
        return FromAudioResource(self._client)

    @cached_property
    def with_raw_response(self) -> FileInterpreterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/maisaai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return FileInterpreterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileInterpreterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/maisaai/python-sdk#with_streaming_response
        """
        return FileInterpreterResourceWithStreamingResponse(self)


class AsyncFileInterpreterResource(AsyncAPIResource):
    @cached_property
    def from_pdf(self) -> AsyncFromPdfResource:
        return AsyncFromPdfResource(self._client)

    @cached_property
    def from_docx(self) -> AsyncFromDocxResource:
        return AsyncFromDocxResource(self._client)

    @cached_property
    def from_html(self) -> AsyncFromHTMLResource:
        return AsyncFromHTMLResource(self._client)

    @cached_property
    def from_image(self) -> AsyncFromImageResource:
        return AsyncFromImageResource(self._client)

    @cached_property
    def from_audio(self) -> AsyncFromAudioResource:
        return AsyncFromAudioResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFileInterpreterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/maisaai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFileInterpreterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileInterpreterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/maisaai/python-sdk#with_streaming_response
        """
        return AsyncFileInterpreterResourceWithStreamingResponse(self)


class FileInterpreterResourceWithRawResponse:
    def __init__(self, file_interpreter: FileInterpreterResource) -> None:
        self._file_interpreter = file_interpreter

    @cached_property
    def from_pdf(self) -> FromPdfResourceWithRawResponse:
        return FromPdfResourceWithRawResponse(self._file_interpreter.from_pdf)

    @cached_property
    def from_docx(self) -> FromDocxResourceWithRawResponse:
        return FromDocxResourceWithRawResponse(self._file_interpreter.from_docx)

    @cached_property
    def from_html(self) -> FromHTMLResourceWithRawResponse:
        return FromHTMLResourceWithRawResponse(self._file_interpreter.from_html)

    @cached_property
    def from_image(self) -> FromImageResourceWithRawResponse:
        return FromImageResourceWithRawResponse(self._file_interpreter.from_image)

    @cached_property
    def from_audio(self) -> FromAudioResourceWithRawResponse:
        return FromAudioResourceWithRawResponse(self._file_interpreter.from_audio)


class AsyncFileInterpreterResourceWithRawResponse:
    def __init__(self, file_interpreter: AsyncFileInterpreterResource) -> None:
        self._file_interpreter = file_interpreter

    @cached_property
    def from_pdf(self) -> AsyncFromPdfResourceWithRawResponse:
        return AsyncFromPdfResourceWithRawResponse(self._file_interpreter.from_pdf)

    @cached_property
    def from_docx(self) -> AsyncFromDocxResourceWithRawResponse:
        return AsyncFromDocxResourceWithRawResponse(self._file_interpreter.from_docx)

    @cached_property
    def from_html(self) -> AsyncFromHTMLResourceWithRawResponse:
        return AsyncFromHTMLResourceWithRawResponse(self._file_interpreter.from_html)

    @cached_property
    def from_image(self) -> AsyncFromImageResourceWithRawResponse:
        return AsyncFromImageResourceWithRawResponse(self._file_interpreter.from_image)

    @cached_property
    def from_audio(self) -> AsyncFromAudioResourceWithRawResponse:
        return AsyncFromAudioResourceWithRawResponse(self._file_interpreter.from_audio)


class FileInterpreterResourceWithStreamingResponse:
    def __init__(self, file_interpreter: FileInterpreterResource) -> None:
        self._file_interpreter = file_interpreter

    @cached_property
    def from_pdf(self) -> FromPdfResourceWithStreamingResponse:
        return FromPdfResourceWithStreamingResponse(self._file_interpreter.from_pdf)

    @cached_property
    def from_docx(self) -> FromDocxResourceWithStreamingResponse:
        return FromDocxResourceWithStreamingResponse(self._file_interpreter.from_docx)

    @cached_property
    def from_html(self) -> FromHTMLResourceWithStreamingResponse:
        return FromHTMLResourceWithStreamingResponse(self._file_interpreter.from_html)

    @cached_property
    def from_image(self) -> FromImageResourceWithStreamingResponse:
        return FromImageResourceWithStreamingResponse(self._file_interpreter.from_image)

    @cached_property
    def from_audio(self) -> FromAudioResourceWithStreamingResponse:
        return FromAudioResourceWithStreamingResponse(self._file_interpreter.from_audio)


class AsyncFileInterpreterResourceWithStreamingResponse:
    def __init__(self, file_interpreter: AsyncFileInterpreterResource) -> None:
        self._file_interpreter = file_interpreter

    @cached_property
    def from_pdf(self) -> AsyncFromPdfResourceWithStreamingResponse:
        return AsyncFromPdfResourceWithStreamingResponse(self._file_interpreter.from_pdf)

    @cached_property
    def from_docx(self) -> AsyncFromDocxResourceWithStreamingResponse:
        return AsyncFromDocxResourceWithStreamingResponse(self._file_interpreter.from_docx)

    @cached_property
    def from_html(self) -> AsyncFromHTMLResourceWithStreamingResponse:
        return AsyncFromHTMLResourceWithStreamingResponse(self._file_interpreter.from_html)

    @cached_property
    def from_image(self) -> AsyncFromImageResourceWithStreamingResponse:
        return AsyncFromImageResourceWithStreamingResponse(self._file_interpreter.from_image)

    @cached_property
    def from_audio(self) -> AsyncFromAudioResourceWithStreamingResponse:
        return AsyncFromAudioResourceWithStreamingResponse(self._file_interpreter.from_audio)
