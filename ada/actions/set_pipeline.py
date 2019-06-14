from rasa_core_sdk import Action
import requests
import os
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import telegram

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")
GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")
SECS = 10.0


class ActionSetPipeline(Action):
    def name(self):
        return "action_set_pipeline"

    def run(self, dispatcher, tracker, domain):
        slot_repo = tracker.get_slot("repository_gitlab")
        if slot_repo:

            try:
                tracker_state = tracker.current_state()
                sender_id = tracker_state["sender_id"]
                headers = {"Content-Type": "application/json"}
                try:
                    response = requests.get(GITLAB_SERVICE_URL +
                                            "build/{sender_id}"
                                            .format(sender_id=sender_id),
                                            timeout=SECS,
                                            headers=headers)
                except requests.exceptions.Timeout:
                    text = "Desculpa, não consegui fazer o "\
                           "que você me pediu! 😕"
                    bot = telegram.Bot(token=ACCESS_TOKEN)
                    bot = bot.send_message(chat_id=sender_id, text=text)
                else:
                    job_build = response.json()
                    dispatcher.utter_message(
                        "Vou procurar o resultado do seu pipeline aqui,"
                        " já volto.")
                    if job_build[0]["pipeline_status"] == "success":
                        status = "passou nos critérios de aceitação"
                    elif job_build[0]["pipeline_status"] == "failed":
                        status = "não passou nos critérios de aceitação"
                    else:
                        status = "ainda está em andamento"

                    text_message_2 = "Encontrei seu pipeline mais " \
                        "recente, e ele " + "{status}.".format(status=status)

                    dispatcher.utter_message(text_message_2)

                    text_message = "Os passos da build são:\n"

                    for i, item in enumerate(job_build):

                        if job_build[i]["status"] == "success":
                            status = "✅"
                        elif job_build[i]["status"] == "failed":
                            status = "❌"
                        else:
                            status = "🔄"

                        text_message += "{status} {job_name}\n" \
                                        .format(status=status,
                                                job_name=job_build
                                                [i]["job_name"])

                    dispatcher.utter_message("A build #{job_id} "
                                             "da branch {branch}, "
                                             "commit {commit}",
                                             "está no estágio de {stage}"
                                             .format(job_id=job_build
                                                     [0]["job_id"],
                                                     branch=job_build
                                                     [0]["branch"],
                                                     commit=job_build
                                                     [0]["commit"],
                                                     stage=job_build
                                                     [0]["stage"]))

                    dispatcher.utter_message(text_message)

                    dispatcher.utter_message("Para visualizar seu Pipeline "
                                             "no GitLab, acesse o link"
                                             " {web_url}".format(
                                               web_url=job_build[0]
                                               ["pipeline_url"]))
            except KeyError:
                dispatcher.utter_message(
                    "Não consegui encontrar o seu pipeline no GitLab, "
                    "por favor verifique se existe um e me manda novamente.")
            except IndexError:
                dispatcher.utter_message(
                    "Não consegui encontrar o seu pipeline no GitLab, "
                    "por favor verifique se existe um e me manda novamente.")
            except HTTPError:
                dispatcher.utter_message(
                    "Não consegui achar um pipeline no seu repositório, "
                    "tenta conferir se existe um e tente novamente.")
            except ValueError:
                dispatcher.utter_message(
                    "Estou com problemas para me conectar, me manda "
                    "mais uma mensagem pra ver se dessa vez dá certo.")
            except NewConnectionError:
                dispatcher.utter_message(
                    "Estou com problemas para me conectar, me manda "
                    "mais uma mensagem pra ver se dessa vez dá certo.")
        else:
            dispatcher.utter_message("Para ter acesso ao pipeline"
                                     " é necessário que você tenha um "
                                     "repositório do gitlab cadastrado!")
            dispatcher.utter_message("Quando quiser cadastrar é só avisar!")
            return []
