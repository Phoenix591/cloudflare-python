# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["MembershipListParams", "Account"]


class MembershipListParams(TypedDict, total=False):
    account: Account

    direction: Literal["asc", "desc"]
    """Direction to order memberships."""

    name: str
    """Account name"""

    order: Literal["id", "account.name", "status"]
    """Field to order memberships by."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of memberships per page."""

    status: Literal["accepted", "pending", "rejected"]
    """Status of this membership."""


class Account(TypedDict, total=False):
    name: str
    """Account name"""