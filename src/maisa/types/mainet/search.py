# File generated from our OpenAPI spec by Stainless.

from typing import List

from ..._models import BaseModel

__all__ = ["Search", "Doc"]


class Doc(BaseModel):
    id: str
    """The id of the document."""

    content: str
    """The content of the document."""

    source: str
    """The source of the document."""


class Search(BaseModel):
    docs: List[Doc]
    """The list of documents found."""
