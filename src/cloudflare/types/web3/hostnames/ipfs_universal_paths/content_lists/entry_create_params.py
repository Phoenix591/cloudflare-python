# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EntryCreateParams"]


class EntryCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Specify the identifier of the hostname."""

    content: Required[str]
    """Specify the CID or content path of content to block."""

    type: Required[Literal["cid", "content_path"]]
    """Specify the type of content list entry to block."""

    description: str
    """Specify an optional description of the content list entry."""
