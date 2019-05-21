from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import requests
import json
import sys
GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")
GITHUB_SERVICE_URL = os.getenv("GITHUB_SERVICE_URL", "")


class ActionCreateIssue(Action):
    def name(self):
        return "action_create_issue"

    def run(self, dispatcher, tracker, domain):
        try:
            headers = {'Content-Type': 'application/json'}
            tracker_state = tracker.current_state()
            chat_id = tracker_state["sender_id"]

            message = tracker.latest_message.get('text')
            message = message.split(": ")
            issue_body = message[1]
            title = tracker.get_slot("issue_name")
            data = {"title": title, "body": issue_body}
            url = GITHUB_SERVICE_URL + "api/new_issue/{chat_id}".format(
                    chat_id=chat_id)
            response = requests.post(url=url, data=json.dumps(data),
                                     headers=headers)
            received_repositories = response.json()
            dispatcher.utter_message("Criei sua issue aqui, para acessar"
                                     " clique nesse link: {link}".format(
                                         link=str(
                                             received_repositories['html_url'])
                                     ))
        except ValueError:
            print("Deu erro", file=sys.stderr)
        else:
            return [SlotSet('issue_body', issue_body)]
