"""
BotZaVOD GitHub Lite — memory_controller_core

The real platform ships with a multi-layer memory controller
managing short-term, long-term and structured memories.

For GitHub Lite we expose a thin stub that documents the shape of the
interface without revealing algorithms or storage backends.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class MemoryRecord:
    role: str
    content: str


@dataclass
class MemoryState:
    history: List[MemoryRecord] = field(default_factory=list)


class MemoryController:
    """Minimal, in-memory stub implementation."""

    def __init__(self) -> None:
        self._state = MemoryState()

    def add(self, role: str, content: str) -> None:
        self._state.history.append(MemoryRecord(role=role, content=content))

    def snapshot(self) -> Dict[str, Any]:
        return {"history": [r.__dict__ for r in self._state.history]}
