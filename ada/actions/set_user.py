from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random
import os
import logging
from pymongo import MongoClient

# telegram_client = MongoClient('mongodb://mongo-telegram:27017/ada')


class ActionSetUser(Action):
    def name(self):
        return "action_set_user"

    def run(self, dispatcher, tracker, domain):
        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']
        dispatcher.utter_message("Variavel Local:" + str(sender_id))

        # mydb = telegram_client['mydatabase']
        # users = mydb['users']
        # dic = {"sender_id": str(sender_id)}
        # users.insert_one(dic)
        # dispatcher.utter_message('ID no banco:' + str(users.find_one(dic)))
        try:
            username = tracker.current_slot_values()['usuario']
            dispatcher.utter_message(
                "Seu nome de usuário é: {user}.".format(user=username))
            dispatcher.utter_message("Agora digite o nome do seu repositório")
        except ValueError:
            dispatcher.utter_message(ValueError)
