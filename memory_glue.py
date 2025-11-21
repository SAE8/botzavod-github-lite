"""
BotZaVOD GitHub Lite — memory_glue

In production this module coordinates memory snapshots with the GPT
engine, platform diagnostics, and accelerators.

The Lite version provides just a minimal helper that can be extended
by anyone who forks the repo.
"""

from __future__ import annotations

from typing import Dict, List

from .memory_controller_core import MemoryController, MemoryRecord


class MemoryGlue:
    def __init__(self, controller: MemoryController | None = None) -> None:
        self.controller = controller or MemoryController()

    def record_user_message(self, text: str) -> None:
        self.controller.add("user", text)

    def record_assistant_message(self, text: str) -> None:
        self.controller.add("assistant", text)

    def export_history(self) -> List[Dict[str, str]]:
        snapshot = self.controller.snapshot()
        return list(snapshot.get("history", []))
