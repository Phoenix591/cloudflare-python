# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AssociationListResponse", "AssociationListResponseItem"]


class AssociationListResponseItem(BaseModel):
    service: Optional[str] = None
    """The service using the certificate."""

    status: Optional[str] = None
    """Certificate deployment status for the given service."""


AssociationListResponse = List[AssociationListResponseItem]
