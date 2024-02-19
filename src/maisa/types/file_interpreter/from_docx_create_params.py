# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["FromDocxCreateParams"]


class FromDocxCreateParams(TypedDict, total=False):
    file: Required[FileTypes]
