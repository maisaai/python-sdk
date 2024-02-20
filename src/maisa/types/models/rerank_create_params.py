# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["RerankCreateParams"]


class RerankCreateParams(TypedDict, total=False):
    sentences: Required[List[str]]
    """A list of sentences to be reranked."""

    source_sentence: Required[str]
    """The sentence to be used as a reference to rerank the sentences."""
