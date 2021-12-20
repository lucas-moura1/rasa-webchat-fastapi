from typing import Any, Text, Dict, List
import os

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset


class ActionWeatherForecast(Action):

    def name(self) -> Text:
        return "action_weather_forecast"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("LOC")
        day = tracker.get_slot("day")

        try:
            if not city:
                raise

            api_response = await self.request_weather_api(city, day)

            dispatcher.utter_message(
                template="utter_weather_forecast",
                city = city,
                day = f", {day}," if day else "",
                temp = api_response["temp"],
                max = api_response["temp_max"],
                min = api_response["temp_min"]
            )

            return [AllSlotsReset()]


        except Exception:

            dispatcher.utter_message(
                template="utter_problem_weather_forecast")

            return [AllSlotsReset()]

    async def request_weather_api(self, city: str, day: str) -> Dict:

        api_url = os.getenv("weather_api")

        response = requests.get(f"{api_url}?city={city}&day={day}")

        response_json = response.json()

        return response_json
