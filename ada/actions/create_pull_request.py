from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import requests
import json
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError

GITHUB_SERVICE_URL = os.getenv("GITHUB_SERVICE_URL", "")


class ActionCreatePullRequest(Action):
    def name(self):
        return "action_create_pull_request"

    def run(self, dispatcher, tracker, domain):
        try:
            headers = {'Content-Type': 'application/json'}
            tracker_state = tracker.current_state()
            chat_id = tracker_state["sender_id"]

            message = tracker.latest_message.get('text')
            message = message.split(": ")
            pull_request_body = message[1]
            title = tracker.get_slot("pull_request_title")
            head_branch = tracker.get_slot("head_branch")
            base_branch = tracker.get_slot("base_branch")
            data = {"title": title, "body": pull_request_body,
                    "head": head_branch, "base": base_branch}
            url = GITHUB_SERVICE_URL + "api/new_pr/{chat_id}".format(
                    chat_id=chat_id)
            response = requests.post(url=url, data=json.dumps(data),
                                     headers=headers)
            response.json()
            dispatcher.utter_message("Criei seu Pull Request!")
        except HTTPError:
            dispatcher.utter_message(
                "Não consegui criar o pull request, tente novamente")
        except ValueError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        else:
            return [SlotSet('pull_request_body', pull_request_body)]
