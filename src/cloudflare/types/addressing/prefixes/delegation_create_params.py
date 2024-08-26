# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["DelegationCreateParams"]

class DelegationCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    cidr: Required[str]
    """IP Prefix in Classless Inter-Domain Routing format."""

    delegated_account_id: Required[str]
    """Account identifier for the account to which prefix is being delegated."""