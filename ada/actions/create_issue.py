from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import requests
import json
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError

GITHUB_SERVICE_URL = os.getenv("GITHUB_SERVICE_URL", "")


class ActionCreateIssue(Action):
    def name(self):
        return "action_create_issue"

    def run(self, dispatcher, tracker, domain):
        headers = {'Content-Type': 'application/json'}
        tracker_state = tracker.current_state()
        chat_id = tracker_state["sender_id"]
        if self.check_user(chat_id, headers):
            try:

                message = tracker.latest_message.get('text')
                message = message.split(": ")
                issue_body = message[1]
                title = tracker.get_slot("issue_name")
                data = {"title": title, "body": issue_body}
                url = GITHUB_SERVICE_URL + "api/new_issue/{chat_id}".format(
                        chat_id=chat_id)
                response = requests.post(url=url, data=json.dumps(data),
                                         headers=headers)
                response.json()
                dispatcher.utter_message("Criei sua issue aqui!")
            except HTTPError:
                dispatcher.utter_message(
                    "Não consegui criar a issue, tente novamente")
            except ValueError:
                dispatcher.utter_message(
                 "Estou com problemas para encontrar seus dados agora,"
                 "me mande novamente uma mensagem mais tarde.")
            except NewConnectionError:
                dispatcher.utter_message(
                 "Estou com problemas para me conectar agora, me mande "
                 "novamente uma mensagem mais tarde.")
            else:
                return [SlotSet('issue_body', issue_body)]
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
