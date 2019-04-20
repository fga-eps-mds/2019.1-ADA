from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random


class ActionSetRepositorie(Action):
    def name(self):
        return "action_set_repositorie"

    def run(self, dispatcher, tracker, domain):
        try:
            message = tracker.latest_message.get('text')
            vector = message.split()
            repositorio = vector[len(vector)-1]
            dispatcher.utter_message(
                "O nome do seu repositorio é: {rep}.".format(rep=repositorio))
            return [SlotSet('repositorio', repositorio)]
        except ValueError:
            dispatcher.utter_message(ValueError)
