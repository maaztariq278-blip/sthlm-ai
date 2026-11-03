from .llm_client import ask_structured

SYSTEM = """
You are a classifier for a Stockholm weather assistant.
Return JSON with these exact keys:
- intent: one of ["current", "forecast", "history", "unknown"]
- location: string (default "Stockholm")
- days_ahead: integer or null
- confidence: float between 0 and 1
"""

def classify(text: str) -> dict:
    return ask_structured(SYSTEM, text)

if __name__ == "__main__":
    tests = [
        "Will it rain tomorrow in Stockholm?",
        "What was the temperature last week?",
        "Hello"
    ]
    
    for t in tests:
        print(t, "->", classify(t))