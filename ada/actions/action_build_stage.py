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
            build_json = response.json()

            text_message = "Os passos da build são:\n"

            for i, item in enumerate(build_json):

                if build_json[i]['status'] == "success":
                    status = "✅"
                elif build_json[i]['status'] == "failed":
                    status = "❌"
                else:
                    status = "🔄"

                text_message += "{status} {job_name}\n" \
                                .format(status=status,
                                        job_name=build_json[i]['job_name'])

            dispatcher.utter_message('A build #{job_id} '
                                     'da branch {branch}, '
                                     'commit "{commit}", '
                                     'está no estágio de "{stage}".'
                                     .format(job_id=build_json[0]['job_id'],
                                             branch=build_json[0]['branch'],
                                             commit=build_json[0]['commit'],
                                             stage=build_json[0]['stage']))

            dispatcher.utter_message(text_message)

            dispatcher.utter_message("Para visualizar sua build "
                                     "no GitLab acesse o link {pipeline_url}"
                                     .format(
                                     pipeline_url=build_json[0]['web_url']))

            is_there_any_build = True
        except ValueError:
            dispatcher.utter_message(ValueError)
            if(not is_there_any_build):
                default = "Não há build's em andamento, "
                "mas continuo te informando."
                dispatcher.utter_message(default)
