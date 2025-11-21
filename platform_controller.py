"""
BotZaVOD GitHub Lite — platform_controller

High-level facade that connects API, dispatcher and memory.
The goal here is to show how the layers fit together logically.
"""

from __future__ import annotations

from typing import Dict

from .api_module import ApiRequest, GptApi
from .memory_orchestrator import MemoryOrchestrator


class PlatformController:
    def __init__(self) -> None:
        self.api = GptApi()
        self.memory = MemoryOrchestrator()

    def handle_user_prompt(self, text: str) -> Dict[str, str]:
        self.memory.on_user_query(text)
        response = self.api.completion(ApiRequest(prompt=text))
        self.memory.on_assistant_reply(response.output)
        return {"output": response.output}
