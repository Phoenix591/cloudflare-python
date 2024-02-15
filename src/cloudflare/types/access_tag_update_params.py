# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccessTagUpdateParams"]


class AccessTagUpdateParams(TypedDict, total=False):
    identifier: Required[str]
    """Identifier"""

    name: Required[str]
    """The name of the tag"""
