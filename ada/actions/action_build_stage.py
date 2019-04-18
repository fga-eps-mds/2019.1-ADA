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
            project_owner = "gitlab-org"
            project_name = "gitlab-ee"
            response = requests.get(GITLAB_SERVICE_URL +
                                    "build/{project_owner}/{project_name}/jobs"
                                    .format(project_owner=project_owner,
                                            project_name=project_name),
                                    headers=headers)
            requests_build = response.json()

            if requests_build['status'] == "success":
                status = "✅"
            elif requests_build['status'] == "failed":
                status = "❌"
            else:
                status = "🔄"

            if requests_build['status1'] == "success":
                status1 = "✅"
            elif requests_build['status1'] == "failed":
                status1 = "❌"
            else:
                status1 = "🔄"

            dispatcher.utter_message('A build #{id} da '
                                     'branch {branch}, '
                                     'commit "{commit}", '
                                     'está no estágio de "{stage}".'
                                     .format(id=requests_build['id'],
                                             commit=requests_build['commit'],
                                             branch=requests_build['branch'],
                                             stage=requests_build['stage']))
            dispatcher.utter_message("Os passos da build são:\n"
                                     "{status} {name}\n{status1} {name1}"
                                     .format(status=status,
                                             name=requests_build['name'],
                                             status1=status1,
                                             name1=requests_build['name1']))
            dispatcher.utter_message("Para visualizar sua build "
                                     "no GitLab acesse o link {web_url}"
                                     .format(web_url=requests_build
                                             ['web_url']))
            is_there_any_build = True
        except ValueError:
            dispatcher.utter_message(ValueError)
            if(not is_there_any_build):
                default = "Não há build's em andamento, "
                "mas continuo te informando."
                dispatcher.utter_message(default)
