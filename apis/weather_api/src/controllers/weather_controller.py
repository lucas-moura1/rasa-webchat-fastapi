import logging

from fastapi import HTTPException

from src.utils import valitate_data_request
from src.services import WeatherService

class WeatherController:

    @staticmethod
    def get_weather_forecast(city: str, day: str) -> dict:
        logging.info("Receiving datas for getting datas weather")
        logging.debug(f"city: {city} and day: {day}")

        try:
            valitate_data_request(city, day)

            weather_data = WeatherService.get_weather_forecast(city, day)

            return weather_data
        except Exception as error:
            logging.error(f"Error => {error}")

            status_code = error.status_code
            msg = error.detail

            raise HTTPException(status_code, msg)
