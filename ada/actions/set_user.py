from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random
import os
import logging
from pymongo import MongoClient


class ActionSetUser(Action):
    def name(self):
        return "action_set_user"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker_state = tracker.current_state()
            sender_id = tracker_state['sender_id']
            message = tracker.latest_message.get('text')
            vector = message.split()
            username = vector[len(vector)-1]
            dispatcher.utter_message(
                "Seu nome de usuário é: {user}.".format(user=username))
            dispatcher.utter_message(
                "Agora me fala o nome do seu repositório, mas não se esqueça que de escrever repositório: na frente")
            return [SlotSet('usuario', username)]
            # dispatcher.utter_message(
            #     "Variavel Local:" + str(sender_id) + "Nome do usuario:" + msg)

            # telegram = self.db_connect()
            # telegram.insert_one({'sender_id': sender_id})

            # dispatcher.utter_message(
            #     'ID do usuario:' + telegram.find_one({'sender_id': sender_id}))
        except ValueError:
            dispatcher.utter_message(ValueError)

    # def db_connect(self):
    #     telegram_client = MongoClient("mongodb://mongo-telegram:27017/ada")
    #     telegram_db = telegram_client['ada']
    #     telegram = telegram_db['users']
    #     return telegram
