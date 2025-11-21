# BotZaVOD Architecture Overview (Demo Version)

This document briefly describes the main layers present in this demo stack.

## 1. GPT Engine Layer (`platform_core`)

**Key files:**
- `run_gpt_engine.py` — entrypoint for the local GPT/LLM engine.
- `gpt_dispatcher.py` — routes requests to the underlying model backend.
- `gpt_prompt_final.py` / `prompt_assembler.py` — final prompt assembly logic.

This layer encapsulates:
- request → prompt assembly → model invocation → response flow
- a clean separation between transport/API logic and core text generation.

## 2. Memory Layer

**Key files:**
- `memory_controller_core.py`
- `memory_module.py`
- `memory_glue.py`
- `memory_orchestrator.py`

The memory layer provides:
- centralized control over different memory segments (short / long / external)
- glue logic for attaching external JSONL-based memory sources
- orchestration of read/write flows around GPT calls.

## 3. Platform Control Layer

**Key files:**
- `platform_controller.py`
- `platform_manager.py`
- `platform_diagnostics.py`
- `platform_adapter.py`
- `module_loader.py`
- `module_registry.py`
- `platform_config.json`, `platform_settings.json`, `roles.json`

This layer represents the "platform shell" around the GPT engine:
- module registry & dynamic loading
- routing between high-level platform functions
- diagnostics and sanity checks
- configuration and role-based behavior.

## 4. Accelerator & GPU Helpers (`modules`)

**Key files:**
- `accelerator_launcher.py`, `accelerator_utils.py`
- `cuda_module_engineer.py`
- `gpu_display_router.py`
- `gpu_fps_monitor_v3.py`

These modules illustrate:
- generic accelerator launching and bookkeeping
- encapsulation of CUDA/GPU-specific logic in isolated helpers
- simple FPS / display routing helpers for GPU-driven workloads.

(The full internal platform contains many more accelerator and quantum-related
modules which are intentionally not included here.)

## 5. Tunnel / Remote Execution Concept

**Key files:**
- `tunnel_api.py`
- `tunnel_agent.py`
- `tunnel_config.json`

This mini-layer demonstrates the **concept** of remote/tunneled execution:
- basic agent interface for remote nodes
- configuration-driven behavior
- simple API façade for higher-level components.

## Intent of this Demo

The goal of this variant is to show:
- how the candidate designs and structures AI infrastructure code,
- how layers (engine, memory, platform, accelerators, tunnels) fit together,
- that the system was built as a modular, extensible platform rather than a
  collection of one-off scripts.

It is intentionally compact and IP-safe, while remaining technical enough
for infra / GPU / LLM engineers to assess code quality and architecture decisions.

---

**GitHub Lite Notice**

This public version intentionally removes all proprietary logic, private prompts, and internal IP. Only high-level structure, interfaces, and safe stubs are included.
