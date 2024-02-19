# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, TypedDict

from ..._types import FileTypes

__all__ = ["MediaCompareParams", "Model", "ModelVariables", "ModelMetadataMedia1", "ModelMetadataMedia2"]


class MediaCompareParams(TypedDict, total=False):
    file1: Required[FileTypes]

    file2: Required[FileTypes]

    model: Required[Model]
    """Media Comparator Request."""


class ModelVariables(TypedDict, total=False):
    description: Required[str]

    type: Required[Literal["string", "number", "date", "boolean"]]
    """Text Extraction Request Variable Type."""


class ModelMetadataMedia1(TypedDict, total=False):
    keywords: List[str]
    """
    When uploading an audio file, this list is for uncommon proper nouns or other
    words to transcribe that could not be part of the model's vocabulary
    """


class ModelMetadataMedia2(TypedDict, total=False):
    keywords: List[str]
    """
    When uploading an audio file, this list is for uncommon proper nouns or other
    words to transcribe that could not be part of the model's vocabulary
    """


class Model(TypedDict, total=False):
    variables: Required[Dict[str, ModelVariables]]
    """The variables to be compared."""

    lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"]
    """The language of the output.

    If not provided, the language used will be the same as the language of the text
    provided.
    """

    metadata_media1: ModelMetadataMedia1
    """Metadata about the media file 1 used in the media file comparation."""

    metadata_media2: ModelMetadataMedia2
    """Metadata about the media file 2 used in the media file comparation."""

    prompt: str
    """The prompt to be used as criteria to compare the texts."""
