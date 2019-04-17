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
            dispatcher.utter_message("Certo! Encontrei a build mais "
                                     "recente do seu repositório.")
            headers = {'Content-Type': 'application/json'}
            project_owner = "adabot"
            project_name = "ada-gitlab"
            response = requests.get(GITLAB_SERVICE_URL +
                                    "build/{project_owner}/{project_name}/jobs"
                                    .format(project_owner=project_owner, 
                                    project_name=project_name), headers=headers)
            requests_build = response.json()

            if requests_build['status'] == "success":
                status = "E está passando nos critérios de aceitação adotadas pela Build."
            else:
                status = "E não está passando nos critérios de aceitação adotadas pela Build."
            
            if requests_build['stage'] == "test":
                stage = "de teste"
            elif requests_build['stage'] == "build":
                stage = "de construção"
            elif requests_build['stage'] == "deploy":
                stage = "de implementação"
            

            dispatcher.utter_message("A build {name} do "
                                    "serviço {ref} "
                                    "está no estágio {stage}."
                                    .format(name=requests_build['name'].capitalize(),
                                            ref=requests_build['ref'],
                                            stage=stage))
            dispatcher.utter_message("{status}".format(status=status))
            dispatcher.utter_message("Para visualizar essa build no GitLab acesse o link {web_url}"
                                    .format(web_url=requests_build['web_url']))
            is_there_any_build = True
        except ValueError:
            dispatcher.utter_message(ValueError)
            if(not is_there_any_build):
                default = "Não há build's em andamento, mas continuo te informando."
                dispatcher.utter_message(default)
