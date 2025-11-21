"""
BotZaVOD GitHub Lite — memory_orchestrator

Placeholder orchestrator that would normally:
- decide what to keep,
- talk to external databases / vector stores,
- prune and compress histories.

All heavy logic is intentionally omitted here.
"""

from __future__ import annotations

from .memory_glue import MemoryGlue


class MemoryOrchestrator:
    def __init__(self) -> None:
        self.glue = MemoryGlue()

    def on_user_query(self, text: str) -> None:
        self.glue.record_user_message(text)

    def on_assistant_reply(self, text: str) -> None:
        self.glue.record_assistant_message(text)
