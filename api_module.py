"""
BotZaVOD GitHub Lite — api_module

Simplified HTTP-like API façade.

The internal implementation exposes a FastAPI-based service with
authentication, streaming, and rich telemetry. Here we keep only
a tiny, framework-agnostic interface that could be wrapped by any web layer.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from .gpt_dispatcher import GptDispatcher
from .prompt_assembler import assemble_prompt


@dataclass
class ApiRequest:
    prompt: str


@dataclass
class ApiResponse:
    output: str
    raw: Dict[str, Any]


class GptApi:
    """Lightweight, in-process API object."""

    def __init__(self) -> None:
        self.dispatcher = GptDispatcher()

    def completion(self, request: ApiRequest) -> ApiResponse:
        full_prompt = assemble_prompt(request.prompt)
        raw = self.dispatcher.handle_request(full_prompt)
        return ApiResponse(output=raw.get("output", ""), raw=raw)
