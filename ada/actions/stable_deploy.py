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
            response.raise_for_status()

        # informar ao usuário : caso de falha / tratamento de erros
        except HTTPError:
            dispatcher.utter_message(
                "Ai que pena... não consegui fazer o deploy da versão\
                 estável mais recente do seu projeto 😔")
            dispatcher.utter_message(
                "Podemos tentar novamente mais tarde... pode ser ?\
                 Só me lembra de fazer isso :)")
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
