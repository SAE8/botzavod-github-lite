"""
BotZaVOD GitHub Lite — api_interface

Very small adapter that shows how a concrete web framework
could talk to the `GptApi` object. The actual HTTP wiring is left
to the integrator.
"""

from __future__ import annotations

from typing import Dict

from .api_module import ApiRequest, GptApi

api = GptApi()


def handle_http_like_request(payload: Dict[str, str]) -> Dict[str, str]:
    """Example adapter that could be used from FastAPI / Flask / etc."""
    prompt = payload.get("prompt", "")
    response = api.completion(ApiRequest(prompt=prompt))
    return {"output": response.output}
