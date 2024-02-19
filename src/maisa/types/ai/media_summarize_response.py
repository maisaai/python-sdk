# File generated from our OpenAPI spec by Stainless.

from ..._models import BaseModel

__all__ = ["MediaSummarizeResponse"]


class MediaSummarizeResponse(BaseModel):
    summary: str
    """The summarized version of the provided text."""
