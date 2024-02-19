# File generated from our OpenAPI spec by Stainless.

from typing import List

from .._models import BaseModel

__all__ = ["ModelRerankResponse"]


class ModelRerankResponse(BaseModel):
    sorted_sentences: List[str]
