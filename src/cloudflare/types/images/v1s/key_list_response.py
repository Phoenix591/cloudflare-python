# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["KeyListResponse", "Key"]


class Key(BaseModel):
    name: Optional[str] = None
    """Key name."""

    value: Optional[str] = None
    """Key value."""


class KeyListResponse(BaseModel):
    keys: Optional[List[Key]] = None