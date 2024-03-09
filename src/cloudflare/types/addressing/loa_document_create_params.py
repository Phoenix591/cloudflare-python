# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LOADocumentCreateParams"]


class LOADocumentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    loa_document: Required[str]
    """LOA document to upload."""