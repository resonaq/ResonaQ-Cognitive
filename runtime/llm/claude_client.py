"""
Claude API Client - Anthropic Integration

Philosophy:
- LLM is not a vibe-coding tool - it's a partner in cognitive process
- Maintains intention→output relationship (Ψ - vertical flow)
- Respects bio-rhythm phases (no rushing to output)
- Preserves conversation history for ΔÇE computation
- Supports streaming for process observation

Safety:
- Respects kernel safety_buffer_rule
- Vulnerable states modulate generation parameters
- Epistemic uncertainty tracking
"""

import os
from typing import Optional, List, Dict, Any, AsyncIterator
from dataclasses import dataclass, field
from datetime import datetime
import asyncio

try:
    from anthropic import Anthropic, AsyncAnthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("Warning: anthropic package not installed. Install with: pip install anthropic")


# =============================================================================
# MESSAGE TYPES
# =============================================================================

@dataclass
class Message:
    """
    Single message in conversation.

    Preserves not just content but also metadata for resonance computation.
    """
    role: str  # "user" or "assistant"
    content: str
    timestamp: datetime = field(default_factory=datetime.now)

    # Resonance metadata
    sentiment: Optional[float] = None  # For bio-rhythm sentiment_scan
    vulnerability: Optional[float] = None  # For safety_buffer_rule
    complexity: Optional[float] = None  # For CI computation

    def to_anthropic_format(self) -> Dict[str, str]:
        """Convert to Anthropic API format"""
        return {
            "role": self.role,
            "content": self.content
        }


@dataclass
class ConversationState:
    """
    Maintains conversation history and resonance state.

    This is not just for LLM context - it's for preserving the
    obligation chain (write → recognize → see deficiency → return).
    """
    messages: List[Message] = field(default_factory=list)

    # Resonance tracking
    previous_entropy: float = 0.0  # For ΔÇE computation
    current_entropy: float = 0.0

    # Bio-rhythm state
    current_phase: Optional[str] = None  # Which phase we're in

    # Intention tracking (for Ψ - vertical flow)
    source_intention: Optional[str] = None  # Original user intent

    def add_message(self, message: Message) -> None:
        """Add message and update resonance state"""
        self.messages.append(message)

        # Update entropy (simplified - real version would compute from content)
        if message.complexity is not None:
            self.previous_entropy = self.current_entropy
            self.current_entropy = message.complexity

    def get_recent_messages(self, n: int = 10) -> List[Message]:
        """Get last N messages for context"""
        return self.messages[-n:]

    def to_anthropic_format(self) -> List[Dict[str, str]]:
        """Convert conversation to Anthropic API format"""
        return [msg.to_anthropic_format() for msg in self.messages]


# =============================================================================
# CLAUDE CLIENT
# =============================================================================

class ClaudeClient:
    """
    Claude API client for ResonaQ.

    Philosophy:
    - Not a simple API wrapper
    - Maintains relationship between intention and output
    - Respects cognitive architecture constraints
    - Preserves obligation chain

    Usage:
        client = ClaudeClient(api_key="...")

        # Simple call
        response = client.generate("Hello, how are you?")

        # With conversation state
        state = ConversationState()
        response = client.generate_with_state("Hello", state)

        # Streaming (for process observation)
        async for chunk in client.stream("Explain quantum physics"):
            print(chunk, end="")
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "claude-sonnet-4-5-20250929",
        max_tokens: int = 4096,
        temperature: float = 1.0,
        process_pause_delay: float = 0.0,  # Bio-rhythm "Ma" - breathing room
    ):
        """
        Initialize Claude client.

        Args:
            api_key: Anthropic API key (if None, reads from ANTHROPIC_API_KEY env var)
            model: Claude model to use
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            process_pause_delay: Delay before generation (bio-rhythm "Ma" phase)
        """
        if not ANTHROPIC_AVAILABLE:
            raise ImportError(
                "anthropic package not installed. "
                "Install with: pip install anthropic"
            )

        # API key
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "No API key provided. Set ANTHROPIC_API_KEY environment variable "
                "or pass api_key parameter."
            )

        # Clients
        self.client = Anthropic(api_key=self.api_key)
        self.async_client = AsyncAnthropic(api_key=self.api_key)

        # Configuration
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.process_pause_delay = process_pause_delay

        # Conversation states (keyed by session_id)
        self.conversations: Dict[str, ConversationState] = {}

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
    ) -> str:
        """
        Generate response (synchronous).

        Args:
            prompt: User prompt
            system_prompt: Optional system prompt
            temperature: Optional temperature override
            max_tokens: Optional max tokens override

        Returns:
            Generated response text
        """
        # Use defaults if not specified
        temp = temperature if temperature is not None else self.temperature
        tokens = max_tokens if max_tokens is not None else self.max_tokens

        # Build messages
        messages = [{"role": "user", "content": prompt}]

        # API call
        kwargs = {
            "model": self.model,
            "max_tokens": tokens,
            "temperature": temp,
            "messages": messages,
        }

        if system_prompt:
            kwargs["system"] = system_prompt

        response = self.client.messages.create(**kwargs)

        # Extract text
        return response.content[0].text

    def generate_with_state(
        self,
        prompt: str,
        state: ConversationState,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        # Resonance parameters
        sentiment: Optional[float] = None,
        vulnerability: Optional[float] = None,
        complexity: Optional[float] = None,
    ) -> str:
        """
        Generate response with conversation state tracking.

        This maintains the obligation chain - conversation history is preserved
        for ΔÇE (contradiction entropy) computation.

        Args:
            prompt: User prompt
            state: Conversation state to maintain
            system_prompt: Optional system prompt
            temperature: Optional temperature override
            max_tokens: Optional max tokens override
            sentiment: Optional sentiment score (for bio-rhythm)
            vulnerability: Optional vulnerability score (for safety_buffer_rule)
            complexity: Optional complexity score (for CI)

        Returns:
            Generated response text
        """
        # Add user message to state
        user_msg = Message(
            role="user",
            content=prompt,
            sentiment=sentiment,
            vulnerability=vulnerability,
            complexity=complexity,
        )
        state.add_message(user_msg)

        # Track source intention (for Ψ - vertical flow)
        if state.source_intention is None:
            state.source_intention = prompt

        # Apply safety modulation
        temp = temperature if temperature is not None else self.temperature
        tokens = max_tokens if max_tokens is not None else self.max_tokens

        # Safety buffer rule: if vulnerability high, reduce temperature
        if vulnerability is not None and vulnerability > 0.7:
            temp = min(temp, 0.7)  # More conservative generation

        # Build messages from state
        messages = state.to_anthropic_format()

        # API call
        kwargs = {
            "model": self.model,
            "max_tokens": tokens,
            "temperature": temp,
            "messages": messages,
        }

        if system_prompt:
            kwargs["system"] = system_prompt

        response = self.client.messages.create(**kwargs)

        # Extract text
        response_text = response.content[0].text

        # Add assistant message to state
        assistant_msg = Message(
            role="assistant",
            content=response_text,
        )
        state.add_message(assistant_msg)

        return response_text

    async def agenerate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
    ) -> str:
        """
        Generate response (asynchronous).

        Includes process_pause_delay for bio-rhythm "Ma" phase.
        """
        # Process pause (bio-rhythm breathing room)
        if self.process_pause_delay > 0:
            await asyncio.sleep(self.process_pause_delay)

        # Use defaults if not specified
        temp = temperature if temperature is not None else self.temperature
        tokens = max_tokens if max_tokens is not None else self.max_tokens

        # Build messages
        messages = [{"role": "user", "content": prompt}]

        # API call
        kwargs = {
            "model": self.model,
            "max_tokens": tokens,
            "temperature": temp,
            "messages": messages,
        }

        if system_prompt:
            kwargs["system"] = system_prompt

        response = await self.async_client.messages.create(**kwargs)

        # Extract text
        return response.content[0].text

    async def stream(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
    ) -> AsyncIterator[str]:
        """
        Stream response (asynchronous).

        This allows observation of the generation process, not just consumption
        of the final output. Maintains relationship with the emerging text.

        Usage:
            async for chunk in client.stream("Explain AI"):
                print(chunk, end="")
        """
        # Process pause
        if self.process_pause_delay > 0:
            await asyncio.sleep(self.process_pause_delay)

        # Use defaults
        temp = temperature if temperature is not None else self.temperature
        tokens = max_tokens if max_tokens is not None else self.max_tokens

        # Build messages
        messages = [{"role": "user", "content": prompt}]

        # API call
        kwargs = {
            "model": self.model,
            "max_tokens": tokens,
            "temperature": temp,
            "messages": messages,
        }

        if system_prompt:
            kwargs["system"] = system_prompt

        # Stream
        async with self.async_client.messages.stream(**kwargs) as stream:
            async for text in stream.text_stream:
                yield text

    def get_or_create_conversation(self, session_id: str) -> ConversationState:
        """
        Get or create conversation state for session.

        Maintains relationship across turns.
        """
        if session_id not in self.conversations:
            self.conversations[session_id] = ConversationState()
        return self.conversations[session_id]

    def clear_conversation(self, session_id: str) -> None:
        """Clear conversation history"""
        if session_id in self.conversations:
            del self.conversations[session_id]


# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

def create_client(
    api_key: Optional[str] = None,
    model: str = "claude-sonnet-4-5-20250929",
    **kwargs
) -> ClaudeClient:
    """
    Create Claude client with sensible defaults.

    Args:
        api_key: Anthropic API key
        model: Claude model
        **kwargs: Additional arguments for ClaudeClient

    Returns:
        Configured ClaudeClient
    """
    return ClaudeClient(api_key=api_key, model=model, **kwargs)


# =============================================================================
# MAIN (for testing)
# =============================================================================

if __name__ == "__main__":
    import asyncio

    print("Testing Claude Client...")

    # Check API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("\nError: ANTHROPIC_API_KEY not set")
        print("Set it with: export ANTHROPIC_API_KEY=your_key_here")
        exit(1)

    # Create client
    client = ClaudeClient()

    # Test 1: Simple generation
    print("\n=== Test 1: Simple Generation ===")
    response = client.generate("Say hello in Turkish")
    print(f"Response: {response}")

    # Test 2: With conversation state
    print("\n=== Test 2: Conversation State ===")
    state = ConversationState()

    response1 = client.generate_with_state(
        "My name is ResonaQ",
        state,
        sentiment=0.5,
        vulnerability=0.3,
        complexity=0.4,
    )
    print(f"Turn 1: {response1}")

    response2 = client.generate_with_state(
        "What's my name?",
        state,
        sentiment=0.5,
        vulnerability=0.2,
        complexity=0.2,
    )
    print(f"Turn 2: {response2}")

    print(f"\nConversation has {len(state.messages)} messages")
    print(f"ΔÇE (entropy change): {abs(state.current_entropy - state.previous_entropy):.4f}")

    # Test 3: Streaming (async)
    print("\n=== Test 3: Streaming ===")

    async def test_streaming():
        print("Streaming response: ", end="")
        async for chunk in client.stream("Count to 5 in Turkish"):
            print(chunk, end="", flush=True)
        print()  # Newline

    asyncio.run(test_streaming())

    # Test 4: Safety modulation
    print("\n=== Test 4: Safety Modulation (High Vulnerability) ===")
    state_vulnerable = ConversationState()

    response = client.generate_with_state(
        "Tell me something reassuring",
        state_vulnerable,
        vulnerability=0.9,  # High vulnerability triggers safety modulation
    )
    print(f"Response (modulated): {response}")

    print("\nClaude client working correctly!")
