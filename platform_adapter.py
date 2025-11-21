"""
BotZaVOD GitHub Lite — platform_adapter

Showcases how the platform controller could be exposed to the
outside world (e.g. CLI, Telegram bot, web panel).
"""

from __future__ import annotations

from typing import Dict

from .platform_controller import PlatformController


controller = PlatformController()


def handle_text(text: str) -> Dict[str, str]:
    return controller.handle_user_prompt(text)
