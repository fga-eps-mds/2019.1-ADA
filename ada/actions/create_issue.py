from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import requests
import telegram
import json
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import sys
GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")


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
            dic = {"title": title, "body": issue_body}

        except ValueError:
            print("Deu erro", file=sys.stderr)
        else:
            return [SlotSet('issue_body', issue_body)]
