from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import requests
import json
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import sys
import telegram

GITHUB_SERVICE_URL = os.getenv("GITHUB_SERVICE_URL", "")


class ActionCommentIssue(Action):
    def name(self):
        return "action_comment_issue"

    def run(self, dispatcher, tracker, domain):
        try:
            headers = {'Content-Type': 'application/json'}
            tracker_state = tracker.current_state()
            chat_id = tracker_state["sender_id"]
            message = tracker.latest_message.get('text')
            splited_message = message.split(": ")
            issue_body = splited_message[-1]
            splited_message = splited_message[0].split('#')
            issue_number = splited_message[-1]
            data = {"body": issue_body, "issue_number": issue_number}
            url = GITHUB_SERVICE_URL + "api/comment_issue/{chat_id}".format(
                chat_id=chat_id)
            response = requests.post(url=url, data=json.dumps(data),
                                        headers=headers)
            received_repositories = response.json()
            dispatcher.utter_message("Criei sua issue aqui, para acessar"
                                     " clique nesse link: {link}".format(
                                         link=str(received_repositories['html_url'])))
                                
            text_message = "Certo! Comentei sua issue!"
            dispatcher.utter_message(text_message)
        except HTTPError:
            dispatcher.utter_message(
                "Não consegui criar a issue, tente novamente")
        except ValueError:
            dispatcher.utter_message(
                "Estou com problemas para criar a issue, manda "
                "mais uma vez pra ver se dessa vez dá certo.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        else:
            return [SlotSet('issue_body', issue_body)]
