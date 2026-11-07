from fastapi import FastAPI
from pydantic import BaseModel
from sthlm_ai.weather_intent import classify

# Create the FastAPI application
app = FastAPI(title="Stockholm Weather Intent API")

# Define what the request body should look like
class Question(BaseModel):
    text: str

# Define the endpoint
@app.post("/classify")
def classify_question(question: Question):
    """Receive a question and return the classified intent."""
    result = classify(question.text)
    return result