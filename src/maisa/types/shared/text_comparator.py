# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["TextComparator"]


class TextComparator(BaseModel):
    """Texts Comparator Response."""

    extracted_data: object
    """The extracted data from the text."""
