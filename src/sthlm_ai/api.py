from fastapi import FastAPI
from pydantic import BaseModel
from sthlm_ai.weather_intent import classify
from sthlm_ai.weather_client import get_current_weather

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

@app.get("/weather/current")
def current_weather():
    """Return current weather in Stockholm."""
    return get_current_weather()