# File generated from our OpenAPI spec by Stainless.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FromImage"]


class FromImage(BaseModel):
    image_caption: str = FieldInfo(alias="imageCaption")
