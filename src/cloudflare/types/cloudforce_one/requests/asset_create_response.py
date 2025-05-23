# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["AssetCreateResponse"]


class AssetCreateResponse(BaseModel):
    id: int
    """Asset ID."""

    name: str
    """Asset name."""

    created: Optional[datetime] = None
    """Defines the asset creation time."""

    description: Optional[str] = None
    """Asset description."""

    file_type: Optional[str] = None
    """Asset file type."""
