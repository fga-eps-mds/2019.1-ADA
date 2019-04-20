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
            project_name = "gitaly"
            response = requests.get(GITLAB_SERVICE_URL +
                                    "build/{project_owner}/{project_name}"
                                    .format(project_owner=project_owner,
                                            project_name=project_name),
                                    headers=headers)
            received_build = response.json()

            text_message = "Os passos da build são:\n"

            for i, item in enumerate(received_build):

                if received_build[i]['status'] == "success":
                    status = "✅"
                elif received_build[i]['status'] == "failed":
                    status = "❌"
                else:
                    status = "🔄"

                text_message += "{status} {job_name}\n" \
                                .format(status=status,
                                        job_name=received_build[i]['job_name'])

            dispatcher.utter_message('A build #{job_id} '
                                     'da branch {branch}, '
                                     'commit "{commit}", '
                                     'está no estágio de "{stage}".'
                                     .format(job_id=received_build[0]['job_id'],
                                             branch=received_build[0]['branch'],
                                             commit=received_build[0]['commit'],
                                             stage=received_build[0]['stage']))

            dispatcher.utter_message(text_message)

            dispatcher.utter_message("Para visualizar sua build "
                                     "no GitLab acesse o link {pipeline_url}"
                                     .format(pipeline_url=received_build \
                                     [0]['web_url']))

            is_there_any_build = True
        except ValueError:
            dispatcher.utter_message(ValueError)
            if(not is_there_any_build):
                default = "Não há build's em andamento, "
                "mas continuo te informando."
                dispatcher.utter_message(default)
