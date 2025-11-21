"""
BotZaVOD GitHub Lite — memory_module

Compatibility wrapper around `MemoryController`. In the internal
codebase this module is richer and connects to external stores.
"""

from __future__ import annotations

from .memory_controller_core import MemoryController


memory = MemoryController()
