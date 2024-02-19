# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AIExtractParams", "Variables"]


class AIExtractParams(TypedDict, total=False):
    text: Required[str]
    """The text to be extracted from."""

    variables: Required[Dict[str, Variables]]
    """The variables to be extracted from the text."""

    lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"]
    """The language of the output.

    If not provided, the language used will be the same as the language of the text
    provided.
    """


class Variables(TypedDict, total=False):
    description: Required[str]
    """The description of the variable."""

    type: Required[Literal["string", "number", "date", "boolean"]]
    """Text Extraction Request Variable Type."""
