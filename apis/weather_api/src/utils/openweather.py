import logging
import requests
from datetime import datetime, timedelta

from fastapi import HTTPException

from .constants import WEATHER_API_KEY, WEATHER_API_URL
from .validators import convert_week_day_in_int_day

def request_weather_api(city: str) -> dict:
        logging.info("Requesting weather API")

        url_api = WEATHER_API_URL
        key_api = WEATHER_API_KEY

        params = {
            "q": city,
            "units": "metric",
            "lang": "pt_br",
            "appid": key_api
        }

        try:

            response = requests.get(url_api, params)

            response_json = response.json()

            if (response.status_code != 200):
                logging.error(f"Error from request open weather api"
                              f" >> {response_json}")

                raise HTTPException(response.status_code, response.reason)

            return response_json
        except Exception as error:
            logging.error(f"Error > {error}")

            raise error


def handle_response_weather_api(datas_weather: dict, day: int) -> dict:
    logging.info("Handling weather API response")

    day_int = 0
    user_forecasted_data = {}
    weekday_today_int = datetime.now().isoweekday()

    if "hoje" in day or not day or "None" in day:
        day_int = 0
    elif not "amanh" in day:
        weekday_user_forecasted_data_int = convert_week_day_in_int_day(day)

        diff = weekday_user_forecasted_data_int - weekday_today_int

        if diff < 0:
            day_int = diff + 7
        else:
            day_int = diff

    elif ("amanh" and "depois") in day:
        day_int = 2
    elif "amanh" in day and not "depois" in day:
        day_int = 1

    user_forecasted_day = datetime.now() + timedelta(days = day_int)
    user_forecasted_day_int = user_forecasted_day.day

    for data_weather in datas_weather["list"]:

        date_data = data_weather["dt_txt"]
        handle_date_data =  datetime.fromisoformat(date_data)
        day_data = handle_date_data.day

        if day_data is user_forecasted_day_int:
            logging.debug(f"Complete weather data > {data_weather}")

            user_forecasted_data = {
                "temp": data_weather["main"]["temp"],
                "temp_min": data_weather["main"]["temp_min"],
                "temp_max": data_weather["main"]["temp_max"]
            }
            break

    return user_forecasted_data
