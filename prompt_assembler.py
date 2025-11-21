"""
BotZaVOD GitHub Lite — prompt_assembler

In the full platform this module combines:
- the base system prompt,
- conversation history,
- memory snapshots,
- tool / accelerator instructions.

The Lite version exposes only a minimal assembler that merges a fixed
system prompt with the current user message.
"""

from __future__ import annotations

from typing import Dict

from .gpt_prompt_final import FINAL_GPT_PROMPT


def assemble_prompt(user_message: str) -> str:
    """Return a very simple combined prompt.

    This keeps just enough structure to demonstrate the idea.
    """
    return f"{FINAL_GPT_PROMPT}\n\nUser: {user_message}\nAssistant:"
