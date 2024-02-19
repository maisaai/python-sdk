# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel

__all__ = ["AIExtractResponse"]


class AIExtractResponse(BaseModel):
    extracted_data: object
    """The extracted data from the text."""
