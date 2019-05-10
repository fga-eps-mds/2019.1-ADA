from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import requests
import telegram
import json
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import sys

class ActionStart(Action):
    def name(self):
        return "action_start"

    def run(self, dispatcher, tracker, domain):
        try:
            headers = {
                "Content-Type": "applications/json"
            }

            tracker_state = tracker.current_state()
            sender_id = tracker_state['sender_id']
            print(sender_id, file=sys.stderr)

            message = tracker.latest_message.get('text')
            message = message.split()
            github_id = message[-1]
            print("%"*30, file=sys.stderr)
            print(github_id, file=sys.stderr)
            print("%"*30, file=sys.stderr)

            url = "https://github.com/login/oauth/authorize?client_id=3656fdad2090a18b72b2&redirect_uri=https%3A%2F%2Ft.me%2FAda_Git_Bot%2F{sender_id}&scope=admin%3Arepo_hook%2Crepo".format(sender_id=sender_id)

            dispatcher.utter_message(url)
            print(url, file=sys.stderr)
        except ValueError:
            dispatcher.utter_message("Deu errado")
            