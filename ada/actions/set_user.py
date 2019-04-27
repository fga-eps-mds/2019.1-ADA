from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import requests
import sys
from requests.exceptions import HTTPError
import telegram
import logging
GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "")

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
            options = []
            for i, item in enumerate(received_repositories['repositories']):
                options.append((item, item))
            
            repo_names = [received_repositories['repositories'][i:i+2] for i in range(0, len(received_repositories['repositories']), 2)]
            dispatcher.utter_message(
                "Olá {user}, obrigado por confiar em mim para te ajudar nos seus trabalhos.".format(user=project_owner))
            
            bot = telegram.Bot(token=ACCESS_TOKEN)
            
            repositories_buttons = self.build_buttons(options)
            lista = [repositories_buttons[x:x+2]
                     for x in range(0, len(repositories_buttons), 2)]

            
            for item in lista:
                dispatcher.utter_button_message('Qual repositório você quer que eu fique responsavél?',
                                                item,
                                                button_type="custom")

            # reply_markup = telegram.InlineKeyboardMarkup(lista)
            # bot.send_message(chat_id=sender_id,
            #      text="Escolha o seu repositório",
            #      reply_markup=reply_markup)

            # reply_markup = {
            #     "remove_keyboard": True
            # }

            return [SlotSet('usuario', project_owner)]

        except KeyError:
            dispatcher.utter_message(
                "Não consegui encontrar o nome de usuário {user} no banco de dados do gitlab.".format(user=project_owner))
        except IndexError:
            dispatcher.utter_message(
                "Não consegui encontrar o nome de usuário {user} no banco de dados do gitlab.".format(user=project_owner))

    def build_buttons(self, button_values):
        buttons = []
        button = {}
        for item in button_values:
            button['title'] = item[0]
            button['payload'] = "meu repositório é " + item[1]
            buttons.append(button.copy())
        return buttons

        
