# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import Optional, List

from datetime import datetime

from .record_metadata import RecordMetadata

from .record_tags import RecordTags

from .ttl import TTL

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["AAAARecord"]

class AAAARecord(BaseModel):
    content: str
    """A valid IPv6 address."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["AAAA"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified."""

    created_on: Optional[datetime] = None
    """When the record was created."""

    meta: Optional[RecordMetadata] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    proxied: Optional[bool] = None
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: Optional[List[RecordTags]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified."""

    ttl: Optional[TTL] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """