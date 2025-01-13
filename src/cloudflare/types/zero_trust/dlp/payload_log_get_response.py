# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["PayloadLogGetResponse"]


class PayloadLogGetResponse(BaseModel):
    updated_at: datetime

    public_key: Optional[str] = None
