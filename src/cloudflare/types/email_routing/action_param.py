# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionParam"]


class ActionParam(TypedDict, total=False):
    type: Required[Literal["drop", "forward", "worker"]]
    """Type of supported action."""

    value: List[str]
