from typing import Any, Text, Dict, List
from datetime import datetime

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        greet = self.logic_greet

        dispatcher.utter_message(
            template="utter_greet",
            greet = greet
        )

        return []

    @property
    def get_current_hour(self) -> int:

        current_hour = datetime.now().hour

        return current_hour

    @property
    def logic_greet(self) -> str:
        current_hour = self.get_current_hour - 3

        greet = "Bom dia"

        if 12 < current_hour < 18:
            greet = "Boa Tarde"
        elif 6 > current_hour > 18:
            greet = "Boa noite"

        return greet
