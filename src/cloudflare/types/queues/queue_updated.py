# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["QueueUpdated"]


class QueueUpdated(BaseModel):
    created_on: Optional[object] = None

    modified_on: Optional[object] = None

    queue_id: Optional[str] = None

    queue_name: Optional[str] = None
