# ResonaQ-Cognitive Runtime

Modern agentic system with sophisticated cognitive architecture.

## What is ResonaQ?

ResonaQ combines the capabilities of modern agentic AI systems (like OpenClaw/Moltbot) with a unique cognitive architecture based on:

- **Bio-Rhythm Cycles**: 4-phase processing (sentiment scan → limbic link → processing pause → output modulation)
- **Resonance Metrics**: Dynamic metrics (YRE, CI, ΔÇE, Φ, Ψ) measuring system coherence and energy
- **Triadic-Flow Network**: 11-node cognitive graph with 3 pillars (constraint, expansion, integration)
- **Multi-Scale Reasoning**: Automatic scale selection (micro/meso/macro/astral)
- **Philosopher Consensus**: Multi-agent coordination with contradiction as energy

## Architecture

```
Kernel (Source of Truth)
  ├── Bio-Rhythm Cycle (4 phases)
  ├── Resonance Cycle (YRE metrics)
  ├── Meta-Analysis Core (scale selection)
  └── Interdisciplinary Heuristics (safety rules)

Runtime (Execution Environment)
  ├── Kernel Loader (dynamic JSON interpreter)
  ├── Bio-Rhythm Graph (LangGraph state machine)
  ├── Resonance Metrics (YRE, CI, ΔÇE, Φ, Ψ computation)
  ├── LLM Client (Claude/Anthropic API)
  ├── Tools (MCP: files, shell, web, communication)
  └── Memory (Session: SQLite, Long-term: ChromaDB)

Agents (Specialized Processors)
  ├── Triadic-Flow (11-node cognitive network)
  ├── Socratic-Lens (Context Grammar Induction)
  ├── Lagrange-Lens (Symmetry-driven decisions)
  ├── Meta-Analysis (Heterogeneity management)
  └── Driftcraft (Navigable linguistic space)
```

## Quick Start

### 1. Setup Environment

```bash
# Create virtual environment
python3.11 -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Linux/Mac)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Claude API

```bash
# Windows
set ANTHROPIC_API_KEY=your_key_here

# Linux/Mac
export ANTHROPIC_API_KEY=your_key_here
```

### 3. Test Kernel Loading

```bash
python runtime/kernel_loader.py
```

Expected output:
```
Loading kernel...

Kernel Version: v9.2-TrueStealth-motorcore
Codename: Adaptive Dojo (Zen Architect)

Bio-Rhythm Phases: ['1_sentiment_scan', '2_direct_link', '3_process_pause', '4_response_modulation']
Astral Threshold: 0.8
...
```

### 4. Test Resonance Metrics

```bash
python runtime/resonance_metrics.py
```

## Project Structure

```
ResonaQ-Cognitive/
├── kernel/                          # Source of truth (unchanged)
│   └── system_snapshot_motorcore.json
├── agents/                          # Agent definitions (unchanged)
│   ├── triadic-flow/engine.json
│   ├── socratic-lens/
│   └── ...
├── runtime/                         # NEW - Execution environment
│   ├── kernel_loader.py            # Kernel JSON interpreter
│   ├── resonance_metrics.py        # YRE, CI, ΔÇE, Φ, Ψ computation
│   ├── bio_rhythm_graph.py         # 4-phase state machine
│   ├── orchestrator.py             # Multi-agent coordinator
│   ├── llm/
│   │   └── claude_client.py       # Anthropic API wrapper
│   ├── tools/                      # MCP tools
│   │   ├── file_tools.py
│   │   ├── shell_tools.py
│   │   └── web_tools.py
│   ├── memory/
│   │   ├── session_store.py       # Session persistence
│   │   └── vector_store.py        # Long-term memory
│   └── agent_graphs/               # Per-agent LangGraph implementations
├── tests/                           # NEW - Test suite
├── requirements.txt                 # Dependencies
├── pyproject.toml                   # Project configuration
└── resonaq-cli.py                   # CLI interface
```

## Key Features

### 1. Kernel = Source of Truth

The `kernel/system_snapshot_motorcore.json` file remains the single source of truth. The runtime **interprets** it dynamically - never compiles. This preserves research flexibility.

```python
from runtime.kernel_loader import load_kernel

kernel = load_kernel()
print(kernel.bio_rhythm_cycle.get_phase_names())
# ['1_sentiment_scan', '2_direct_link', '3_process_pause', '4_response_modulation']
```

### 2. Resonance Metrics

All metrics are computed dynamically based on kernel formulas:

```python
from runtime.resonance_metrics import ResonanceMetrics, ResonanceState

state = ResonanceState(nodes={...}, ...)
YRE = ResonanceMetrics.compute_YRE(state)

# YRE interpretation:
# < 0.3: Low resonance (noise zone)
# 0.3-0.6: Balanced
# 0.6-0.9: High resonance
# >= 0.9: Astral (full coherence)
```

### 3. Multi-Agent Coordination

Agents share kernel state and coordinate via A2A protocol:

```python
from runtime.orchestrator import ResonaQOrchestrator

orchestrator = ResonaQOrchestrator(kernel)
result = await orchestrator.run("User input", session_id="user_123")
```

## Development Status

### ✅ Phase 1: Foundation (Current)

- [x] Project structure
- [x] Kernel loader (dynamic JSON interpreter)
- [x] Resonance metrics (YRE, CI, ΔÇE, Φ, Ψ)
- [ ] Bio-rhythm graph (LangGraph state machine)
- [ ] Claude client (Anthropic API wrapper)
- [ ] Basic tools (file I/O)
- [ ] CLI interface
- [ ] Unit tests

### 📋 Phase 2: Agent Conversion

- [ ] Socratic-Lens agent (CGI runner wrapper)
- [ ] Lagrange-Lens agent (signal-based)
- [ ] LLM integration tests
- [ ] Web browsing tool

### 📋 Phase 3: Multi-Agent Orchestration

- [ ] Triadic-Flow agent (11-node network)
- [ ] Agent coordinator
- [ ] Philosopher consensus
- [ ] Light panel logging
- [ ] Vector store (long-term memory)

### 📋 Phase 4: Protocol Integration

- [ ] MCP client (full implementation)
- [ ] A2A server
- [ ] Tool safety checker
- [ ] Audit logging

### 📋 Phase 5: Production Hardening

- [ ] Comprehensive test suite
- [ ] Error handling
- [ ] Performance optimization
- [ ] Documentation
- [ ] Deployment options

## Philosophy

ResonaQ is not just another AI agent. It's a cognitive architecture that:

1. **Treats contradiction as energy**, not error
2. **Preserves philosophical depth** while enabling real-world action
3. **Adapts scale dynamically** (micro/meso/macro/astral)
4. **Maintains kernel as source of truth** (human-editable, research-friendly)
5. **Coordinates multiple specialized agents** via resonance principles

## References

- [Plan Document](C:\Users\altug_h4ei4ws\.claude\plans\giggly-wondering-balloon.md)
- [Kernel Definition](kernel/system_snapshot_motorcore.json)
- [Triadic-Flow Specification](agents/triadic-flow/engine.json)

## License

MIT

---

**Version**: 1.0.0-alpha
**Status**: Active Development (Phase 1)
**Framework**: LangGraph + MCP
**LLM Provider**: Claude (Anthropic)
