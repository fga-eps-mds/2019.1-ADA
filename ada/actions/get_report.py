from rasa_core_sdk import Action
import requests
import os
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import telegram
GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")
SECS = 15.0


class Report(Action):
    def name(self):
        return "action_get_report"

    def run(self, dispatcher, tracker, domain):
        slot_repo = tracker.get_slot("repository_gitlab")
        if slot_repo:
            try:
                headers = {'Content-Type': 'application/json'}
                tracker_state = tracker.current_state()
                chat_id = tracker_state["sender_id"]
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

                    dispatcher.utter_message("Primeiramente, o seu projeto "
                                             "se chama {project_name}"
                                             " e se encontra disponível "
                                             "nesse site {web_url}"
                                             .format(project_name=project
                                                     ["name"],
                                                     web_url=project
                                                     ["web_url"]))
                    text_message = "As branches do seu repositório "\
                                   "são as seguintes:\n"
                    for item in branches:
                        text_message += "▪️ {names}\n".format(names=item
                                                              ["name"])
                    dispatcher.utter_message(text_message)
                    commits = commits["last_commit"]
                    dispatcher.utter_message("O último commit foi feito por"
                                             "{author_name}"
                                             "no dia {author_date} com"
                                             " o título {title}.".format(
                                              author_name=commits
                                              ["author_name"],
                                              author_date=commits
                                              ["authored_date"],
                                              title=commits["title"]))

                    dispatcher.utter_message("O atual pipeline possui id "
                                             "{pipeline_id}"
                                             "e nome {pipeline_name}".format(
                                              pipeline_id=(
                                               pipeline
                                               ["current_pipeline_id"]),
                                              pipeline_name=(
                                               pipeline
                                               ["current_pipeline_name"]
                                               )))

                    dispatcher.utter_message("Sobre o projeto como um todo:"
                                             "\n📌 Número total de pipelines:"
                                             "{total}\n"
                                             "☑️ {success} obtiveram sucesso\n"
                                             "❗️ {fail} falharam\n"
                                             "☑️ A porcentagem de sucesso foi:"
                                             " {perc_suc}%\n❗️ E a porcentagem"
                                             " de falhas"
                                             "foi: {perc_fail}%\n".format(
                                              total=(
                                               pipeline
                                               ["number_of_pipelines"]),
                                              success=(
                                               pipeline["succeded_pipelines"]),
                                              fail=pipeline
                                              ["failed_pipelines"],
                                              perc_suc=(
                                               pipeline["percent_succeded"]),
                                              perc_fail=100-(
                                               pipeline["percent_succeded"])))

                    last_7 = pipeline["recents_pipelines"]["last_7_days"]
                    last_30 = pipeline["recents_pipelines"]["last_30_days"]
                    dispatcher.utter_message("Sobre os últimos 7 dias:\n⚒ "
                                             "Número total de pipelines:"
                                             "{total}\n"
                                             "☑️ {success} obtiveram sucesso\n"
                                             "❗️ {fail} falharam\n"
                                             "☑️ A porcentagem de sucesso foi:"
                                             " {perc_suc}%\n❗️ E a porcentagem"
                                             " de falhas"
                                             "foi: {perc_fail}%\n".format(
                                              total=(
                                               last_7["number_of_pipelines"]),
                                              success=(
                                               last_7["succeded_pipelines"]),
                                              fail=last_7["failed_pipelines"],
                                              perc_suc=(
                                               last_7["percent_succeded"]),
                                              perc_fail=100-(
                                               last_7["percent_succeded"])))

                    dispatcher.utter_message("Sobre os últimos 30 dias:\n⚒ "
                                             "Número total de pipelines: "
                                             "{total}\n"
                                             "☑️ {success} obtiveram sucesso\n"
                                             "❗️ {fail} falharam\n"
                                             "☑️ A porcentagem de sucesso foi:"
                                             "{perc_suc}%\n❗️ E a porcentagem "
                                             "de falhas"
                                             "foi: {perc_fail}%\n".format(
                                              total=(
                                               last_30["number_of_pipelines"]),
                                              success=(
                                               last_30["succeded_pipelines"]),
                                              fail=last_30["failed_pipelines"],
                                              perc_suc=(
                                               last_30["percent_succeded"]),
                                              perc_fail=100-(
                                               last_30["percent_succeded"])))
                    return []
            except HTTPError:
                dispatcher.utter_message(
                    "Não estou conseguindo ter acesso a seus dados, "
                    "tem certeza que seus dados estão certos?")
            except ValueError:
                dispatcher.utter_message(
                    "Estou com problemas para me conectar, me manda "
                    "mais uma mensagem pra ver se dessa vez dá certo.")
            except NewConnectionError:
                dispatcher.utter_message(
                    "Estou com problemas para me conectar, me manda "
                    "mais uma mensagem pra ver se dessa vez dá certo.")
        else:
            dispatcher.utter_message("Para ter acesso ao relatório"
                                     " é necessário que você tenha um "
                                     "repositório do gitlab cadastrado!")
            dispatcher.utter_message("Quando quiser cadastrar é só avisar!")
            return []
