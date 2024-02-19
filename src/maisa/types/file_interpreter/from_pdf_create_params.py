# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["FromPdfCreateParams"]


class FromPdfCreateParams(TypedDict, total=False):
    file: Required[FileTypes]

    max_pages: Optional[int]
