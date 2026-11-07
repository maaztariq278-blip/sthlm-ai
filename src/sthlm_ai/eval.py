import json
from pathlib import Path
from sthlm_ai.weather_intent import classify

def run_eval(file_path: str = "evals/questions.jsonl"):
    correct = 0
    total = 0
    path = Path(file_path)
    
    with path.open() as f:
        for line in f:
            item = json.loads(line)
            result = classify(item["text"])
            predicted = result.get("intent")
            expected = item["expected_intent"]
            total += 1
            
            if predicted == expected:
                correct += 1
            else:
                print(f"Wrong: '{item['text']}' predicted={predicted}, expected={expected}")
                
    accuracy = correct / total if total else 0
    print(f"\nAccuracy: {correct}/{total} ({accuracy:.0%})")

if __name__ == "__main__":
    run_eval()