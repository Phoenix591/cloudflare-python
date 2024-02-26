# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["QueueCreateParams"]


class QueueCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    body: Required[object]