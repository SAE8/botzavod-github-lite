"""
BotZaVOD GitHub Lite — platform_diagnostics

Stub for health checks and simple introspection.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class DiagnosticsReport:
    status: str
    details: Dict[str, str]


def basic_healthcheck() -> DiagnosticsReport:
    return DiagnosticsReport(status="ok", details={"mode": "github-lite"})
