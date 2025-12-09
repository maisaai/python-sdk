# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["TextExtractor"]


class TextExtractor(BaseModel):
    """Text Extraction Response."""

    extracted_data: object
    """The extracted data from the text."""
