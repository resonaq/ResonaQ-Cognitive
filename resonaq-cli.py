"""
ResonaQ CLI - Command Line Interface

Simple CLI for testing ResonaQ cognitive architecture.

Usage:
    python resonaq-cli.py

Philosophy:
- Not a vibe coding assistant
- Enforces bio-rhythm cycle (4 phases)
- Maintains relationship between intention and output
- Computes and displays resonance metrics

Example session:
    > Hello, how are you?
    [Phase 1: Sentiment Scan] sentiment=0.5
    [Phase 2: Direct Link] vulnerability=0.2
    [Phase 3: Process Pause - Ma] YRE=0.65
    [Phase 4: Response Modulation] factor=0.7
    Assistant: [response]
"""

import sys
import os
from pathlib import Path

# Add runtime to path
runtime_path = Path(__file__).parent / "runtime"
sys.path.insert(0, str(runtime_path))

from runtime.kernel_loader import load_kernel
from runtime.bio_rhythm_graph import BioRhythmGraph, BioRhythmConfig
from runtime.resonance_metrics import compute_all_metrics, ScaleSelector, ResonanceState


# =============================================================================
# CLI APPLICATION
# =============================================================================

class ResonaQCLI:
    """
    Command-line interface for ResonaQ.

    Demonstrates:
    - Bio-rhythm cycle execution
    - Resonance metric computation
    - Relationship preservation
    """

    def __init__(self, verbose: bool = True):
        """
        Initialize CLI.

        Args:
            verbose: If True, show detailed phase information
        """
        self.verbose = verbose

        # Load kernel
        print("Loading kernel...")
        try:
            self.kernel = load_kernel()
            print(f"[OK] Kernel loaded: {self.kernel.version}")
            print(f"     Codename: {self.kernel.codename}")
            print()
        except Exception as e:
            print(f"[ERROR] Error loading kernel: {e}")
            sys.exit(1)

        # Create bio-rhythm graph
        print("Initializing bio-rhythm graph...")
        config = BioRhythmConfig()
        self.bio_rhythm = BioRhythmGraph(config)
        self.app = self.bio_rhythm.compile()
        print("[OK] Bio-rhythm graph ready")
        print()

        # Session state
        self.conversation_history = []
        self.turn_count = 0

    def process_message(self, user_message: str) -> dict:
        """
        Process user message through bio-rhythm cycle.

        Args:
            user_message: User input

        Returns:
            Result dictionary with phase outputs and metrics
        """
        self.turn_count += 1

        # Prepare input
        input_state = {
            "user_message": user_message,
            "source_intention": user_message,  # First turn = intention
            "conversation_history": self.conversation_history,
            "metadata": {
                "turn": self.turn_count,
            },
        }

        # Run bio-rhythm cycle
        if self.verbose:
            print("=== Bio-Rhythm Cycle ===========================")

        result = self.app.invoke(input_state)

        if self.verbose:
            # Phase results
            print("  Phase 1 (Sentiment Scan)")
            print(f"    Sentiment: {result['sentiment_score']:.3f}")
            print(f"    Safety buffer: {'ACTIVE' if result['safety_buffer_active'] else 'inactive'}")
            print()
            print("  Phase 2 (Direct Link)")
            print(f"    Vulnerability: {result['vulnerability']:.3f}")
            print(f"    Complexity (CI): {result['CI']:.3f}")
            print()
            print("  Phase 3 (Process Pause - Ma)")
            print(f"    Pause duration: {result['pause_duration']:.1f}s")
            print(f"    YRE (resonance): {result['YRE']:.3f}")
            print(f"    Intention preserved: {result['intention_preserved']:.3f}")
            print()
            print("  Phase 4 (Response Modulation)")
            print(f"    Modulation factor: {result['modulation_factor']:.3f}")
            print("================================================")
            print()

        # Update conversation history
        self.conversation_history.append({
            "role": "user",
            "content": user_message,
        })

        # In full system, this would generate actual LLM response
        # For now, we'll create a mock response based on metrics
        response = self._generate_mock_response(result)

        self.conversation_history.append({
            "role": "assistant",
            "content": response,
        })

        result["assistant_response"] = response
        return result

    def _generate_mock_response(self, bio_rhythm_result: dict) -> str:
        """
        Generate mock response based on bio-rhythm metrics.

        In full system, this would pass metrics to LLM.
        """
        vulnerability = bio_rhythm_result["vulnerability"]
        safety_buffer = bio_rhythm_result["safety_buffer_active"]
        modulation = bio_rhythm_result["modulation_factor"]
        YRE = bio_rhythm_result["YRE"]

        # Different response styles based on metrics
        if safety_buffer or vulnerability > 0.7:
            # Protective, supportive
            return (
                "I hear you, and I'm here. It's okay to feel this way. "
                "Let's take this one step at a time."
            )
        elif YRE >= 0.8:
            # Astral - can be direct and deep
            return (
                "There's a clarity in what you're asking. "
                "Let's explore this together with full presence."
            )
        elif modulation < 0.6:
            # Conservative
            return (
                "I understand what you're sharing. "
                "How would you like to proceed?"
            )
        else:
            # Balanced
            return (
                "I'm processing what you've said. "
                "There are a few directions we could take here."
            )

    def run_interactive(self):
        """Run interactive CLI session"""
        print("=" * 60)
        print("ResonaQ Interactive Session")
        print("=" * 60)
        print()
        print("Philosophy:")
        print("  - 4-phase bio-rhythm cycle (no vibe coding shortcuts)")
        print("  - Resonance metrics computed at each step")
        print("  - Relationship between intention and output preserved")
        print()
        print("Commands:")
        print("  /verbose - Toggle detailed phase output")
        print("  /metrics - Show resonance metrics")
        print("  /quit    - Exit")
        print()
        print("Type your message and press Enter...")
        print()

        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()

                if not user_input:
                    continue

                # Handle commands
                if user_input.startswith("/"):
                    if user_input == "/quit":
                        print("\nGoodbye!")
                        break
                    elif user_input == "/verbose":
                        self.verbose = not self.verbose
                        print(f"Verbose mode: {'ON' if self.verbose else 'OFF'}")
                        continue
                    elif user_input == "/metrics":
                        self._show_metrics_summary()
                        continue
                    else:
                        print(f"Unknown command: {user_input}")
                        continue

                # Process message
                result = self.process_message(user_input)

                # Show response
                print(f"ResonaQ: {result['assistant_response']}")
                print()

                # Show resonance state
                if result['YRE'] >= 0.9:
                    print("  [Resonance: ASTRAL - full coherence]")
                elif result['YRE'] >= 0.6:
                    print("  [Resonance: HIGH]")
                elif result['YRE'] >= 0.3:
                    print("  [Resonance: Balanced]")
                else:
                    print("  [Resonance: Low - noise zone]")
                print()

            except KeyboardInterrupt:
                print("\n\nInterrupted. Goodbye!")
                break
            except Exception as e:
                print(f"\nError: {e}")
                import traceback
                traceback.print_exc()

    def _show_metrics_summary(self):
        """Show resonance metrics summary"""
        if not self.conversation_history:
            print("No conversation history yet.")
            return

        print()
        print("=" * 60)
        print("Resonance Metrics Summary")
        print("=" * 60)
        print(f"Turns: {self.turn_count}")
        print()
        print("This would show:")
        print("  - YRE trend over conversation")
        print("  - ΔÇE (contradiction entropy) evolution")
        print("  - Φ (expansion-restraint balance)")
        print("  - Ψ (intention preservation / vertical flow)")
        print("  - Scale selection history (micro/meso/macro/astral)")
        print()
        print("(Full implementation pending)")
        print()


# =============================================================================
# MAIN
# =============================================================================

def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="ResonaQ CLI - Cognitive Architecture Interface"
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Disable verbose phase output"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run single test message and exit"
    )

    args = parser.parse_args()

    # Create CLI
    cli = ResonaQCLI(verbose=not args.quiet)

    if args.test:
        # Test mode - single message
        print("Running test message...")
        print()
        result = cli.process_message("Hello, I'm feeling a bit overwhelmed today")
        print(f"Response: {result['assistant_response']}")
        print()
        print("[OK] Test completed")
    else:
        # Interactive mode
        cli.run_interactive()


if __name__ == "__main__":
    main()
