from rasa_core_sdk import Action
import json
import requests
import os
import sys

GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")

class Report(Action):
    def name(self):
        return "action_get_report"

    def run(self, dispatcher, tracker, domain):
        try:
            headers = {'Content-Type': 'application/json'}
            project_owner = "gitlab-org"
            project_name = "gitaly"
            response = requests.get(GITLAB_SERVICE_URL +
                                    "report/{project_owner}/{project_name}"
                                    .format(project_owner=project_owner,
                                            project_name=project_name), headers=headers)
            report_project = response.json()
            print(report_project, file=sys.stderr)
            dispatcher.utter_message("Primeiramente, o seu projeto se chama {project_name}\
                                     e se encontra disponível nesse site {web_url}".format(project_name=report_project[0]["project"]["name"], web_url=report_project[0]["project"]["web_url"]))

            text_message_2 = "Os membros desse projeto são os seguintes:\n"
            for item in report_project:
                for value in item["members"]["name"]:
                    text_message_2 += "➡️ {members}\n".format(members=value)
            dispatcher.utter_message(text_message_2)

            text_message = "As branches do seu repositório são as seguintes:\n"
            for item in report_project:
                for value in item["branches"]["name"]:
                    text_message += "➡️ {names}\n".format(names=value)
            dispatcher.utter_message(text_message)

            dispatcher.utter_message("O último commit foi feito por {author_name} no dia {authored_date} com o título {title}.".format(author_name=report_project[0]["commits"]["last_commit"]["author_name"], authored_date=report_project[0]["commits"]["last_commit"]["authored_date"],title=report_project[0]["commits"]["last_commit"]["title"]))

            dispatcher.utter_message("O repositório possui um total de {number_of_commits} commit's.".format(number_of_commits=report_project[0]["commits"]["number_of_commits"]))

            dispatcher.utter_message("O atual pipeline possui id {current_pipeline_id} e nome {current_pipeline_name}".format(current_pipeline_id=report_project[0]["pipelines"]["current_pipeline_id"], current_pipeline_name=report_project[0]["pipelines"]["current_pipeline_name"]))

            dispatcher.utter_message("O número total de pipelines é {number_of_pipelines} com {succeded_pipelines} que obtiveram sucesso e {failed_pipeline}\
                    que obtiveram falha. A porcentagem de sucesso dos pipelines é igual a {percent_succeded}%.".format(number_of_pipelines=report_project[0]["pipelines"]\
                    ["number_of_pipelines"], succeded_pipelines=report_project[0]["pipelines"]["succeded_pipelines"], failed_pipeline=report_project[0]["pipelines"]\
                    ["failed_pipelines"], percent_succeded=report_project[0]["pipelines"]["percent_succeded"]))

            dispatcher.utter_message("Agora, vou te mostrar a duração dos seus pipelines, trazendo o tempo total, a média, o maior tempo e o menor tempo.")
            dispatcher.utter_message("O tempo total ficou acumulado em {total} segundos. A média de tempo dos pipelines ficou igual a {average} segundos, tendo um tempo máximo de {higher} segundos e um tempo mínimo de {lower} segundos.".format(total=report_project[0]["pipelines_times"]["total"], average=report_project[0]["pipelines_times"]["average"], higher=report_project[0]["pipelines_times"]["higher"], lower=report_project[0]["pipelines_times"]["lower"]))
        except ValueError:
            dispatcher.utter_message(ValueError)
