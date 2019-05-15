from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import requests
import telegram
import json
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import sys

GITHUB_SERVICE_URL = os.environ.get("GITHUB_SERVICE_URL", "")

class NewIntegration(Action):
    def name(self):
        return "action_new_integration"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker_state = tracker.current_state()
            sender_id = tracker_state["sender_id"]
            print(sender_id, file=sys.stderr)
            headers = {"Content-Type": "application/json"}

            url = GITHUB_SERVICE_URL + "user/{sender_id}".format(sender_id=sender_id)
            response = requests.get(url=url, headers=headers)
            github_login = response.json()
            print(github_login["username"], file=sys.stderr)
            repo_names = self.build_buttons(github_login["username"], headers)
        except ValueError:
            dispatcher.utter_message("Deu errado")
            # repo_names = self.build_buttons(github_username, headers)
    def build_buttons(self, github_username, headers):
        get_repository = GITHUB_SERVICE_URL + \
            "user/{github_username}/repositories".format(
        github_username=github_username)

        response = requests.get(url=get_repository, headers=headers)

        received_repositories = response.json()
        buttons = []
        for repositorio in received_repositories["repositories"]:
            buttons.append(telegram.InlineKeyboardButton(
                text=repositorio["name"],
                callback_data="meu repositorio do github é " + repositorio["name"]))
        repo_names = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
        return repo_names
