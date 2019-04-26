from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import requests
import sys
from requests.exceptions import HTTPError
GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")


class ActionSetUser(Action):
    def name(self):
        return "action_set_user"

    def run(self, dispatcher, tracker, domain):
        try:
            # tracker_state = tracker.current_state()
            # sender_id = tracker_state['sender_id']

            message = tracker.latest_message.get('text')
            message = message.split()
            username = message[len(message)-1]

            headers = {"Content-Type": "application/json"}
            project_owner = username
            get_repository = GITLAB_SERVICE_URL + \
                "user/{project_owner}".format(
                    project_owner=project_owner)
            print(get_repository, file=sys.stderr)
            response = requests.get(
                get_repository, headers=headers)
            received_repositories = response.json()

            options = []
            for i, item in enumerate(received_repositories['repositories']):
                options.append((item, item))

            repositories_buttons = self.build_buttons(options)
            repositories_buttons.sort()
            lista = [repositories_buttons[x:x+2]
                     for x in range(0, len(repositories_buttons), 2)]
            # dispatcher.utter_message(
            #     "Escolha o repositório que deseja gerenciar:")

            dispatcher.utter_message(
                "Olá {user}, obrigado por confiar em mim para te ajudar nos seus trabalhos.".format(user=username))
            for item in lista:
                dispatcher.utter_button_message('Qual repositório você quer que eu fique responsavél?',
                                                item,
                                                button_type="custom")

            return [SlotSet('usuario', username)]

        except KeyError:
            dispatcher.utter_message(
                "Não consegui encontrar o nome de usuário {user} no banco de dados do gitlab.".format(user=username))
        except IndexError:
            dispatcher.utter_message(
                "Não consegui encontrar o nome de usuário {user} no banco de dados do gitlab.".format(user=username))

    def build_buttons(self, button_values):
        buttons = []
        button = {}
        button_values.sort()
        for item in button_values:
            button['title'] = item[0]
            button['payload'] = "meu repositório é " + item[1]
            buttons.append(button.copy())
        return buttons