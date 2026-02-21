"""
Bio-Rhythm Graph - 4-Phase Cognitive Cycle

Implements the core bio-rhythm cycle from kernel:
    1. Sentiment Scan (Inhale) - Emotional sensing
    2. Direct Link (Limbic) - Vulnerability detection
    3. Process Pause (Ma) - Meaning gap, deliberation
    4. Response Modulation (Exhale) - Output tonality

Philosophy:
- PREVENTS vibe coding - you cannot skip to output
- ENFORCES deliberation - Ma (process pause) is mandatory
- MAINTAINS relationship - each phase builds on previous
- COMPUTES resonance - YRE, CI, ΔÇE, Φ at each step

This is the "obligation chain" enforcer:
    Input → Sense → Link → Pause → Modulate → Output
    (Each step MUST happen - no shortcuts)

Contrast with vibe coding:
    Vibe: Prompt → [Black box] → Output (relationship lost)
    Bio-rhythm: Input → 4 phases → Output (relationship preserved)
"""

from typing import TypedDict, Annotated, Optional, Dict, Any, List
from dataclasses import dataclass, field
from datetime import datetime
import operator

try:
    from langgraph.graph import StateGraph, START, END
    from langgraph.checkpoint.memory import MemorySaver
    LANGGRAPH_AVAILABLE = True
except ImportError:
    LANGGRAPH_AVAILABLE = False
    print("Warning: langgraph not installed. Install with: pip install langgraph")


# =============================================================================
# STATE DEFINITION
# =============================================================================

class BioRhythmState(TypedDict):
    """
    State maintained through bio-rhythm cycle.

    This is not just LLM context - it's the RELATIONSHIP state.
    Each field tracks part of the obligation chain.
    """
    # Input/output
    user_message: str
    assistant_response: str

    # Current phase
    phase: str  # Which phase we're in
    phase_index: int  # 0-3 index

    # Bio-rhythm measurements
    sentiment_score: float  # From phase 1
    vulnerability: float  # From phase 2
    pause_duration: float  # From phase 3 (Ma)
    modulation_factor: float  # From phase 4

    # Resonance metrics (computed during cycle)
    YRE: float  # Yankı Rezonans Endeksi
    CI: float  # Complexity Index
    ΔÇE: float  # Contradiction Entropy Change
    Δf: float  # Phase difference

    # Intention tracking (for Ψ - vertical flow)
    source_intention: str  # Original user intent
    intention_preserved: float  # How much intention survived (0-1)

    # Context
    conversation_history: Annotated[List[Dict[str, str]], operator.add]
    metadata: Dict[str, Any]

    # Safety
    safety_buffer_active: bool  # If sentiment < -0.6


@dataclass
class BioRhythmConfig:
    """
    Configuration for bio-rhythm cycle.

    Loaded from kernel configuration.
    """
    # Phase names (from kernel)
    phase_names: List[str] = field(default_factory=lambda: [
        "1_sentiment_scan",
        "2_direct_link",
        "3_process_pause",
        "4_response_modulation"
    ])

    # Delays (enforcing deliberation)
    phase_delays: Dict[str, float] = field(default_factory=lambda: {
        "1_sentiment_scan": 0.0,  # No delay for sensing
        "2_direct_link": 0.0,  # No delay for linking
        "3_process_pause": 1.0,  # Ma - mandatory pause (seconds)
        "4_response_modulation": 0.0,  # No delay for output
    })

    # Safety thresholds (from kernel)
    sentiment_threshold: float = -0.6  # Below this = safety buffer
    vulnerability_threshold: float = 0.7  # Above this = protective mode

    # Resonance thresholds
    astral_threshold: float = 0.8  # YRE >= 0.8 = astral state


# =============================================================================
# BIO-RHYTHM GRAPH
# =============================================================================

class BioRhythmGraph:
    """
    4-phase bio-rhythm cycle implemented as LangGraph StateGraph.

    Usage:
        config = BioRhythmConfig()
        graph = BioRhythmGraph(config)
        app = graph.compile()

        # Run cycle
        result = app.invoke({
            "user_message": "Hello, how are you?",
            "source_intention": "Greeting"
        })

    Philosophy:
    - Each phase MUST execute (no skipping)
    - Process pause (Ma) is MANDATORY
    - Resonance computed at each step
    - Prevents vibe coding by design
    """

    def __init__(self, config: Optional[BioRhythmConfig] = None):
        """
        Initialize bio-rhythm graph.

        Args:
            config: Bio-rhythm configuration (default if None)
        """
        if not LANGGRAPH_AVAILABLE:
            raise ImportError("langgraph not installed. Install with: pip install langgraph")

        self.config = config or BioRhythmConfig()

        # Build graph
        self.graph = StateGraph(BioRhythmState)
        self._build_graph()

    def _build_graph(self):
        """
        Build 4-phase state graph.

        Topology:
            START → Sentiment Scan → Direct Link → Process Pause → Response Modulation → END

        Each phase is MANDATORY - no conditional edges that skip phases.
        This is the anti-vibe-coding architecture.
        """
        # Add nodes for each phase
        self.graph.add_node("sentiment_scan", self.phase_1_sentiment_scan)
        self.graph.add_node("direct_link", self.phase_2_direct_link)
        self.graph.add_node("process_pause", self.phase_3_process_pause)
        self.graph.add_node("response_modulation", self.phase_4_response_modulation)

        # Connect phases (LINEAR - no skipping allowed)
        self.graph.add_edge(START, "sentiment_scan")
        self.graph.add_edge("sentiment_scan", "direct_link")
        self.graph.add_edge("direct_link", "process_pause")
        self.graph.add_edge("process_pause", "response_modulation")
        self.graph.add_edge("response_modulation", END)

    def phase_1_sentiment_scan(self, state: BioRhythmState) -> Dict[str, Any]:
        """
        Phase 1: Sentiment Scan (Inhale)

        From kernel: "Duygu Taraması - kullanıcı mesajının duygusal yükünü ölç"

        Purpose:
        - Detect emotional tone
        - Identify vulnerability signals
        - Set baseline for safety_buffer_rule

        Implementation:
        - Simple keyword-based (full NLP would require another model)
        - Looks for positive/negative/neutral markers
        - Computes sentiment score [-1, +1]
        """
        message = state["user_message"]

        # Simple sentiment analysis (placeholder - real version would use model)
        sentiment_score = self._compute_sentiment(message)

        # Check safety buffer rule
        safety_buffer_active = sentiment_score < self.config.sentiment_threshold

        updates = {
            "phase": self.config.phase_names[0],
            "phase_index": 0,
            "sentiment_score": sentiment_score,
            "safety_buffer_active": safety_buffer_active,
            "metadata": {
                **state.get("metadata", {}),
                "phase_1_timestamp": datetime.now().isoformat(),
            }
        }

        return updates

    def phase_2_direct_link(self, state: BioRhythmState) -> Dict[str, Any]:
        """
        Phase 2: Direct Link (Limbic Connection)

        From kernel: "Limbik Bağlantı - vulnerability tespit, empati kurma"

        Purpose:
        - Detect vulnerability level
        - Establish emotional connection
        - Determine if protective mode needed

        This phase answers: "Is the user in a vulnerable state?"
        If yes, subsequent phases will modulate accordingly.
        """
        message = state["user_message"]
        sentiment = state["sentiment_score"]

        # Vulnerability detection (placeholder)
        vulnerability = self._compute_vulnerability(message, sentiment)

        # Update resonance metrics
        CI = self._compute_complexity(message)

        updates = {
            "phase": self.config.phase_names[1],
            "phase_index": 1,
            "vulnerability": vulnerability,
            "CI": CI,
            "metadata": {
                **state.get("metadata", {}),
                "phase_2_timestamp": datetime.now().isoformat(),
            }
        }

        return updates

    def phase_3_process_pause(self, state: BioRhythmState) -> Dict[str, Any]:
        """
        Phase 3: Process Pause (Ma - Meaning Gap)

        From kernel: "Anlam Boşluğu - yanıt üretme öncesi nefes"

        Purpose:
        - MANDATORY PAUSE - prevents rushing to output
        - Allow complexity to settle
        - Compute resonance metrics
        - This is the ANTI-VIBE-CODING phase

        Philosophy:
        "Ma" (間) - Japanese concept of negative space, pause, breath.
        In music: the silence between notes.
        In ResonaQ: the deliberation before response.

        Vibe coding skips this. ResonaQ enforces it.
        """
        import time

        # Enforce pause (Ma)
        pause_duration = self.config.phase_delays["3_process_pause"]
        if pause_duration > 0:
            time.sleep(pause_duration)

        # Compute resonance metrics during pause
        # (This is when we CHECK the relationship, not just rush through)

        # ΔÇE (contradiction entropy change)
        current_entropy = state.get("CI", 0.0)
        previous_entropy = state.get("metadata", {}).get("previous_entropy", 0.0)
        ΔÇE = abs(current_entropy - previous_entropy)

        # Δf (phase difference) - placeholder
        Δf = self._compute_phase_difference(state)

        # YRE (resonance index) - simplified computation
        CI = state.get("CI", 0.0)
        k = 0.1
        ε_AI = 0.1  # Epistemic uncertainty (placeholder)
        DF = state.get("vulnerability", 0.0)  # Depth factor
        safety_weight = 1.0

        numerator = CI * (1 - abs(ΔÇE)) + k * abs(ε_AI)
        denominator = 1 + (DF * safety_weight) * (2.71828 ** (-abs(Δf)))
        YRE = numerator / denominator if denominator > 0 else 0.0

        # Intention preservation (Ψ - vertical flow)
        # How much of source intention is preserved?
        intention_preserved = self._compute_intention_preservation(state)

        updates = {
            "phase": self.config.phase_names[2],
            "phase_index": 2,
            "pause_duration": pause_duration,
            "ΔÇE": ΔÇE,
            "Δf": Δf,
            "YRE": YRE,
            "intention_preserved": intention_preserved,
            "metadata": {
                **state.get("metadata", {}),
                "phase_3_timestamp": datetime.now().isoformat(),
                "previous_entropy": current_entropy,
            }
        }

        return updates

    def phase_4_response_modulation(self, state: BioRhythmState) -> Dict[str, Any]:
        """
        Phase 4: Response Modulation (Exhale)

        From kernel: "Çıktı Tonlaması - ton, üslup, format ayarlama"

        Purpose:
        - Adjust response tone based on sentiment/vulnerability
        - Apply safety buffer if needed
        - Prepare final output

        This phase applies the lessons from phases 1-3:
        - If sentiment negative → more supportive tone
        - If vulnerability high → more protective
        - If YRE high → can be more direct
        """
        sentiment = state["sentiment_score"]
        vulnerability = state["vulnerability"]
        YRE = state.get("YRE", 0.0)
        safety_buffer = state["safety_buffer_active"]

        # Modulation factor (how much to adjust response)
        # Lower = more conservative, Higher = more direct
        if safety_buffer or vulnerability > self.config.vulnerability_threshold:
            modulation_factor = 0.5  # Conservative, supportive
        elif YRE >= self.config.astral_threshold:
            modulation_factor = 1.0  # Can be direct (astral coherence)
        else:
            modulation_factor = 0.7  # Balanced

        # In real implementation, this would pass modulation_factor to LLM
        # For now, just record it

        updates = {
            "phase": self.config.phase_names[3],
            "phase_index": 3,
            "modulation_factor": modulation_factor,
            "metadata": {
                **state.get("metadata", {}),
                "phase_4_timestamp": datetime.now().isoformat(),
            }
        }

        return updates

    # =========================================================================
    # HELPER METHODS (Placeholders - real versions would be more sophisticated)
    # =========================================================================

    def _compute_sentiment(self, message: str) -> float:
        """
        Compute sentiment score.

        Placeholder: keyword-based.
        Real version: would use sentiment model or LLM.
        """
        # Positive keywords
        positive = ["good", "great", "happy", "love", "thanks", "excellent"]
        # Negative keywords
        negative = ["bad", "sad", "hate", "angry", "terrible", "awful"]

        message_lower = message.lower()
        pos_count = sum(1 for word in positive if word in message_lower)
        neg_count = sum(1 for word in negative if word in message_lower)

        if pos_count == 0 and neg_count == 0:
            return 0.0  # Neutral

        # Simple ratio
        return (pos_count - neg_count) / (pos_count + neg_count + 1)

    def _compute_vulnerability(self, message: str, sentiment: float) -> float:
        """Compute vulnerability level"""
        # Vulnerability signals
        vulnerable_words = ["help", "scared", "worried", "confused", "lost", "alone"]

        message_lower = message.lower()
        vuln_count = sum(1 for word in vulnerable_words if word in message_lower)

        # Combine with sentiment
        base_vuln = min(1.0, vuln_count * 0.3)

        # Negative sentiment increases vulnerability
        if sentiment < 0:
            base_vuln = min(1.0, base_vuln + abs(sentiment) * 0.5)

        return base_vuln

    def _compute_complexity(self, message: str) -> float:
        """Compute message complexity (for CI)"""
        # Simple: based on length and word count
        words = message.split()
        word_count = len(words)

        if word_count < 5:
            return 0.2
        elif word_count < 15:
            return 0.5
        else:
            return 0.8

    def _compute_phase_difference(self, state: BioRhythmState) -> float:
        """Compute phase alignment (Δf)"""
        # Placeholder: would compare multiple nodes in triadic flow
        # For now, return small value
        return 0.15

    def _compute_intention_preservation(self, state: BioRhythmState) -> float:
        """
        Compute how much of original intention is preserved (Ψ factor).

        In full system, this would track intention through triadic flow.
        """
        # Placeholder: assume high preservation if not too complex
        CI = state.get("CI", 0.5)
        return max(0.0, 1.0 - CI * 0.3)

    def compile(self, checkpointer=None):
        """
        Compile graph to executable app.

        Args:
            checkpointer: Optional checkpointer for state persistence

        Returns:
            Compiled LangGraph app
        """
        return self.graph.compile(checkpointer=checkpointer)


# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

def create_bio_rhythm_graph(
    config: Optional[BioRhythmConfig] = None,
    with_memory: bool = False
) -> Any:
    """
    Create and compile bio-rhythm graph.

    Args:
        config: Optional configuration
        with_memory: If True, use MemorySaver for state persistence

    Returns:
        Compiled graph ready to invoke
    """
    graph = BioRhythmGraph(config)

    checkpointer = MemorySaver() if with_memory else None

    return graph.compile(checkpointer=checkpointer)


# =============================================================================
# MAIN (for testing)
# =============================================================================

if __name__ == "__main__":
    print("Testing Bio-Rhythm Graph...")

    # Create graph
    config = BioRhythmConfig()
    graph = BioRhythmGraph(config)
    app = graph.compile()

    # Test input
    test_input = {
        "user_message": "I'm feeling a bit lost and confused today",
        "source_intention": "Seeking support",
        "conversation_history": [],
        "metadata": {},
    }

    print("\n=== Running 4-Phase Bio-Rhythm Cycle ===")
    print(f"Input: {test_input['user_message']}")
    print()

    # Run cycle
    result = app.invoke(test_input)

    # Print results
    print("=== Results ===")
    print(f"Phase completed: {result['phase']}")
    print(f"Phase index: {result['phase_index']}")
    print()
    print(f"Sentiment score: {result['sentiment_score']:.3f}")
    print(f"Vulnerability: {result['vulnerability']:.3f}")
    print(f"Complexity (CI): {result['CI']:.3f}")
    print(f"Pause duration: {result['pause_duration']:.1f}s")
    print()
    print(f"DCE (entropy change): {result['ΔÇE']:.3f}")
    print(f"Df (phase diff): {result['Δf']:.3f}")
    print(f"YRE (resonance): {result['YRE']:.3f}")
    print(f"Intention preserved: {result['intention_preserved']:.3f}")
    print()
    print(f"Safety buffer active: {result['safety_buffer_active']}")
    print(f"Modulation factor: {result['modulation_factor']:.3f}")

    # Interpretation
    print("\n=== Interpretation ===")
    if result['YRE'] < 0.3:
        print("Resonance state: Low (noise zone)")
    elif result['YRE'] < 0.6:
        print("Resonance state: Balanced")
    elif result['YRE'] < 0.9:
        print("Resonance state: High resonance")
    else:
        print("Resonance state: ASTRAL (full coherence)")

    if result['safety_buffer_active']:
        print("Safety buffer: ACTIVE (protective mode)")
    else:
        print("Safety buffer: Inactive")

    print("\nBio-rhythm graph working correctly!")
    print("All 4 phases executed in sequence (no vibe coding shortcuts).")
