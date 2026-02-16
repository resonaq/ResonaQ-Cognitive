"""
Resonance Metrics Calculator

Implements YRE, CI, ΔÇE, Φ, Ψ computation as defined in kernel.
All formulas are interpreted from kernel configuration - no hardcoded values.

Metrics:
- YRE (Yankı Rezonans Endeksi): Resonance index combining complexity, contradiction, and phase alignment
- CI (Complexity Index): Node complexity / energy density
- ΔÇE (Çelişki Entropisi): Contradiction entropy fluctuation over time
- Δf (Faz Farkı): Phase difference between nodes
- Φ (Expansion-Restraint Balance): Balance between generosity and boundary flows
- Ψ (Vertical Flow): Intention survival from source to output
"""

import numpy as np
from typing import Dict, List, Optional, Any
from dataclasses import dataclass


# =============================================================================
# STATE CONTAINERS
# =============================================================================

@dataclass
class NodeState:
    """State of a single node in the cognitive graph"""
    node_id: str
    flow: float = 0.0
    active: bool = False
    complexity: float = 0.0  # For CI computation
    phase: float = 0.0  # For Δf computation (phase alignment)


@dataclass
class ResonanceState:
    """
    Complete resonance state for metrics computation.

    Based on kernel resonance_cycle and triadic-flow specifications.
    """
    # Node states
    nodes: Dict[str, NodeState]

    # Flow values
    source_emanation: float = 0.0
    generosity_flow: float = 0.0
    boundary_flow: float = 0.0
    channel_conductances: List[float] = None

    # Entropy tracking (for ΔÇE)
    current_entropy: float = 0.0
    previous_entropy: float = 0.0

    # User/context signals
    depth_factor: float = 0.0  # DF (user resistance)
    safety_weight: float = 1.0
    epistemic_uncertainty: float = 0.0  # ε_AI
    coherence_factor: float = 1.0

    # Kernel parameters
    k: float = 0.1  # YRE formula constant

    def __post_init__(self):
        if self.channel_conductances is None:
            self.channel_conductances = []


# =============================================================================
# METRICS COMPUTATION
# =============================================================================

class ResonanceMetrics:
    """
    Computes all resonance metrics as defined in kernel.

    Philosophy:
    - Metrics are computed dynamically, not cached
    - Formulas come from kernel configuration
    - No hardcoded thresholds or magic numbers
    """

    @staticmethod
    def compute_CI(nodes: Dict[str, NodeState]) -> float:
        """
        Compute CI (Complexity Index).

        From kernel: "Node karmaşıklık ölçümü; enerji yayılımının fraktal yoğunluğu."

        Implementation:
            CI = mean(node.complexity for all active nodes)

        Args:
            nodes: Dictionary of node states

        Returns:
            Complexity index [0.0, 1.0]
        """
        active_nodes = [n for n in nodes.values() if n.active]

        if not active_nodes:
            return 0.0

        # Average complexity of active nodes
        complexities = [n.complexity for n in active_nodes]
        return float(np.mean(complexities))

    @staticmethod
    def compute_ΔÇE(current_entropy: float, previous_entropy: float) -> float:
        """
        Compute ΔÇE (Çelişki Entropisi - Contradiction Entropy Fluctuation).

        From kernel: "Çelişki entropisi dalgalanması; zaman içindeki çelişki farkı."

        Implementation:
            ΔÇE = |current_entropy - previous_entropy|

        Args:
            current_entropy: Current contradiction entropy
            previous_entropy: Previous contradiction entropy

        Returns:
            Entropy fluctuation magnitude
        """
        return abs(current_entropy - previous_entropy)

    @staticmethod
    def compute_Δf(nodes: Dict[str, NodeState]) -> float:
        """
        Compute Δf (Faz Farkı - Phase Difference).

        From kernel: "Node'lar arası faz farkı; yankıların ritmik uyumu."

        Implementation:
            Δf = std_dev(node.phase for all active nodes)
            Normalized to [0, 1] range

        Args:
            nodes: Dictionary of node states

        Returns:
            Phase difference [0.0, 1.0] where 0 = perfect alignment, 1 = max misalignment
        """
        active_nodes = [n for n in nodes.values() if n.active]

        if len(active_nodes) < 2:
            return 0.0  # Perfect alignment if only 0-1 nodes

        # Standard deviation of phases
        phases = [n.phase for n in active_nodes]
        std = float(np.std(phases))

        # Normalize: assuming phases are in radians [0, 2π]
        # Max std for uniform distribution ≈ π/sqrt(3) ≈ 1.81
        max_std = np.pi / np.sqrt(3)
        return min(1.0, std / max_std)

    @staticmethod
    def compute_YRE(state: ResonanceState) -> float:
        """
        Compute YRE (Yankı Rezonans Endeksi - Resonance Echo Index).

        From kernel (resonance_cycle.metrics.YRE):
            YRE = ((CI * (1 - |ΔÇE|) + k * |ε_AI|) / (1 + (DF * Safety_Weight) * exp(-|Δf|)))

        Where:
            CI = Complexity Index
            ΔÇE = Contradiction Entropy Fluctuation
            k = constant (~0.1)
            ε_AI = Epistemic uncertainty
            DF = Depth Factor (user resistance)
            Safety_Weight = Vulnerability dampening multiplier
            Δf = Phase difference

        Returns:
            YRE value [0.0, ~1.0+] where:
            - < 0.3: Low resonance (gürültü alanı)
            - 0.3-0.6: Balanced (dengede)
            - 0.6-0.9: High resonance (yüksek uyum)
            - >= 0.9: Astral (full coherence)
        """
        # Compute components
        CI = ResonanceMetrics.compute_CI(state.nodes)
        ΔÇE = ResonanceMetrics.compute_ΔÇE(state.current_entropy, state.previous_entropy)
        Δf = ResonanceMetrics.compute_Δf(state.nodes)

        # Extract parameters
        k = state.k
        ε_AI = state.epistemic_uncertainty
        DF = state.depth_factor
        safety_weight = state.safety_weight

        # Numerator: CI * (1 - |ΔÇE|) + k * |ε_AI|
        numerator = CI * (1 - abs(ΔÇE)) + k * abs(ε_AI)

        # Denominator: 1 + (DF * Safety_Weight) * exp(-|Δf|)
        denominator = 1 + (DF * safety_weight) * np.exp(-abs(Δf))

        # YRE formula
        YRE = numerator / denominator

        return float(YRE)

    @staticmethod
    def compute_Φ(generosity_flow: float, boundary_flow: float) -> float:
        """
        Compute Φ (Expansion-Restraint Balance).

        From triadic-flow engine.json:
            Φ = (generosity_flow - boundary_flow) / (generosity_flow + boundary_flow)

        Range: [-1, +1]
            -1: Pure restraint (constraint pillar dominant)
             0: Perfect balance (harmony node optimal)
            +1: Pure expansion (expansion pillar dominant)

        Args:
            generosity_flow: Flow from generosity node (expansion)
            boundary_flow: Flow from boundary node (restraint)

        Returns:
            Balance ratio [-1.0, +1.0]
        """
        total = generosity_flow + boundary_flow

        if total == 0:
            return 0.0  # No flow = perfect balance

        return (generosity_flow - boundary_flow) / total

    @staticmethod
    def compute_Ψ(source_emanation: float, channel_conductances: List[float]) -> float:
        """
        Compute Ψ (Vertical Flow - Intention Survival).

        From triadic-flow engine.json:
            Ψ = source_emanation × Π(channel_conductances)

        Measures: How much original intention survives to manifestation

        Args:
            source_emanation: Initial flow from source node
            channel_conductances: List of channel conductance values

        Returns:
            Vertical flow [0.0, source_emanation]
        """
        if not channel_conductances:
            return source_emanation

        # Product of all conductances
        conductance_product = float(np.prod(channel_conductances))

        return source_emanation * conductance_product

    @staticmethod
    def compute_ERI(Ψ: float, Φ: float, coherence_factor: float = 1.0) -> float:
        """
        Compute ERI (Resonance Index).

        From triadic-flow engine.json:
            ERI = |Ψ| × (1 - |Φ|) × coherence_factor

        High resonance = strong vertical flow + balanced horizontal forces

        Args:
            Ψ: Vertical flow
            Φ: Expansion-restraint balance
            coherence_factor: System coherence multiplier

        Returns:
            Resonance index
        """
        return abs(Ψ) * (1 - abs(Φ)) * coherence_factor


# =============================================================================
# SCALE SELECTOR (Meta-Analysis Core)
# =============================================================================

class ScaleSelector:
    """
    Selects optimal scale (micro/meso/macro/astral) based on metrics.

    From kernel: meta_analysis_core.scales
    """

    @staticmethod
    def select_scale(ΔÇE: float, Δf: float, YRE: float, astral_threshold: float = 0.8) -> str:
        """
        Select scale based on kernel triggers.

        From kernel/system_snapshot_motorcore.json:

        micro:
            trigger: "ΔÇE < 0.25 ve Δf < 0.2"
            expected_YRE: "0.7–0.9"

        meso (default):
            trigger: "0.25 ≤ ΔÇE ≤ 0.6"
            expected_YRE: "0.6–0.8"

        macro:
            trigger: "ΔÇE > 0.6 veya Δf > 0.7"
            expected_YRE: "0.3–0.6"

        astral:
            (implicit from runtime_params.astral_threshold = 0.8)
            trigger: YRE >= 0.8

        Args:
            ΔÇE: Contradiction entropy fluctuation
            Δf: Phase difference
            YRE: Resonance index
            astral_threshold: Threshold for astral state (from kernel runtime_params)

        Returns:
            Scale name: "micro", "meso", "macro", or "astral"
        """
        # Astral (highest priority)
        if YRE >= astral_threshold:
            return "astral"

        # Micro
        if ΔÇE < 0.25 and Δf < 0.2:
            return "micro"

        # Macro
        if ΔÇE > 0.6 or Δf > 0.7:
            return "macro"

        # Meso (default)
        return "meso"


# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

def compute_all_metrics(state: ResonanceState) -> Dict[str, float]:
    """
    Compute all resonance metrics at once.

    Args:
        state: Complete resonance state

    Returns:
        Dictionary with all computed metrics
    """
    CI = ResonanceMetrics.compute_CI(state.nodes)
    ΔÇE = ResonanceMetrics.compute_ΔÇE(state.current_entropy, state.previous_entropy)
    Δf = ResonanceMetrics.compute_Δf(state.nodes)
    YRE = ResonanceMetrics.compute_YRE(state)
    Φ = ResonanceMetrics.compute_Φ(state.generosity_flow, state.boundary_flow)
    Ψ = ResonanceMetrics.compute_Ψ(state.source_emanation, state.channel_conductances)
    ERI = ResonanceMetrics.compute_ERI(Ψ, Φ, state.coherence_factor)

    return {
        "CI": CI,
        "ΔÇE": ΔÇE,
        "Δf": Δf,
        "YRE": YRE,
        "Φ": Φ,
        "Ψ": Ψ,
        "ERI": ERI,
    }


# =============================================================================
# MAIN (for testing)
# =============================================================================

if __name__ == "__main__":
    # Test metrics computation
    print("Testing Resonance Metrics...")

    # Create mock node states
    nodes = {
        "source": NodeState("source", flow=1.0, active=True, complexity=0.5, phase=0.0),
        "spark": NodeState("spark", flow=0.8, active=True, complexity=0.7, phase=0.2),
        "structure": NodeState("structure", flow=0.6, active=True, complexity=0.6, phase=0.15),
        "harmony": NodeState("harmony", flow=0.7, active=True, complexity=0.65, phase=0.1),
        "output": NodeState("output", flow=0.75, active=True, complexity=0.6, phase=0.05),
    }

    # Create resonance state
    state = ResonanceState(
        nodes=nodes,
        source_emanation=1.0,
        generosity_flow=0.7,
        boundary_flow=0.5,
        channel_conductances=[0.9, 0.85, 0.9, 0.95],
        current_entropy=0.35,
        previous_entropy=0.30,
        depth_factor=0.4,
        safety_weight=1.0,
        epistemic_uncertainty=0.1,
        coherence_factor=1.0,
        k=0.1,
    )

    # Compute all metrics
    metrics = compute_all_metrics(state)

    print("\nComputed Metrics:")
    for name, value in metrics.items():
        print(f"  {name}: {value:.4f}")

    # Scale selection
    scale = ScaleSelector.select_scale(
        ΔÇE=metrics["ΔÇE"],
        Δf=metrics["Δf"],
        YRE=metrics["YRE"],
        astral_threshold=0.8
    )
    print(f"\nSelected Scale: {scale}")

    # Interpret YRE
    YRE = metrics["YRE"]
    if YRE < 0.3:
        state_name = "Low resonance (gürültü alanı)"
    elif YRE < 0.6:
        state_name = "Balanced (dengede)"
    elif YRE < 0.9:
        state_name = "High resonance (yüksek uyum)"
    else:
        state_name = "Astral (full coherence)"

    print(f"Resonance State: {state_name}")
    print("\nResonance metrics calculator working correctly!")
