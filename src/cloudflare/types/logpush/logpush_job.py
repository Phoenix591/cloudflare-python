# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .output_options import OutputOptions

__all__ = ["LogpushJob"]


class LogpushJob(BaseModel):
    id: Optional[int] = None
    """Unique id of the job."""

    dataset: Optional[
        Literal[
            "access_requests",
            "audit_logs",
            "biso_user_actions",
            "casb_findings",
            "device_posture_results",
            "dlp_forensic_copies",
            "dns_firewall_logs",
            "dns_logs",
            "email_security_alerts",
            "firewall_events",
            "gateway_dns",
            "gateway_http",
            "gateway_network",
            "http_requests",
            "magic_ids_detections",
            "nel_reports",
            "network_analytics_logs",
            "page_shield_events",
            "sinkhole_http_logs",
            "spectrum_events",
            "ssh_logs",
            "workers_trace_events",
            "zaraz_events",
            "zero_trust_network_sessions",
        ]
    ] = None
    """Name of the dataset.

    A list of supported datasets can be found on the
    [Developer Docs](https://developers.cloudflare.com/logs/reference/log-fields/).
    """

    destination_conf: Optional[str] = None
    """Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.

    Additional configuration parameters supported by the destination may be
    included.
    """

    enabled: Optional[bool] = None
    """Flag that indicates if the job is enabled."""

    error_message: Optional[str] = None
    """If not null, the job is currently failing.

    Failures are usually repetitive (example: no permissions to write to destination
    bucket). Only the last failure is recorded. On successful execution of a job the
    error_message and last_error are set to null.
    """

    frequency: Optional[Literal["high", "low"]] = None
    """This field is deprecated.

    Please use `max_upload_*` parameters instead. The frequency at which Cloudflare
    sends batches of logs to your destination. Setting frequency to high sends your
    logs in larger quantities of smaller files. Setting frequency to low sends logs
    in smaller quantities of larger files.
    """

    kind: Optional[Literal["edge"]] = None
    """
    The kind parameter (optional) is used to differentiate between Logpush and Edge
    Log Delivery jobs. Currently, Edge Log Delivery is only supported for the
    `http_requests` dataset.
    """

    last_complete: Optional[datetime] = None
    """Records the last time for which logs have been successfully pushed.

    If the last successful push was for logs range 2018-07-23T10:00:00Z to
    2018-07-23T10:01:00Z then the value of this field will be 2018-07-23T10:01:00Z.
    If the job has never run or has just been enabled and hasn't run yet then the
    field will be empty.
    """

    last_error: Optional[datetime] = None
    """Records the last time the job failed.

    If not null, the job is currently failing. If null, the job has either never
    failed or has run successfully at least once since last failure. See also the
    error_message field.
    """

    logpull_options: Optional[str] = None
    """This field is deprecated.

    Use `output_options` instead. Configuration string. It specifies things like
    requested fields and timestamp formats. If migrating from the logpull api, copy
    the url (full url or just the query string) of your call here, and logpush will
    keep on making this call for you, setting start and end times appropriately.
    """

    max_upload_bytes: Optional[int] = None
    """The maximum uncompressed file size of a batch of logs.

    This setting value must be between `5 MB` and `1 GB`, or `0` to disable it. Note
    that you cannot set a minimum file size; this means that log files may be much
    smaller than this batch size. This parameter is not available for jobs with
    `edge` as its kind.
    """

    max_upload_interval_seconds: Optional[int] = None
    """The maximum interval in seconds for log batches.

    This setting must be between 30 and 300 seconds (5 minutes), or `0` to disable
    it. Note that you cannot specify a minimum interval for log batches; this means
    that log files may be sent in shorter intervals than this. This parameter is
    only used for jobs with `edge` as its kind.
    """

    max_upload_records: Optional[int] = None
    """The maximum number of log lines per batch.

    This setting must be between 1000 and 1,000,000 lines, or `0` to disable it.
    Note that you cannot specify a minimum number of log lines per batch; this means
    that log files may contain many fewer lines than this. This parameter is not
    available for jobs with `edge` as its kind.
    """

    name: Optional[str] = None
    """Optional human readable job name.

    Not unique. Cloudflare suggests that you set this to a meaningful string, like
    the domain name, to make it easier to identify your job.
    """

    output_options: Optional[OutputOptions] = None
    """The structured replacement for `logpull_options`.

    When including this field, the `logpull_option` field will be ignored.
    """
