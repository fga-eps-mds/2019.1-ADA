from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random


class ActionSetUser(Action):
    def name(self):
        return "action_set_user"

    def run(self, dispatcher, tracker, domain):
        try:
            user = tracker.current_slot_values()['usuario']
            dispatcher.utter_message(
                "Seu nome de usuário é: {user}.".format(user=user))
            dispatcher.utter_message("Agora digite o nome do seu repositório")
        except ValueError:
            dispatcher.utter_message(ValueError)
