# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .from_pdf import (
    FromPdf,
    AsyncFromPdf,
    FromPdfWithRawResponse,
    AsyncFromPdfWithRawResponse,
    FromPdfWithStreamingResponse,
    AsyncFromPdfWithStreamingResponse,
)
from ..._compat import cached_property
from .from_docx import (
    FromDocx,
    AsyncFromDocx,
    FromDocxWithRawResponse,
    AsyncFromDocxWithRawResponse,
    FromDocxWithStreamingResponse,
    AsyncFromDocxWithStreamingResponse,
)
from .from_html import (
    FromHTML,
    AsyncFromHTML,
    FromHTMLWithRawResponse,
    AsyncFromHTMLWithRawResponse,
    FromHTMLWithStreamingResponse,
    AsyncFromHTMLWithStreamingResponse,
)
from .from_audio import (
    FromAudio,
    AsyncFromAudio,
    FromAudioWithRawResponse,
    AsyncFromAudioWithRawResponse,
    FromAudioWithStreamingResponse,
    AsyncFromAudioWithStreamingResponse,
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

__all__ = ["FileInterpreter", "AsyncFileInterpreter"]


class FileInterpreter(SyncAPIResource):
    @cached_property
    def from_pdf(self) -> FromPdf:
        return FromPdf(self._client)

    @cached_property
    def from_docx(self) -> FromDocx:
        return FromDocx(self._client)

    @cached_property
    def from_html(self) -> FromHTML:
        return FromHTML(self._client)

    @cached_property
    def from_image(self) -> FromImageResource:
        return FromImageResource(self._client)

    @cached_property
    def from_audio(self) -> FromAudio:
        return FromAudio(self._client)

    @cached_property
    def with_raw_response(self) -> FileInterpreterWithRawResponse:
        return FileInterpreterWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileInterpreterWithStreamingResponse:
        return FileInterpreterWithStreamingResponse(self)


class AsyncFileInterpreter(AsyncAPIResource):
    @cached_property
    def from_pdf(self) -> AsyncFromPdf:
        return AsyncFromPdf(self._client)

    @cached_property
    def from_docx(self) -> AsyncFromDocx:
        return AsyncFromDocx(self._client)

    @cached_property
    def from_html(self) -> AsyncFromHTML:
        return AsyncFromHTML(self._client)

    @cached_property
    def from_image(self) -> AsyncFromImageResource:
        return AsyncFromImageResource(self._client)

    @cached_property
    def from_audio(self) -> AsyncFromAudio:
        return AsyncFromAudio(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFileInterpreterWithRawResponse:
        return AsyncFileInterpreterWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileInterpreterWithStreamingResponse:
        return AsyncFileInterpreterWithStreamingResponse(self)


class FileInterpreterWithRawResponse:
    def __init__(self, file_interpreter: FileInterpreter) -> None:
        self._file_interpreter = file_interpreter

    @cached_property
    def from_pdf(self) -> FromPdfWithRawResponse:
        return FromPdfWithRawResponse(self._file_interpreter.from_pdf)

    @cached_property
    def from_docx(self) -> FromDocxWithRawResponse:
        return FromDocxWithRawResponse(self._file_interpreter.from_docx)

    @cached_property
    def from_html(self) -> FromHTMLWithRawResponse:
        return FromHTMLWithRawResponse(self._file_interpreter.from_html)

    @cached_property
    def from_image(self) -> FromImageResourceWithRawResponse:
        return FromImageResourceWithRawResponse(self._file_interpreter.from_image)

    @cached_property
    def from_audio(self) -> FromAudioWithRawResponse:
        return FromAudioWithRawResponse(self._file_interpreter.from_audio)


class AsyncFileInterpreterWithRawResponse:
    def __init__(self, file_interpreter: AsyncFileInterpreter) -> None:
        self._file_interpreter = file_interpreter

    @cached_property
    def from_pdf(self) -> AsyncFromPdfWithRawResponse:
        return AsyncFromPdfWithRawResponse(self._file_interpreter.from_pdf)

    @cached_property
    def from_docx(self) -> AsyncFromDocxWithRawResponse:
        return AsyncFromDocxWithRawResponse(self._file_interpreter.from_docx)

    @cached_property
    def from_html(self) -> AsyncFromHTMLWithRawResponse:
        return AsyncFromHTMLWithRawResponse(self._file_interpreter.from_html)

    @cached_property
    def from_image(self) -> AsyncFromImageResourceWithRawResponse:
        return AsyncFromImageResourceWithRawResponse(self._file_interpreter.from_image)

    @cached_property
    def from_audio(self) -> AsyncFromAudioWithRawResponse:
        return AsyncFromAudioWithRawResponse(self._file_interpreter.from_audio)


class FileInterpreterWithStreamingResponse:
    def __init__(self, file_interpreter: FileInterpreter) -> None:
        self._file_interpreter = file_interpreter

    @cached_property
    def from_pdf(self) -> FromPdfWithStreamingResponse:
        return FromPdfWithStreamingResponse(self._file_interpreter.from_pdf)

    @cached_property
    def from_docx(self) -> FromDocxWithStreamingResponse:
        return FromDocxWithStreamingResponse(self._file_interpreter.from_docx)

    @cached_property
    def from_html(self) -> FromHTMLWithStreamingResponse:
        return FromHTMLWithStreamingResponse(self._file_interpreter.from_html)

    @cached_property
    def from_image(self) -> FromImageResourceWithStreamingResponse:
        return FromImageResourceWithStreamingResponse(self._file_interpreter.from_image)

    @cached_property
    def from_audio(self) -> FromAudioWithStreamingResponse:
        return FromAudioWithStreamingResponse(self._file_interpreter.from_audio)


class AsyncFileInterpreterWithStreamingResponse:
    def __init__(self, file_interpreter: AsyncFileInterpreter) -> None:
        self._file_interpreter = file_interpreter

    @cached_property
    def from_pdf(self) -> AsyncFromPdfWithStreamingResponse:
        return AsyncFromPdfWithStreamingResponse(self._file_interpreter.from_pdf)

    @cached_property
    def from_docx(self) -> AsyncFromDocxWithStreamingResponse:
        return AsyncFromDocxWithStreamingResponse(self._file_interpreter.from_docx)

    @cached_property
    def from_html(self) -> AsyncFromHTMLWithStreamingResponse:
        return AsyncFromHTMLWithStreamingResponse(self._file_interpreter.from_html)

    @cached_property
    def from_image(self) -> AsyncFromImageResourceWithStreamingResponse:
        return AsyncFromImageResourceWithStreamingResponse(self._file_interpreter.from_image)

    @cached_property
    def from_audio(self) -> AsyncFromAudioWithStreamingResponse:
        return AsyncFromAudioWithStreamingResponse(self._file_interpreter.from_audio)
