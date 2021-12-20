import logging

from src.utils import request_weather_api, handle_response_weather_api

class WeatherService:

    @staticmethod
    def get_weather_forecast(city: str, day = "" ) -> dict:
        logging.info("Getting datas weather")

        try:
            response = request_weather_api(city)

            handled_response = handle_response_weather_api(response, day)

            return handled_response

        except Exception as error:
            logging.error(f"Error in service > {error}")

            raise error

