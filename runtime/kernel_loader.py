"""
Kernel Loader - Dynamic JSON Interpreter

Loads and interprets kernel/system_snapshot_motorcore.json dynamically.
The kernel remains the single source of truth - this module interprets it at runtime,
does NOT compile it to code.

Critical: Kernel JSON must remain human-editable for research flexibility.
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Literal
from pydantic import BaseModel, Field


# =============================================================================
# KERNEL CONFIGURATION MODELS
# =============================================================================

class BioRhythmPhase(BaseModel):
    """Single phase of bio-rhythm cycle"""
    action: str


class BioRhythmCycle(BaseModel):
    """4-phase bio-rhythm cycle configuration"""
    description: str
    phases: Dict[str, BioRhythmPhase]

    def get_phase_names(self) -> List[str]:
        """Get ordered list of phase names"""
        # Extract phase numbers and sort
        phases = [(k, v) for k, v in self.phases.items()]
        return [k for k, v in sorted(phases, key=lambda x: x[0])]


class HeuristicRule(BaseModel):
    """Single heuristic rule (e.g., safety_buffer_rule)"""
    action: str
    trigger: str


class InterdisciplinaryHeuristics(BaseModel):
    """Safety and challenge heuristics"""
    safety_buffer_rule: HeuristicRule
    challenge_rule: HeuristicRule
    cognitive_rest: HeuristicRule
    esthetic_deviation_rule: HeuristicRule
    indirect_awakening_rule: HeuristicRule


class ResonanceMetrics(BaseModel):
    """Resonance cycle metric definitions"""
    YRE: str  # Formula as string
    YRE_legacy: str
    YRE_note: str
    CI: str  # Description
    ΔÇE: str  # Description
    Δf: str  # Description
    DF: str  # Description
    Safety_Weight: str
    Ma_Factor: str


class ResonanceCycle(BaseModel):
    """Resonance cycle configuration"""
    purpose: str
    phases: Dict[str, str]  # scan, echo, threshold_test, feedback
    metrics: ResonanceMetrics
    states: Dict[str, str]  # low_resonance, balanced, high_resonance, astral
    actions: Dict[str, str]


class MetaAnalysisScale(BaseModel):
    """Single scale definition (micro/meso/macro)"""
    description: str
    trigger: str
    expected_YRE: str


class MetaAnalysisCore(BaseModel):
    """Meta-analysis core configuration"""
    purpose: str
    principles: List[str]
    scales: Dict[str, MetaAnalysisScale]
    operations: Dict[str, str]
    resonance_hooks: Dict[str, List[str]]
    metrics: Dict[str, str]
    states: Dict[str, str]
    actions: Dict[str, str]


class AmplificationLayer(BaseModel):
    """Single amplification layer (e.g., Dissonance Gain)"""
    name: str
    purpose: str
    trigger: Optional[List[str]] = None
    action: Optional[str] = None
    metric_hooks: Optional[List[str]] = None


class RuntimeParams(BaseModel):
    """Runtime parameters"""
    max_turns: int = 128
    astral_threshold: float = 0.8
    philosopher_scan_every_turn: bool = True


class LightPanel(BaseModel):
    """Light panel state (event logging)"""
    total_events: int = 0
    intensity_score: float = 0.0
    channels: List[str]


class SystemState(BaseModel):
    """Current system state"""
    bio_rhythm_phase: Optional[str] = None
    resonance_state: Optional[str] = None
    meta_analysis_scale: Optional[str] = None
    meta_analysis_trajectory: Optional[str] = None
    last_updated: Optional[str] = None


class KernelConfig(BaseModel):
    """
    Complete kernel configuration loaded from JSON.

    This is the runtime representation of kernel/system_snapshot_motorcore.json.
    All system behavior derives from this configuration.
    """
    version: str
    codename: str
    purpose: str
    principles: List[str]

    # Core modules
    bio_rhythm_cycle: BioRhythmCycle
    interdisciplinary_heuristics: InterdisciplinaryHeuristics
    resonance_cycle: ResonanceCycle
    meta_analysis_core: MetaAnalysisCore

    # Extensions
    amplification_layers: List[AmplificationLayer]
    runtime_params: RuntimeParams
    light_panel: LightPanel
    state: SystemState

    # Full raw data for access to any field
    raw_data: Dict[str, Any] = Field(default_factory=dict)


# =============================================================================
# KERNEL LOADER
# =============================================================================

class KernelLoader:
    """
    Loads and interprets the kernel JSON dynamically.

    Philosophy:
    - Kernel JSON is the single source of truth
    - This loader INTERPRETS, does NOT compile
    - Kernel remains human-editable
    - Changes to kernel JSON take effect immediately on reload
    """

    def __init__(self, kernel_path: Optional[Path] = None):
        """
        Initialize kernel loader.

        Args:
            kernel_path: Path to kernel JSON. If None, uses default location.
        """
        if kernel_path is None:
            # Default: kernel/system_snapshot_motorcore.json relative to project root
            self.kernel_path = Path(__file__).parent.parent / "kernel" / "system_snapshot_motorcore.json"
        else:
            self.kernel_path = Path(kernel_path)

        if not self.kernel_path.exists():
            raise FileNotFoundError(f"Kernel not found at: {self.kernel_path}")

    def load(self) -> KernelConfig:
        """
        Load and interpret kernel JSON.

        Returns:
            KernelConfig object with all kernel data

        Raises:
            FileNotFoundError: If kernel JSON not found
            json.JSONDecodeError: If kernel JSON is malformed
            ValueError: If kernel structure is invalid
        """
        with open(self.kernel_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Extract system_core
        system_core = data.get("system_core", {})
        modules = data.get("modules", {})

        # Parse bio_rhythm_cycle
        bio_rhythm_data = modules.get("bio_rhythm_cycle", {})
        bio_rhythm = BioRhythmCycle(
            description=bio_rhythm_data.get("description", ""),
            phases={
                k: BioRhythmPhase(action=v.get("action", ""))
                for k, v in bio_rhythm_data.get("phases", {}).items()
            }
        )

        # Parse interdisciplinary_heuristics
        heuristics_data = modules.get("interdisciplinary_heuristics", {})
        heuristics = InterdisciplinaryHeuristics(
            safety_buffer_rule=HeuristicRule(**heuristics_data.get("safety_buffer_rule", {})),
            challenge_rule=HeuristicRule(**heuristics_data.get("challenge_rule", {})),
            cognitive_rest=HeuristicRule(**heuristics_data.get("cognitive_rest", {})),
            esthetic_deviation_rule=HeuristicRule(**heuristics_data.get("esthetic_deviation_rule", {})),
            indirect_awakening_rule=HeuristicRule(**heuristics_data.get("indirect_awakening_rule", {})),
        )

        # Parse resonance_cycle
        resonance_data = modules.get("resonance_cycle", {})
        resonance = ResonanceCycle(
            purpose=resonance_data.get("purpose", ""),
            phases=resonance_data.get("phases", {}),
            metrics=ResonanceMetrics(**resonance_data.get("metrics", {})),
            states=resonance_data.get("states", {}),
            actions=resonance_data.get("actions", {}),
        )

        # Parse meta_analysis_core
        meta_data = modules.get("meta_analysis_core", {})
        meta_analysis = MetaAnalysisCore(
            purpose=meta_data.get("purpose", ""),
            principles=meta_data.get("principles", []),
            scales={
                k: MetaAnalysisScale(**v)
                for k, v in meta_data.get("scales", {}).items()
            },
            operations=meta_data.get("operations", {}),
            resonance_hooks=meta_data.get("resonance_hooks", {}),
            metrics=meta_data.get("metrics", {}),
            states=meta_data.get("states", {}),
            actions=meta_data.get("actions", {}),
        )

        # Parse amplification_layers
        amp_layers = [
            AmplificationLayer(**layer)
            for layer in data.get("amplification_layers", [])
        ]

        # Parse runtime_params
        runtime_params_data = data.get("runtime_params", {})
        runtime_params = RuntimeParams(**runtime_params_data)

        # Parse light_panel
        light_panel_data = data.get("light_panel", {})
        light_panel = LightPanel(**light_panel_data)

        # Parse state
        state_data = data.get("state", {})
        state = SystemState(**state_data)

        # Create KernelConfig
        config = KernelConfig(
            version=system_core.get("version", "unknown"),
            codename=system_core.get("codename", ""),
            purpose=system_core.get("purpose", ""),
            principles=system_core.get("principles", []),
            bio_rhythm_cycle=bio_rhythm,
            interdisciplinary_heuristics=heuristics,
            resonance_cycle=resonance,
            meta_analysis_core=meta_analysis,
            amplification_layers=amp_layers,
            runtime_params=runtime_params,
            light_panel=light_panel,
            state=state,
            raw_data=data,  # Preserve full raw data for extensions
        )

        return config

    def reload(self) -> KernelConfig:
        """
        Reload kernel from disk.

        Useful for live updates during development/research.
        """
        return self.load()


# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

def load_kernel(kernel_path: Optional[Path] = None) -> KernelConfig:
    """
    Convenience function to load kernel.

    Args:
        kernel_path: Optional custom kernel path

    Returns:
        Loaded KernelConfig
    """
    loader = KernelLoader(kernel_path)
    return loader.load()


# =============================================================================
# MAIN (for testing)
# =============================================================================

if __name__ == "__main__":
    # Test loading kernel
    print("Loading kernel...")
    config = load_kernel()

    print(f"\nKernel Version: {config.version}")
    print(f"Codename: {config.codename}")
    print(f"\nBio-Rhythm Phases: {config.bio_rhythm_cycle.get_phase_names()}")
    print(f"Astral Threshold: {config.runtime_params.astral_threshold}")
    print(f"Philosopher Scan Every Turn: {config.runtime_params.philosopher_scan_every_turn}")

    print(f"\nMeta-Analysis Scales:")
    for scale_name, scale in config.meta_analysis_core.scales.items():
        print(f"  {scale_name}: {scale.description}")

    print(f"\nAmplification Layers: {len(config.amplification_layers)}")
    for layer in config.amplification_layers:
        print(f"  - {layer.name}")

    print("\n✅ Kernel loaded successfully!")
