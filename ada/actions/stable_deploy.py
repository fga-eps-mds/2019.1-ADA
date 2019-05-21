from rasa_core_sdk import Action
import requests
import os
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")


class StableDeploy(Action):
    def name(self):
        return "action_stable_deploy"

    def run(self, dispatcher, tracker, domain):
        try:
            # fazer a requisicao ao microservico ada-gitlab
            headers = {'Content-Type': 'application/json'}
            tracker_state = tracker.current_state()
            chat_id = tracker_state["sender_id"]
            response = requests.get(GITLAB_SERVICE_URL +
                                    "stable_deploy/{chat_id}"
                                    .format(chat_id=chat_id), headers=headers)
            response.raise_for_status()
        # informar ao usuário : caso de falha / tratamento de erros
        except HTTPError:
            dispatcher.utter_message(
                "Ai que pena... não consegui fazer o deploy da versão\
                 estável mais recente do seu projeto 😔")
            dispatcher.utter_message(
                "Você quer que eu tente novamente agora ?")
        except ValueError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")

        else:
            # informar ao usuário : caso de sucesso
            dispatcher.utter_message("🏆 Pronto! Seu projeto está sendo \
                                      colocado na versão estável mais \
                                      recente.")
