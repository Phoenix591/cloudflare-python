# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo

__all__ = ["NetworkCreateParams"]

class NetworkCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    tunnel_id: Required[str]
    """UUID of the tunnel."""

    comment: str
    """Optional remark describing the route."""

    virtual_network_id: str
    """UUID of the virtual network."""