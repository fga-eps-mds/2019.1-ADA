from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from urllib3.exceptions import NewConnectionError
import requests
import os
GITHUB_SERVICE_URL = os.getenv("GITHUB_SERVICE_URL", "")


class ActionIssueName(Action):
    def name(self):
        return "action_issue_name"

    def run(self, dispatcher, tracker, domain):
        headers = {'Content-Type': 'application/json'}
        tracker_state = tracker.current_state()
        chat_id = tracker_state["sender_id"]
        if self.check_user(chat_id, headers):
            try:
                message = tracker.latest_message.get('text')
                message = message.split(": ")
                issue_name = message[1]

            except ValueError:
                dispatcher.utter_message(
                 "Estou com problemas para encontrar seus dados agora,"
                 "me mande novamente uma mensagem mais tarde.")
            except NewConnectionError:
                dispatcher.utter_message(
                 "Estou com problemas para me conectar agora, me mande "
                 "novamente uma mensagem mais tarde.")

            else:
                return [SlotSet('issue_name', issue_name)]
        else:
            dispatcher.utter_message("Para criar uma issue"
                                     " é necessário que você tenha um "
                                     "repositório do github cadastrado!")
            dispatcher.utter_message("Quando quiser cadastrar é só avisar!")
            return []

    def check_user(self, chat_id, headers):
        url = GITHUB_SERVICE_URL + "user/infos/{chat_id}".\
            format(chat_id=chat_id)
        response = requests.get(url, headers=headers)
        data = response.json()
        if data["username"] and data["repository"]:
            return True
        return False
