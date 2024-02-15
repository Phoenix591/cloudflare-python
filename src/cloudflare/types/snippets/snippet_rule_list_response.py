# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SnippetRuleListResponse", "SnippetRuleListResponseItem"]


class SnippetRuleListResponseItem(BaseModel):
    description: Optional[str] = None

    enabled: Optional[bool] = None

    expression: Optional[str] = None

    snippet_name: Optional[str] = None
    """Snippet identifying name"""


SnippetRuleListResponse = List[SnippetRuleListResponseItem]
