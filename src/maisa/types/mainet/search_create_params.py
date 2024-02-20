# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SearchCreateParams"]


class SearchCreateParams(TypedDict, total=False):
    text: Required[str]
    """The text or query to search for."""
