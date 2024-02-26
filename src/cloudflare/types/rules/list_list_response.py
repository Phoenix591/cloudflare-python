# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ListListResponse", "ListListResponseItem"]


class ListListResponseItem(BaseModel):
    id: str
    """The unique ID of the list."""

    created_on: str
    """The RFC 3339 timestamp of when the list was created."""

    kind: Literal["ip", "redirect", "hostname", "asn"]
    """The type of the list.

    Each type supports specific list items (IP addresses, ASNs, hostnames or
    redirects).
    """

    modified_on: str
    """The RFC 3339 timestamp of when the list was last modified."""

    name: str
    """An informative name for the list. Use this name in filter and rule expressions."""

    num_items: float
    """The number of items in the list."""

    description: Optional[str] = None
    """An informative summary of the list."""

    num_referencing_filters: Optional[float] = None
    """The number of [filters](/operations/filters-list-filters) referencing the list."""


ListListResponse = List[ListListResponseItem]