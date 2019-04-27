from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import requests
import sys
from requests.exceptions import HTTPError
import logging
import telegram

GITLAB_SERVICE_URL = os.environ.get("GITLAB_SERVICE_URL", "")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")

class ActionSetUser(Action):
    def name(self):
        return "action_set_user"

    def run(self, dispatcher, tracker, domain):
        try:

            tracker_state = tracker.current_state()
            sender_id = tracker_state['sender_id']

            message = tracker.latest_message.get('text')
            message = message.split()
            project_owner = message[len(message)-1]

            headers = {"Content-Type": "application/json"}
            get_repository = GITLAB_SERVICE_URL + \
                "user/{project_owner}".format(
                    project_owner=project_owner)
            response = requests.get(
                get_repository, headers=headers)
            received_repositories = response.json()
            
            buttons = []

            for repositorio in received_repositories["repositories"]:
                buttons.append(telegram.InlineKeyboardButton(text=repositorio, callback_data="meu repositorio é " + repositorio))
            repo_names = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
            bot = telegram.Bot(token=ACCESS_TOKEN)
            reply_markup = telegram.InlineKeyboardMarkup(repo_names)
            bot.send_message(chat_id=sender_id,
                    text="Escolha o seu repositório",
                    reply_markup=reply_markup)

            return [SlotSet('usuario', project_owner)]

        except KeyError:
            dispatcher.utter_message(
                "Não consegui encontrar o seu usuário no GitLab, por favor verifique ele e me mande novamente.")
        except IndexError:
            dispatcher.utter_message(
                "Não consegui encontrar o seu usuário no GitLab, por favor verifique ele e me mande novamente.")

    def build_buttons(self, button_values):
        buttons = []
        button = {}
        for item in button_values:
            button['title'] = item[0]
            button['payload'] = "meu repositório é " + item[1]
            buttons.append(button.copy())
        return buttons

        
