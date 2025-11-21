"""
BotZaVOD GitHub Lite — module_registry

Extremely small registry used only for demonstration purposes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class ModuleRegistry:
    _modules: Dict[str, Any] = field(default_factory=dict)

    def register(self, name: str, module: Any) -> None:
        self._modules[name] = module

    def get(self, name: str) -> Any:
        return self._modules[name]
