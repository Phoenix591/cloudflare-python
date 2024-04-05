# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from .ip_rule import IPRule
from .email_rule import EmailRule
from .group_rule import GroupRule
from .domain_rule import DomainRule
from .country_rule import CountryRule
from .ip_list_rule import IPListRule
from .everyone_rule import EveryoneRule
from .email_list_rule import EmailListRule
from .okta_group_rule import OktaGroupRule
from .saml_group_rule import SamlGroupRule
from .azure_group_rule import AzureGroupRule
from .certificate_rule import CertificateRule
from .gsuite_group_rule import GsuiteGroupRule
from .service_token_rule import ServiceTokenRule
from .device_posture_rule import DevicePostureRule
from .external_evaluation_rule import ExternalEvaluationRule
from .github_organization_rule import GitHubOrganizationRule
from .authentication_method_rule import AuthenticationMethodRule
from .any_valid_service_token_rule import AnyValidServiceTokenRule

__all__ = ["Rule"]

Rule = Union[
    EmailRule,
    EmailListRule,
    DomainRule,
    EveryoneRule,
    IPRule,
    IPListRule,
    CertificateRule,
    GroupRule,
    AzureGroupRule,
    GitHubOrganizationRule,
    GsuiteGroupRule,
    OktaGroupRule,
    SamlGroupRule,
    ServiceTokenRule,
    AnyValidServiceTokenRule,
    ExternalEvaluationRule,
    CountryRule,
    AuthenticationMethodRule,
    DevicePostureRule,
]