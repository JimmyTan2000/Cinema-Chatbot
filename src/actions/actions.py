# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


import json
import requests
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class descriptionLinks(Action):

    

    def name(self) -> Text:
        return "action_movie_description"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        x = requests.get('http://127.0.0.1:5000/descriptionLinks')
        y = x.json()
        movie = tracker.get_slot('movie_name')
        dispatcher.utter_message(text = f"{y[0][movie]}")

        return []

class moviesAvailable(Action):

    def name(self) -> Text:
        return "action_movies_available"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        x = requests.get('http://127.0.0.1:5000/schedules')
        y = x.json()
        date = tracker.get_slot('date')
        name = "Name"
        if date.lower() == "today":
            dispatcher.utter_message(text = f"{y[0][name][0]} is/are available on {date}")
        elif date.lower() == "tomorrow":
            dispatcher.utter_message(text = f"{y[1][name][0]} is/are available on {date}")
        elif date.lower() == "29/11":
            dispatcher.utter_message(text = f"{y[2][name][0]} is/are available on {date}")
        elif date.lower() == "30/11":
            dispatcher.utter_message(text = f"{y[3][name][0]} is/are available on {date}")
        else:
            dispatcher.utter_message(text = f"{y[4][name][0]} is/are available on {date}")
        return []
        
class moviesSchedule(Action):

    def name(self) -> Text:
        return "action_movies_schedule"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text ='http://127.0.0.1:5000/schedules')
        return []

class sittingPlans(Action):

    def name(self) -> Text:
        return "action_sitting_plans"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        x = requests.get('http://127.0.0.1:5000/sittingPlans')
        y = x.json()
        movie = tracker.get_slot('movie_name')
        movieUpper = movie.upper()
        date = tracker.get_slot('date')
        Schedules = "Schedules"
        
        try:
            if date.lower() == "today":
                dispatcher.utter_message(text = f"Available seats for {date.lower()} are:\n{y[0][Schedules][0][movieUpper][0]}")
            elif date.lower() == "tomorrow":
                dispatcher.utter_message(text = f"Available seats for {date.lower()} are:\n{y[1][Schedules][0][movieUpper][0]}")
            elif date.lower() == "29/11":
                dispatcher.utter_message(text = f"Available seats for {date.lower()} are:\n{y[2][Schedules][0][movieUpper][0]}")
            elif date.lower() == "30/11":
                dispatcher.utter_message(text = f"Available seats for {date.lower()} are:\n{y[3][Schedules][0][movieUpper][0]}")
            else: 
                dispatcher.utter_message(text = f"Available seats for {date.lower()} are:\n{y[4][Schedules][0][movieUpper][0]}")

        except KeyError:
            dispatcher.utter_message(text = f"{movie} is not available on {date}")
        
        

        return []