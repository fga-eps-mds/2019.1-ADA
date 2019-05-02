from rasa_core_sdk import Action
import requests
import os

from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError


GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")


class ActionGetPipeline(Action):
    def name(self):
        return "action_get_pipeline"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker_state = tracker.current_state()
            sender_id = tracker_state['sender_id']
            headers = {"Content-Type": "application/json"}

            get_pipeline_url = GITLAB_SERVICE_URL + \
                "pipeline/{sender_id}".format(sender_id=sender_id)
            response = requests.get(
                get_pipeline_url, headers=headers)
            received_pipeline = response.json()
            dispatcher.utter_message(
                "Vou procurar o resultado do seu pipeline aqui, já volto.")
            if received_pipeline["status"] == "success":
                status = "passou nos critérios de aceitação."
            else:
                status = "não passou nos critérios de aceitação."

            text_message = 'Encontrei, e ele ' \
                + '{status}.'.format(
                    status=status)+'\n'+'Para visualizar '\
                + 'mais informações sobre ele acesse o link '\
                + '{web_url}'.format(status=status,
                                     web_url=received_pipeline["web_url"])

            dispatcher.utter_message(text_message)
            return []
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