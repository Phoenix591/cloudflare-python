# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["PageruleCreateParams", "Action", "ActionValue", "Target", "TargetConstraint"]


class PageruleCreateParams(TypedDict, total=False):
    actions: Required[Iterable[Action]]
    """The set of actions to perform if the targets of this rule match the request.

    Actions can redirect to another URL or override settings, but not both.
    """

    targets: Required[Iterable[Target]]
    """The rule targets to evaluate on each request."""

    priority: int
    """
    The priority of the rule, used to define which Page Rule is processed over
    another. A higher number indicates a higher priority. For example, if you have a
    catch-all Page Rule (rule A: `/images/*`) but want a more specific Page Rule to
    take precedence (rule B: `/images/special/*`), specify a higher priority for
    rule B so it overrides rule A.
    """

    status: Literal["active", "disabled"]
    """The status of the Page Rule."""


class ActionValue(TypedDict, total=False):
    type: Literal["temporary", "permanent"]
    """The response type for the URL redirect."""

    url: str
    """
    The URL to redirect the request to. Notes: ${num} refers to the position of '\\**'
    in the constraint value.
    """


class Action(TypedDict, total=False):
    name: Literal["forward_url"]
    """The type of route."""

    value: ActionValue


class TargetConstraint(TypedDict, total=False):
    operator: Required[Literal["matches", "contains", "equals", "not_equal", "not_contain"]]
    """
    The matches operator can use asterisks and pipes as wildcard and 'or' operators.
    """

    value: Required[str]
    """The URL pattern to match against the current request.

    The pattern may contain up to four asterisks ('\\**') as placeholders.
    """


class Target(TypedDict, total=False):
    constraint: Required[TargetConstraint]
    """String constraint."""

    target: Required[Literal["url"]]
    """A target based on the URL of the request."""
