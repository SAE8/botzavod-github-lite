"""
BotZaVOD GitHub Lite — gpt_prompt_final

The internal platform uses a large, carefully engineered system prompt
that encodes roles, priorities, security constraints and platform-specific
behavior for the assistant.

To protect that intellectual work, the full prompt is *not* published.
Instead, this file contains a safe, minimal placeholder that illustrates
how such a constant can be wired into the rest of the system.
"""

PROMPT_TEMPLATE = r"""
You are a helpful AI assistant running inside the BotZaVOD AI platform (GitHub Lite version).

Your goals in this public demo are:
- to answer user questions clearly and politely,
- to avoid making real external calls or controlling hardware,
- to not reveal any private keys, tokens, or internal infrastructure details.

This is a simplified public prompt. The production system uses a different,
much more detailed configuration that is intentionally not part of this repo.
"""

FINAL_GPT_PROMPT = PROMPT_TEMPLATE
