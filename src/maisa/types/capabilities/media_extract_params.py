# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import FileTypes

__all__ = ["MediaExtractParams"]


class MediaExtractParams(TypedDict, total=False):
    file: Required[FileTypes]

    lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"]
    """The language of the output.

    If not provided, the language used will be the same as the language of the text
    provided.
    """

    variable1_description: str
    """The description of the variable."""

    variable1_name: str
    """The name of the variable to be extracted."""

    variable1_type: Literal["string", "number", "date", "boolean"]
    """Text Extraction Request Variable Type."""

    variable2_description: str
    """The description of the variable."""

    variable2_name: str
    """The name of the variable to be extracted."""

    variable2_type: Literal["string", "number", "date", "boolean"]
    """Text Extraction Request Variable Type."""

    variable3_description: str
    """The description of the variable."""

    variable3_name: str
    """The name of the variable to be extracted."""

    variable3_type: Literal["string", "number", "date", "boolean"]
    """Text Extraction Request Variable Type."""

    variable4_description: str
    """The description of the variable."""

    variable4_name: str
    """The name of the variable to be extracted."""

    variable4_type: Literal["string", "number", "date", "boolean"]
    """Text Extraction Request Variable Type."""
