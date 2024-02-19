# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, TypedDict

from ..._types import FileTypes

__all__ = ["MediaExtractParams", "Model", "ModelVariables", "ModelMetadata"]


class MediaExtractParams(TypedDict, total=False):
    file: Required[FileTypes]

    model: Required[Model]
    """Media Extraction Request."""


class ModelVariables(TypedDict, total=False):
    description: Required[str]
    """The description of the variable."""

    type: Required[Literal["string", "number", "date", "boolean"]]
    """Text Extraction Request Variable Type."""


class ModelMetadata(TypedDict, total=False):
    keywords: List[str]
    """
    When uploading an audio file, this list is for uncommon proper nouns or other
    words to transcribe that could not be part of the model's vocabulary
    """


class Model(TypedDict, total=False):
    variables: Required[Dict[str, ModelVariables]]
    """The variables to be extracted from the text."""

    lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"]
    """The language of the output.

    If not provided, the language used will be the same as the language of the text
    provided.
    """

    metadata: ModelMetadata
    """Metadata used in the media file data extraction."""
