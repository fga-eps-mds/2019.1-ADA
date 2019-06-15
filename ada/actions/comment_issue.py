from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import requests
import json
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError

GITHUB_SERVICE_URL = os.getenv("GITHUB_SERVICE_URL", "")


class ActionCommentIssue(Action):
    def name(self):
        return "action_comment_issue"

    def run(self, dispatcher, tracker, domain):
        slot_repo = tracker.get_slot("repository_github")
        if slot_repo:
            try:
                headers = {'Content-Type': 'application/json'}
                tracker_state = tracker.current_state()
                chat_id = tracker_state["sender_id"]

                message = tracker.latest_message.get('text')
                splited_message = message.split(": ")
                comment_body = splited_message[-1]
                splited_message = splited_message[0].split('#')
                issue_number = splited_message[-1]
                data = {"body": comment_body, "issue_number": issue_number}
                url = GITHUB_SERVICE_URL + "api/comment_issue/{chat_id}".\
                    format(chat_id=chat_id)
                response = requests.post(url=url, data=json.dumps(data),
                                         headers=headers)
                response.raise_for_status()
            except HTTPError:
                dispatcher.utter_message(
                    "Não consegui comentar a issue, tente novamente")
            except ValueError:
                dispatcher.utter_message(
                 "Estou com problemas para me conectar agora, me mande "
                 "novamente uma mensagem mais tarde.")
            except NewConnectionError:
                dispatcher.utter_message(
                 "Estou com problemas para me conectar agora, me mande "
                 "novamente uma mensagem mais tarde.")
            else:
                return [SlotSet('issue_number', issue_number)]
        else:
            dispatcher.utter_message("Para comentar uma issue"
                                     " é necessário que você tenha um "
                                     "repositório do github cadastrado!")
            dispatcher.utter_message("Quando quiser cadastrar é só avisar!")
            return []
