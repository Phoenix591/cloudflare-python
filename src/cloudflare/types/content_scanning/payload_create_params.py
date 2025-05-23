# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PayloadCreateParams", "Body"]


class PayloadCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Defines an identifier."""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    payload: Required[str]
    """Defines the ruleset expression to use in matching content objects."""
