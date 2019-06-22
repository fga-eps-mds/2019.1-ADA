from rasa_core_sdk import Action
import requests
import os
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import telegram
GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")
SECS = 30.0


class Report(Action):
    def name(self):
        return "action_get_report"

    def run(self, dispatcher, tracker, domain):
        headers = {'Content-Type': 'application/json'}
        tracker_state = tracker.current_state()
        chat_id = tracker_state["sender_id"]
        if self.check_user(chat_id, headers):
            try:
                try:
                    response_branches = requests.get(
                                            GITLAB_SERVICE_URL +
                                            "report/branches/{chat_id}"
                                            .format(chat_id=chat_id),
                                            timeout=SECS,
                                            headers=headers)
                    response_commits = requests.get(
                                            GITLAB_SERVICE_URL +
                                            "report/commits/{chat_id}"
                                            .format(chat_id=chat_id),
                                            timeout=SECS,
                                            headers=headers)
                    response_pipelines = requests.get(
                                            GITLAB_SERVICE_URL +
                                            "report/pipelines/{chat_id}"
                                            .format(chat_id=chat_id),
                                            timeout=SECS,
                                            headers=headers)
                    response_project = requests.get(
                                            GITLAB_SERVICE_URL +
                                            "report/project/{chat_id}"
                                            .format(chat_id=chat_id),
                                            timeout=SECS,
                                            headers=headers)

                except requests.exceptions.Timeout:
                    text = "Desculpa, não consegui fazer"\
                           " o que você me pediu! 😕"
                    bot = telegram.Bot(token=ACCESS_TOKEN)
                    bot = bot.send_message(chat_id=chat_id, text=text)
                else:
                    branches = response_branches.json()
                    branches = branches["branches"]
                    commits = response_commits.json()
                    commits = commits["commits"]
                    pipeline = response_pipelines.json()
                    pipeline = pipeline["pipeline"]
                    project = response_project.json()
                    project = project["project"]

                dispatcher.utter_message("Aqui está o relatório do "
                                         "projeto {project_name}"
                                         " ele se encontra disponível "
                                         "neste link {web_url}."
                                         .format(project_name=project["name"],
                                                 web_url=project["web_url"]))
                text_message = "As branches do seu repositório "\
                               "são as seguintes:\n"
                for item in branches:
                    text_message += "▪️ {names}\n".format(names=item["name"])
                dispatcher.utter_message(text_message)
                commits = commits["last_commit"]
                commit_date = commits["authored_date"]
                date = commit_date[:10]
                day = date[8:10]
                month = date[5:7]
                year = date[0:4]
                dispatcher.utter_message("O último commit foi feito por "
                                         "{author_name} no dia "
                                         "{day}/{month}/{year} com "
                                         "o título {title}.".format(
                                             author_name=commits
                                             ["author_name"],
                                             day=day, month=month, year=year,
                                             title=commits["title"]))
                if not pipeline["number_of_pipelines"]:
                    dispatcher.utter_message("Esse repositório não possui "
                                             "pipelines! 😕")
                else:
                    dispatcher.utter_message(
                        "O atual pipeline possui id "
                        "{pipeline_id} "
                        "e nome {pipeline_name}"
                        .format(
                         pipeline_id=(
                          pipeline["current_pipeline_id"]),
                         pipeline_name=(
                          pipeline["current_pipeline_name"]
                         )))

                    dispatcher.utter_message(
                        "Sobre o projeto como um todo:\n📌 "
                        "Número total de pipelines: {total}\n"
                        "☑️ {success} obtiveram sucesso\n"
                        "❗️ {fail} falharam\nE {another}"
                        " tiveram outro estado\n"
                        "☑️ A porcentagem de sucesso foi: "
                        "{perc_suc}%\n❗️ E a porcentagem "
                        "de falhas "
                        "foi: {perc_fail}%\n".format(
                         total=(
                          pipeline["number_of_pipelines"]),
                         success=(
                          pipeline["succeded_pipelines"]),
                         fail=pipeline["failed_pipelines"],
                         another=pipeline["another_status"],
                         perc_suc=(
                          pipeline["percent_succeded"]),
                         perc_fail=(
                          pipeline["percent_failed"])))
                    pipeline_50_last = pipeline["50_last"]
                    if pipeline_50_last["another_status"] > 1:
                        dispatcher.utter_message(
                            "Sobre os últimos 50 pipelines:\n"
                            "☑️ {success} obtiveram sucesso\n"
                            "❗️ {fail} falharam\nE {another}"
                            " tiveram outro estado\n"
                            "☑️ A porcentagem de sucesso foi: "
                            "{perc_suc}%\n❗️ E a porcentagem "
                            "de falhas "
                            "foi: {perc_fail}%\n".format(
                                                    success=(
                                                     pipeline_50_last
                                                     ["succeded_pipelines"]),
                                                    fail=(
                                                     pipeline_50_last
                                                     ["failed_pipelines"]),
                                                    another=(
                                                     pipeline_50_last
                                                     ["another_status"]),
                                                    perc_suc=(
                                                     pipeline_50_last
                                                     ["percent_succeded"]),
                                                    perc_fail=(
                                                     pipeline_50_last
                                                     ["percent_failed"])))
                    else:
                        dispatcher.utter_message(
                            "Sobre os últimos 50 pipelines:\n"
                            "☑️ {success} obtiveram sucesso\n"
                            "❗️ {fail} falharam\nE {another}"
                            " teve outro estado\n"
                            "☑️ A porcentagem de sucesso foi: "
                            "{perc_suc}%\n❗️ E a porcentagem "
                            "de falhas "
                            "foi: {perc_fail}%\n".format(
                                                    success=(
                                                     pipeline_50_last
                                                     ["succeded_pipelines"]),
                                                    fail=(pipeline_50_last
                                                          ["failed_pipelines"]
                                                          ),
                                                    another=(pipeline_50_last
                                                             ["another_status"]
                                                             ),
                                                    perc_suc=(
                                                     pipeline_50_last
                                                     ["percent_succeded"]),
                                                    perc_fail=(
                                                     pipeline_50_last
                                                     ["percent_failed"])))
                return []
            except HTTPError:
                dispatcher.utter_message(
                    "Não estou conseguindo ter acesso a seus dados, tem"
                    " certeza que seus dados estão certos?")
            except ValueError:
                dispatcher.utter_message(
                    "Estou com problemas para me conectar agora, me mande "
                    "novamente uma mensagem mais tarde.")
            except NewConnectionError:
                dispatcher.utter_message(
                    "Estou com problemas para me conectar agora, me mande "
                    "novamente uma mensagem mais tarde.")

    def check_user(self, chat_id, headers):
        url = GITLAB_SERVICE_URL + "user/infos/{chat_id}".\
            format(chat_id=chat_id)
        response = requests.get(url, headers=headers)
        data = response.json()
        if data["username"] and data["repository"]:
            return True
        return False
