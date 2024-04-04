# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .role import Role
from ..._models import BaseModel

__all__ = ["Member", "User"]


class User(BaseModel):
    email: str
    """The contact email address of the user."""

    id: Optional[str] = None
    """Identifier"""

    first_name: Optional[str] = None
    """User's first name"""

    last_name: Optional[str] = None
    """User's last name"""

    two_factor_authentication_enabled: Optional[bool] = None
    """Indicates whether two-factor authentication is enabled for the user account.

    Does not apply to API authentication.
    """


class Member(BaseModel):
    id: str
    """Membership identifier tag."""

    roles: List[Role]
    """Roles assigned to this member."""

    status: object

    user: User