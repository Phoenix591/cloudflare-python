# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

from typing import List, Union

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from typing import TYPE_CHECKING

__all__ = ["RankingTimeseriesGroupsResponse", "Meta", "MetaDateRange", "Serie0"]

class MetaDateRange(BaseModel):
    end_time: datetime = FieldInfo(alias = "endTime")
    """Adjusted end of date range."""

    start_time: datetime = FieldInfo(alias = "startTime")
    """Adjusted start of date range."""

class Meta(BaseModel):
    date_range: List[MetaDateRange] = FieldInfo(alias = "dateRange")

class Serie0(BaseModel):
    timestamps: List[str]

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> List[Union[str, float]]:    ...

class RankingTimeseriesGroupsResponse(BaseModel):
    meta: Meta

    serie_0: Serie0