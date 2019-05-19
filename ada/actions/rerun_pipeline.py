from rasa_core_sdk import Action
import requests
import os
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")


class RerunPipeline(Action):
    def name(self):
        return "action_rerun_pipeline"

    def run(self, dispatcher, tracker, domain):
        try:
            headers = {'Content-Type': 'application/json'}
            tracker_state = tracker.current_state()
            chat_id = tracker_state["sender_id"]
            # pegar a mensagem do user referente ao botao pressionado
            message = tracker.latest_message.get("text")
            splitted_message = message.split()
            pipeline_id = splitted_message[-1]
            # fazer a outra requisicao com o id da pipeline para reinicia-la
            response = requests.get(GITLAB_SERVICE_URL +
                                    "rerun_pipeline/{chat_id}/{pipeline_id}"
                                    .format(chat_id=chat_id,
                                            pipeline_id=pipeline_id),
                                    headers=headers)
            # mensagem de sucesso
            response.raise_for_status()
            dispatcher.utter_message("Tudo certo, reiniciei sua pipeline!")
            # tratamento de erros
        except HTTPError:
            dispatcher.utter_message(
                "Ai que pena... não consegui reiniciar a pipeline que você\
                 me pediu 😔")
            dispatcher.utter_message(
                "Tenta clicar novamente ai nesse botão. Se não der certo, \
                 sugiro entrar no GitLab e tenta reiniciar você mesmo...")
        except ValueError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
