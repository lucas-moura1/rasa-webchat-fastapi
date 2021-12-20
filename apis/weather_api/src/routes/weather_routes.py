import logging

from fastapi import Request

from src.controllers import WeatherController
from src import app

@app.get("/api/health")
def health_root():
    return {"Status": "UP"}


@app.get("/api/weather")
def health_root(city: str, day: str = ""):

    weather_data = WeatherController.get_weather_forecast(city, day)

    return weather_data

