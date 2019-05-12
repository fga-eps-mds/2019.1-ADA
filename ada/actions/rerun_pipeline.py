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
            # response = requests.get(GITLAB_SERVICE_URL +
            #                         "rerun_pipeline/{chat_id}"
            #                         .format(chat_id=chat_id), headers=headers)
            # restarted_pipeline = response.json()
            # TODO HERE

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
