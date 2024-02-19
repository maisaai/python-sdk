# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from ..._types import FileTypes

__all__ = ["MediaSummarizeParams", "Model", "ModelMetadata"]


class MediaSummarizeParams(TypedDict, total=False):
    file: Required[FileTypes]

    model: Required[Model]
    """Media Summary Request."""


class ModelMetadata(TypedDict, total=False):
    keywords: List[str]
    """
    When uploading an audio file, this list is for uncommon proper nouns or other
    words to transcribe that could not be part of the model's vocabulary
    """


class Model(TypedDict, total=False):
    format: Literal["paragraph", "bullet"]
    """Text Summary Request Format."""

    lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"]
    """The language of the output.

    If not provided, the language used will be the same as the language of the text
    provided.
    """

    length: Literal["short", "medium", "long"]
    """Text Summary Request Length."""

    metadata: ModelMetadata
    """Metadata used in the media file sumarization."""

    summary_hint: str
    """A hint to the summarization.

    This can be used to provide a specific summary if the user has a specific
    summary in mind
    """
