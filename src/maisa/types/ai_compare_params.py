# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AICompareParams", "Variables"]


class AICompareParams(TypedDict, total=False):
    text1: Required[str]
    """The text to be compared."""

    text2: Required[str]
    """The text to be compared with."""

    variables: Required[Dict[str, Variables]]
    """The variables to be compared."""

    lang: Literal["en", "es", "pt", "fr", "de", "it", "nl", "sv", "pl", "ro"]
    """The language of the output.

    If not provided, the language used will be the same as the language of the text
    provided.
    """

    prompt: str
    """The prompt to be used as criteria to compare the texts."""


class Variables(TypedDict, total=False):
    description: Required[str]

    type: Required[Literal["string", "number", "date", "boolean"]]
    """Text Extraction Request Variable Type."""
