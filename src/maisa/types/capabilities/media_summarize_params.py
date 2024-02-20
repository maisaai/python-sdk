# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import FileTypes

__all__ = ["MediaSummarizeParams"]


class MediaSummarizeParams(TypedDict, total=False):
    file: Required[FileTypes]

    format: Literal["paragraph", "bullet"]
    """Text Summary Request Format."""

    lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"]
    """The language of the output.

    If not provided, the language used will be the same as the language of the text
    provided.
    """

    length: Literal["short", "medium", "long"]
    """Text Summary Request Length."""

    summary_hint: str
    """A hint to the summarization. This can be used to provide a specific"""
