from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random


class ActionSetRepositorie(Action):
    def name(self):
        return "action_set_repositorie"

    def run(self, dispatcher, tracker, domain):
        try:
            repositorio = tracker.current_slot_values()['repositorio']
            dispatcher.utter_message(
                "O nome do seu repositorio é: {rep}.".format(rep=repositorio))
        except ValueError:
            dispatcher.utter_message(ValueError)
