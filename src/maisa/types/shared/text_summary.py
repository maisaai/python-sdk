# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["TextSummary"]


class TextSummary(BaseModel):
    """Text Summary Request."""

    summary: str
    """The summarized version of the provided text."""
