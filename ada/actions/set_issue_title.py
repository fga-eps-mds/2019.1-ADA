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


class ActionIssueName(Action):
    def name(self):
        return "action_issue_name"

    def run(self, dispatcher, tracker, domain):
        try:
            message = tracker.latest_message.get('text')
            message = message.split(": ")
            issue_name = message[1]
            print("O titulo da Issue é: {issue_name}\n"
                  .format(issue_name=issue_name),
                  file=sys.stderr)
        except ValueError:
            print("Deu erro", file=sys.stderr)
        else:
            return [SlotSet('issue_name', issue_name)]
