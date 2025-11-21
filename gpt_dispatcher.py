"""
BotZaVOD GitHub Lite — gpt_dispatcher

In the internal platform this module routes requests between different
GPT backends (local llama.cpp, remote providers, hybrid modes, etc.).

The Lite version provides a very small, fully self-contained dispatcher
that forwards everything to a demo engine interface.
"""

from __future__ import annotations

import logging
from typing import Any, Dict

from .run_gpt_engine import DemoGptEngine, EngineConfig

logger = logging.getLogger("botzavod.gpt_dispatcher")
if not logger.handlers:
    logging.basicConfig(level=logging.INFO)


class GptDispatcher:
    """Minimal dispatcher used in the public demo.

    The real implementation includes:
    - routing based on mode / latency / availability,
    - error budgets and fallback chains,
    - telemetry and accelerator awareness.

    Those details are intentionally not published here.
    """

    def __init__(self, engine: DemoGptEngine | None = None) -> None:
        self.engine = engine or DemoGptEngine(EngineConfig())
        logger.info("GptDispatcher initialized with demo engine")

    def handle_request(self, prompt: str, **kwargs: Any) -> Dict[str, Any]:
        """Forward the request to the demo engine.

        The shape of the result is compatible with the real platform,
        but all heavy logic is removed.
        """
        logger.debug("handle_request() called with kwargs=%s", kwargs)
        return self.engine.generate(prompt, **kwargs)
