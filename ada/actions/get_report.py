from rasa_core_sdk import Action
import requests
import os
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")


class Report(Action):
    def name(self):
        return "action_get_report"

    def run(self, dispatcher, tracker, domain):
        try:
            headers = {'Content-Type': 'application/json'}
            tracker_state = tracker.current_state()
            chat_id = tracker_state["sender_id"]

            response = requests.get(GITLAB_SERVICE_URL +
                                    "report/{chat_id}"
                                    .format(chat_id=chat_id), headers=headers)
            report_project = response.json()
            # print(report_project, file=sys.stderr)
            project = report_project[0]["project"]
            dispatcher.utter_message("Primeiramente, o seu projeto "
                                     "se chama {project_name}"
                                     " e se encontra disponível "
                                     "nesse site {web_url}"
                                     .format(project_name=project["name"],
                                             web_url=project["web_url"]))

            text_message = "As branches do seu repositório são as seguintes:\n"
            for item in report_project:
                for value in item["branches"]["name"]:
                    text_message += "▪️ {names}\n".format(names=value)
            dispatcher.utter_message(text_message)
            commits = report_project[0]["commits"]["last_commit"]
            dispatcher.utter_message("O último commit foi feito por"
                                     "{author_name}"
                                     "no dia {author_date} com o título"
                                     "{title}.".format(
                                         author_name=commits["author_name"],
                                         author_date=commits["authored_date"],
                                         title=commits["title"]))

            pipeline = report_project[0]["pipelines"]
            dispatcher.utter_message("O atual pipeline possui id "
                                     "{pipeline_id}"
                                     "e nome {pipeline_name}"
                                     .format(
                                             pipeline_id=(
                                              pipeline["current_pipeline_id"]),
                                             pipeline_name=(
                                              pipeline["current_pipeline_name"]
                                              )))

            message_report_todo = self.message_report(pipeline)
            dispatcher.utter_message("Sobre o projeto como um todo:\n📌 " +
                                     message_report_todo)

            last_7 = pipeline["recents_pipelines"]["last_7_days"]
            last_30 = pipeline["recents_pipelines"]["last_30_days"]

            message_report_7 = self.message_report(last_7)
            dispatcher.utter_message("Sobre os últimos 7 dias:\n⚒ " +
                                     message_report_7)

            message_report_30 = self.message_report(last_30)
            dispatcher.utter_message("Sobre os últimos 30 dias:\n⚒ " +
                                     message_report_30)
            return []
        except HTTPError:
            dispatcher.utter_message(
                "Não estou conseguindo ter acesso a seus dados, tem certeza"
                "que seus dados estão certos?")
        except ValueError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")

    def message_report(self, pipeline):
        return ("Número total de pipelines: {total}\n"
                "☑️ {success} obtiveram sucesso\n"
                "❗️ {fail} falharam\n"
                "☑️ A porcentagem de sucesso foi:"
                "{perc_suc}\n❗️ E a porcentagem de falhas"
                "foi: {perc_fail}\n".format(
                    total=(
                        pipeline["number_of_pipelines"]),
                    success=(
                        pipeline["succeded_pipelines"]),
                    fail=(
                        pipeline["failed_pipelines"]),
                    perc_suc=(
                        pipeline["percent_succeded"]),
                    perc_fail=100-(
                        pipeline["percent_succeded"])))
