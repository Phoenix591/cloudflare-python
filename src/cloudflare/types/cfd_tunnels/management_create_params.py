# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ManagementCreateParams"]


class ManagementCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    resources: Required[List[Literal["logs"]]]
