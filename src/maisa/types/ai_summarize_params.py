# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AISummarizeParams"]


class AISummarizeParams(TypedDict, total=False):
    text: Required[str]
    """The text to be summarized."""

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
    """A hint to the summarization.

    This can be used to provide a specific summary if the user has a specific
    summary in mind.
    """
