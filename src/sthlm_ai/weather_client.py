import httpx

STOCKHOLM_LAT = 59.3428
STOCKHOLM_LON = 18.0570

def get_current_weather():
    """Fetch current weather for Stockholm."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": STOCKHOLM_LAT,
        "longitude": STOCKHOLM_LON,
        "current": "temperature_2m,precipitation,weather_code"
    }
    r = httpx.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def get_historical_weather(days: int = 7):
    """Fetch historical weather for the last N days."""
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": STOCKHOLM_LAT,
        "longitude": STOCKHOLM_LON,
        "start_date": "2024-10-01",
        "end_date": "2024-10-07",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum"
    }
    r = httpx.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()