"""
BotZaVOD GitHub Lite — module_loader

Small, reflective loader that demonstrates how optional modules
could be imported by name. The real platform adds validation,
sandboxing and accelerator-awareness.
"""

from __future__ import annotations

import importlib
from typing import Any


def load_module(dotted_path: str) -> Any:
    """Best-effort dynamic import helper."""
    return importlib.import_module(dotted_path)
