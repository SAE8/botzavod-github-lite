# BotZaVOD — Distributed AI Platform Engine  
**Cloud-ready. Modular. GPU-accelerated. Extensible.**

BotZaVOD is a distributed AI platform designed for running large-scale LLM pipelines, GPU/CPU accelerator modules, autonomous agents, and multi-node orchestration.  
The platform was built from scratch with a focus on modularity, performance, diagnostics, and real-time observability.

## 🚀 Core Features

### **1. Modular Platform Core**
- Central event loop and orchestration logic  
- Unified configuration loader (`platform_config.json`, `platform_settings.json`)  
- Role-based routing (`roles.json`)  
- High-level controller for module lifecycle management  
- Dynamic module discovery in `platform_core/` and `modules/`

### **2. GPU / CPU Accelerators**
- CUDA acceleration (MMQ, FP16/INT8 offload, GPU routing)  
- Quantum-inspired compute modules  
- FPS/latency telemetry for GPU agents  
- Multi-platform GPU agents (Windows, Linux, WSL, Android, Smart TV)  
- Unified booster entrypoint (`graphics_boost_start()`)  

### **3. Memory & Context Engine**
- Persistent memory controller  
- Long-term and short-term state separation  
- Glue layer for injecting memory into LLM prompts  
- Autonomous storage & recall  
- Fully isolated memory pipelines  

### **4. LLM Engine Integration**
- Local LLaMA/Mistral inference (via llama.cpp)  
- Cloud/Hybrid GPT switcher  
- Dispatcher for routing between local and cloud models  
- Structured prompt assembler  
- Safety layer for restricted commands  

### **5. Diagnostics & Self-Monitoring**
- Deep platform diagnostics  
- Live system status reports  
- Accelerator health checks  
- GPU usage, VRAM, FPS, temperature tracking  
- Logging with multi-level verbosity  

### **6. Expandable Module System**
Modules in `modules/` can be:
- Accelerators  
- API interfaces  
- Data collectors  
- Compatibility engines  
- Rendering engines  
- Quantum cores  
- IO/terminal subsystems  
Everything is plug-and-play.

## 🧩 Project Structure

```
botzavod/
 ├── platform_core/
 │    ├── platform_engineer.py
 │    ├── gpt_dispatcher.py
 │    ├── run_gpt_engine.py
 │    ├── prompt_assembler.py
 │    ├── memory_controller_core.py
 │    ├── api_module.py
 │    ├── diagnostics/
 │    ├── ...
 │
 ├── modules/
 │    ├── accelerator_launcher.py
 │    ├── gpu_display_router.py
 │    ├── cuda_module_engineer.py
 │    ├── tunnel_api.py
 │    ├── ...
 │
 ├── ARCHITECTURE.md
 ├── README.md
```

## ⚡ Technology Stack
- Python 3.10+
- CUDA / GPU acceleration
- llama.cpp
- FastAPI
- Tailscale
- WebSockets
- Threading & async
- JSON-based configs
- Diagnostics & logging

## 🌐 Multi-Node Deployment
BotZaVOD supports:
- Local node (GPU/CPU)
- Remote node over Tailscale
- Hybrid orchestrations
- Real-time GPU monitoring
- Secure channel tunneling

## 🧠 Philosophy  
BotZaVOD is built as a “cognitive cloud processor” — a platform that unifies:
- AI reasoning  
- GPU acceleration  
- distributed compute  
- system diagnostics  
- autonomous agents  

The design goal is **scalability, reliability, and modular expansion**.

## 🛠️ Author  
Built and engineered by **Evgenii "Moisey" Semenov** — AI Platform Engineer and system architect.

## 📄 License  
Internal use. Contact for collaboration.
