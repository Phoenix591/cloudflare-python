# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["CustomHostnameCustomHostnameForAZoneListCustomHostnamesParams"]


class CustomHostnameCustomHostnameForAZoneListCustomHostnamesParams(TypedDict, total=False):
    id: str
    """Hostname ID to match against.

    This ID was generated and returned during the initial custom_hostname creation.
    This parameter cannot be used with the 'hostname' parameter.
    """

    direction: Literal["asc", "desc"]
    """Direction to order hostnames."""

    hostname: str
    """Fully qualified domain name to match against.

    This parameter cannot be used with the 'id' parameter.
    """

    order: Literal["ssl", "ssl_status"]
    """Field to order hostnames by."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of hostnames per page."""

    ssl: Literal[0, 1]
    """Whether to filter hostnames based on if they have SSL enabled."""
