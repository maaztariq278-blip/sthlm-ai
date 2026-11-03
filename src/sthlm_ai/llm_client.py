import os
import json
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
USE_DUMMY = os.getenv("USE_DUMMY_API", "true").lower() == "true"

def ask_structured(system: str, user: str) -> dict:
    # If dummy mode is enabled, return simulated responses for testing!
    if USE_DUMMY:
        user_lower = user.lower()
        if "tomorrow" in user_lower or "rain" in user_lower:
            return {"intent": "forecast", "location": "Stockholm", "days_ahead": 1, "confidence": 0.98}
        elif "last week" in user_lower or "temperature" in user_lower:
            return {"intent": "history", "location": "Stockholm", "days_ahead": None, "confidence": 0.95}
        else:
            return {"intent": "unknown", "location": "Stockholm", "days_ahead": None, "confidence": 0.99}

    # Otherwise, call the real OpenAI API
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.2
    }
    
    r = httpx.post(f"{BASE_URL}/chat/completions", headers=headers, json=payload, timeout=30)
    r.raise_for_status()
    content = r.json()["choices"][0]["message"]["content"]
    return json.loads(content)