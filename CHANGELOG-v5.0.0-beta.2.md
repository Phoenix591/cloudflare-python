# v5.0.0-beta.2

> This is a beta release. The API surface may change before the stable release.

Full diff: [`v5.0.0-beta.1...next`](https://github.com/cloudflare/cloudflare-python/compare/v5.0.0-beta.1...next)

This release adds 163 new methods across 4 new top-level resources and numerous sub-resource
expansions, restructures the `api.md` surface into per-resource files, and includes codegen
updates across all existing resources.

## General Changes

### Client-level `account_id` and `zone_id` configuration

You can now set `account_id` and `zone_id` once on the client instead of passing them to every
method call. When set, these values are used as defaults for all methods that accept them. You
can still override per-call by passing the parameter explicitly.

```python
from cloudflare import Cloudflare

# Set account_id once at the client level
client = Cloudflare(account_id="my-account-id")

# No need to pass account_id on every call
workers = client.workers.scripts.list()
rules = client.rules.lists.list()
```

Both options also read from environment variables:

- `account_id` from `CLOUDFLARE_ACCOUNT_ID`
- `zone_id` from `CLOUDFLARE_ZONE_ID`

```python
# Or configure via environment variables
# export CLOUDFLARE_ACCOUNT_ID=my-account-id
# export CLOUDFLARE_ZONE_ID=my-zone-id
client = Cloudflare()
```

All methods that previously required `account_id` or `zone_id` as a positional/keyword argument
now accept `None` as a default and fall back to the client-level value. If neither is set, a
`ValueError` is raised with a clear message.

## Breaking Changes

### Restructured Resources

- **AISearch**: `aisearch.instances.items` (`get`, `list`) has been replaced by the new
  namespace-based architecture under `aisearch.namespaces.instances.items` (see New Resources
  below)

- **Registrar**: `registrar.domains` (`get`, `list`, `update`) has been replaced by
  `registrar.registrations` with expanded functionality including `create`, `edit`, `get`, `list`,
  plus new `registrar.check`, `registrar.search`, `registrar.registration_status.get`, and
  `registrar.update_status.get` methods

- **Custom Pages**: `custom_pages` (`get`, `list`, `update`) has been replaced by
  `custom_pages.assets` (`create`, `delete`, `get`, `list`, `update`)

### Removed Methods

- `cloudforce_one.threat_events.delete`

## New API Resources

### Top-Level Resources

- **VulnerabilityScanner** -- Full CRUD for vulnerability scanning
  - `credential_sets` -- `create`, `delete`, `edit`, `get`, `list`, `update`
  - `credential_sets.credentials` -- `create`, `delete`, `edit`, `get`, `list`, `update`
  - `scans` -- `create`, `get`, `list`
  - `target_environments` -- `create`, `delete`, `edit`, `get`, `list`, `update`

- **GoogleTagGateway** -- Google Tag Gateway configuration
  - `config` -- `get`, `update`

- **EmailSending** -- Email sending with subdomain management
  - `send`, `send_raw`
  - `subdomains` -- `create`, `delete`, `get`, `list`
  - `subdomains.dns` -- `get`

- **ResourceTagging** -- Resource tagging and key/value management
  - `list`
  - `account_tags` -- `delete`, `get`, `update`
  - `zone_tags` -- `delete`, `get`, `update`
  - `keys` -- `list`
  - `values` -- `list`

### New Sub-Resources on Existing Resources

- **AISearch** (restructured) -- Expanded namespace-based architecture
  - `aisearch.namespaces` -- `create`, `delete`, `list`, `read`, `search`, `update`,
    `chat_completions`
  - `aisearch.namespaces.instances` -- `create`, `list`, `read`, `search`, `stats`, `update`,
    `chat_completions`
  - `aisearch.namespaces.instances.items` -- `chunks`, `create_or_update`, `delete`, `download`,
    `get`, `list`, `logs`, `sync`, `upload`
  - `aisearch.namespaces.instances.jobs` -- `create`, `get`, `list`, `logs`, `update`

- **APIGateway Labels** -- Label management for API Gateway operations
  - `api_gateway.labels` -- `list`
  - `api_gateway.labels.managed` -- `get`
  - `api_gateway.labels.managed.resources.operation` -- `update`
  - `api_gateway.labels.user` -- `bulk_create`, `bulk_delete`, `delete`, `edit`, `get`, `update`
  - `api_gateway.labels.user.resources.operation` -- `update`
  - `api_gateway.operations.labels` -- `bulk_create`, `bulk_delete`, `bulk_update`, `create`,
    `delete`, `update`

- **BrowserRendering** -- DevTools and crawl APIs
  - `browser_rendering.crawl` -- `create`, `delete`, `get`
  - `browser_rendering.devtools.browser` -- `connect`, `create`, `delete`, `launch`, `protocol`,
    `version`
  - `browser_rendering.devtools.browser.page` -- `get`
  - `browser_rendering.devtools.browser.targets` -- `activate`, `create`, `get`, `list`
  - `browser_rendering.devtools.session` -- `get`, `list`

- **Custom Pages Assets** -- Custom page asset management
  - `custom_pages.assets` -- `create`, `delete`, `get`, `list`, `update`

- **ACM Custom Trust Store** -- Custom origin trust store
  - `acm.custom_trust_store` -- `create`, `delete`, `get`, `list`

- **Workers Observability Destinations** -- Log destinations for Workers observability
  - `workers.observability.destinations` -- `create`, `delete`, `list`, `update`

- **Registrar** (expanded) -- Domain registration with full lifecycle management
  - `registrar.registrations` -- `create`, `edit`, `get`, `list`
  - `registrar.check`, `registrar.search`
  - `registrar.registration_status` -- `get`
  - `registrar.update_status` -- `get`

- **Zero Trust** additions
  - `zero_trust.access.users` -- `create`, `delete`, `get`, `update`
  - `zero_trust.devices.ip_profiles` -- `create`, `delete`, `get`, `list`, `update`
  - `zero_trust.dex.rules` -- `create`, `delete`, `get`, `list`, `update`
  - `zero_trust.dlp.settings` -- `delete`, `edit`, `get`, `update`
  - `zero_trust.gateway.pacfiles` -- `create`, `delete`, `get`, `list`, `update`
  - `zero_trust.networks.subnets.warp` -- `create`, `delete`, `edit`, `get`
  - `zero_trust.tunnels.warp_connector.connections` -- `get`
  - `zero_trust.tunnels.warp_connector.connectors` -- `get`
  - `zero_trust.tunnels.warp_connector.failover` -- `update`

- **Zones Environments** -- Zone environment management
  - `zones.environments` -- `create`, `delete`, `edit`, `list`, `rollback`, `update`

- **Radar** additions
  - `radar.agent_readiness` -- `summary`
  - `radar.ai.markdown_for_agents` -- `summary`, `timeseries`
  - `radar.entities.asns` -- `botnet_threat_feed`
  - `radar.post_quantum.origin` -- `summary`, `timeseries_groups`
  - `radar.post_quantum.tls` -- `support`

- **Billing Usage** -- PayGo billing usage
  - `billing.usage` -- `paygo`

- **Email Security** -- PhishGuard reporting
  - `email_security.phishguard.reports` -- `list`

- **Brand Protection** -- v2 endpoints
  - `brand_protection.v2` additions

## Bug Fixes

- **fix(dlp)**: Add missing `model_rebuild()`/`update_forward_refs()` calls for
  `CustomProfileSharedEntryCustomEntry` and `IntegrationProfileSharedEntryCustomEntry`, fixing
  pydantic v1 validation errors on DLP profile types.
- **fix(workers)**: Make `RunQueryParametersNeedleValue` a `BaseModel` with
  `arbitrary_types_allowed` to prevent pydantic config errors.

## Internal

- `api.md` has been restructured from a single monolithic file into per-resource files under
  `src/cloudflare/resources/*/api.md`. The root `api.md` now contains shared types and links to
  each resource's documentation.
- Codegen updates applied across all resources with updated type annotations and method signatures.
