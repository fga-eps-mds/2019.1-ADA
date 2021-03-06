from rasa_core_sdk import Action
import requests
import os
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import telegram

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")
GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")
SECS = 10.0


class RerunPipeline(Action):
    def name(self):
        return "action_rerun_pipeline"

    def run(self, dispatcher, tracker, domain):
        headers = {'Content-Type': 'application/json'}
        tracker_state = tracker.current_state()
        chat_id = tracker_state["sender_id"]
        if self.check_user(chat_id, headers):
            try:
                message = tracker.latest_message.get("text")
                splitted_message = message.split()
                pipeline_id = splitted_message[-1]
                try:
                    response = requests.get(GITLAB_SERVICE_URL +
                                            "rerun_pipeline/{chat_id}/"
                                            "{pipeline_id}"
                                            .format(chat_id=chat_id,
                                                    pipeline_id=pipeline_id),
                                            timeout=SECS,
                                            headers=headers)
                except requests.exceptions.Timeout:
                    text = "Desculpa, não consegui fazer o que você"\
                           " me pediu! 😕"
                    bot = telegram.Bot(token=ACCESS_TOKEN)
                    bot = bot.send_message(chat_id=chat_id, text=text)
                else:
                    response.raise_for_status()
                    dispatcher.utter_message("Tudo certo, reiniciei sua"
                                             " pipeline!")
            except HTTPError:
                dispatcher.utter_message(
                    "Ai que pena... não consegui reiniciar a pipeline que você"
                    " me pediu 😔")
                dispatcher.utter_message(
                    "Tenta clicar novamente ai nesse botão. Se não der certo,"
                    " sugiro entrar no GitLab e tenta reiniciar você mesmo...")
            except ValueError:
                dispatcher.utter_message(
                 "Estou com problemas para encontrar seus dados agora,"
                 " me mande novamente uma mensagem mais tarde.")
            except NewConnectionError:
                dispatcher.utter_message(
                 "Estou com problemas para me conectar agora, me mande "
                 "novamente uma mensagem mais tarde.")
        else:
            dispatcher.utter_message("Para rodar novamente um pipeline"
                                     " é necessário que você tenha um "
                                     "repositório do gitlab cadastrado!")
            dispatcher.utter_message("Quando quiser cadastrar é só avisar!")
            return []

    def check_user(self, chat_id, headers):
        url = GITLAB_SERVICE_URL + "user/infos/{chat_id}".\
            format(chat_id=chat_id)
        response = requests.get(url, headers=headers)
        data = response.json()
        if data["username"] and data["repository"]:
            return True
        return False
