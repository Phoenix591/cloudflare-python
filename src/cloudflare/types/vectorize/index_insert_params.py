# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["IndexInsertParams"]


class IndexInsertParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    body: Required[FileTypes]
    """ndjson file containing vectors to insert."""
