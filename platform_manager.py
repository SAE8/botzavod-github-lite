"""
BotZaVOD GitHub Lite — platform_manager

Thin orchestration layer that would usually be used by CLI / daemon
processes to run the platform.
"""

from __future__ import annotations

from .platform_controller import PlatformController


def run_demo_session() -> None:
    controller = PlatformController()
    text = "Hello from a GitHub Lite session!"
    result = controller.handle_user_prompt(text)
    print(result["output"])
