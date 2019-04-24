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
            project_owner = 'sudjoao'
            get_repository = GITLAB_SERVICE_URL + \
                "user/{project_owner}".format(
                    project_owner=project_owner)
            response = requests.get(
                get_repository, headers=headers)
            received_repository = response.json()
            # dispatcher.utter_message(received_repository)
            print(received_repository, file=sys.stderr)
    
            # dic = []
            # for i, key in enumerate(received_repository):
            #      dic.append({'title':received_repository[i]['repositories'], 'payload':'/repositorio'})
            
            # dispatcher.utter_button_message("Seus repositórios:", dic)
            
            buttons = [{"title": str(received_repository['repositories'][0]), "payload": "/repositorio"},
                       {"title": str(received_repository['repositories'][1]), "payload": "/repositorio"},
                       {"title": str(received_repository['repositories'][2]), "payload": "/repositorio"},
                       {"title": str(received_repository['repositories'][3]), "payload": "/repositorio"},
                       {"title": str(received_repository['repositories'][4]), "payload": "/repositorio"}]
            dispatcher.utter_button_message(
                "Seus repositórios:", buttons)

            return [SlotSet('usuario', username)]
            
        except ValueError:
            dispatcher.utter_message(ValueError)
