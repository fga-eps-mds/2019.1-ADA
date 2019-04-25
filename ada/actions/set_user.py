from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import requests
import sys

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
            dispatcher.utter_message(
                "Seu nome de usuário é: {user}.".format(user=username))
            
            headers = {"Content-Type": "application/json"}
            project_owner = username
            get_repository = GITLAB_SERVICE_URL + \
                "user/{project_owner}".format(
                    project_owner=project_owner)
            response = requests.get(
                get_repository, headers=headers)
            received_repositories = response.json()

            options = []

            for i, item in enumerate(received_repositories['repositories']):
                options.append((item, item))
            
            repositories_buttons = self.build_buttons(options)
            dispatcher.utter_button_message("Escolha o repositório que deseja gerenciar",
                                            repositories_buttons,
                                            button_type="custom")

            
            return [SlotSet('usuario', username)]

        except ValueError:
            dispatcher.utter_message(ValueError)


    def build_buttons(self, button_values):
        buttons = []
        button = {}
        for item in button_values:
            button['title'] = item[0] 
            button['payload'] = "meu repositório é " + item[1]
            buttons.append(button.copy())
        return buttons
