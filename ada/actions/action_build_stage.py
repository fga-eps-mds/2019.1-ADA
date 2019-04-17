from rasa_core_sdk import Action
import requests
import os

GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")


class BuildStage(Action):
    def name(self):
        return "action_build_stage"

    def run(self, dispatcher, tracker, domain):
        is_there_any_build = False
        try:
            dispatcher.utter_message("Certo! Encontrei a seguinte build no seu "
                                     "repositório.")
            headers = {'Content-Type': 'application/json'}
            project_owner = "adabot"
            project_name = "ada-gitlab"
            response = requests.get(GITLAB_SERVICE_URL +
                                    "build/{project_owner}/{project_name}"
                                    .format(project_owner=project_owner, 
                                    project_name=project_name), headers=headers)
            requests_build = response.json()
            dispatcher.utter_message("A build {name} da "
                                    "pipeline {pipeline_ref} "
                                    "está no estágio {stage}."
                                    .format(name=requests_build['name'].capitalize(),
                                            pipeline_ref=requests_build['pipeline']['ref'].capitalize(),
                                            stage=requests_build['stage'].capitalize()))
            dispatcher.utter_message("O status atual dela é {status}."
                                    .format(status=requests_build['status'].capitalize()))
            dispatcher.utter_message("Para visualizar essa build no GitLab acesse o link {web_url}"
                                    .format(web_url=requests_build['web_url']))
            is_there_any_build = True
        except ValueError:
            dispatcher.utter_message(ValueError)
            if(not is_there_any_build):
                default = "Não há build's em andamento, mas continuo te informando."
                dispatcher.utter_message(default)
