from rasa_core_sdk import Action
import requests
import os
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import telegram

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")
GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")


class FindProjectCollaborators(Action):
    def name(self):
        return "action_find_project_collaborators"

    def run(self, dispatcher, tracker, domain):
        try:
            #TODO
            pass

        except blabla :
            #TODO
            pass

        else:
            #TODO
            pass
