# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from .input_param import InputParam
from .match_item_param import MatchItemParam

__all__ = ["DevicePostureRuleParam"]


class DevicePostureRuleParam(TypedDict, total=False):
    id: str
    """API UUID."""

    description: str
    """The description of the device posture rule."""

    expiration: str
    """Sets the expiration time for a posture check result.

    If empty, the result remains valid until it is overwritten by new data from the
    WARP client.
    """

    input: InputParam
    """The value to be checked against."""

    match: Iterable[MatchItemParam]
    """The conditions that the client must match to run the rule."""

    name: str
    """The name of the device posture rule."""

    schedule: str
    """Polling frequency for the WARP client posture check.

    Default: `5m` (poll every five minutes). Minimum: `1m`.
    """

    type: Literal[
        "file",
        "application",
        "tanium",
        "gateway",
        "warp",
        "disk_encryption",
        "sentinelone",
        "carbonblack",
        "firewall",
        "os_version",
        "domain_joined",
        "client_certificate",
        "unique_client_id",
        "kolide",
        "tanium_s2s",
        "crowdstrike_s2s",
        "intune",
        "workspace_one",
        "sentinelone_s2s",
    ]
    """The type of device posture rule."""