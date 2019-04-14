from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random
import os
import sys

GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")

class ActionGetPipeline(Action):
    def name(self):
        return "action_get_pipeline"

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message("Aqui está o pipeline mais recente")
            headers = { "Content-Type": "application/json" }

            project_owner = "gitlab-org"
            project_name = "gitlab-runner"
            get_pipeline_url = GITLAB_SERVICE_URL + "pipeline/{project_owner}/{project_name}".format(project_owner=project_owner, project_name=project_name)
            response = requests.get(get_pipeline_url, headers=headers, timeout=10)
            received_pipeline = response.json() 
            if received_pipeline["status"] == "success":
                status = "passou nos critérios de aceitação do seu Pipeline."
            else:
                status = "não passou nos critérios de aceitação do seu Pipeline."

            text_message = """O Pipeline mais recente que você solicitou 
                           {status} Para visualizar o Pipeline no GitLab acesse o link 
                           {web_url}""".format(status=status, web_url=received_pipeline["web_url"])

            dispatcher.utter_message(text_message)
            return []

        except ValueError:
            dispatcher.utter_message(ValueError)