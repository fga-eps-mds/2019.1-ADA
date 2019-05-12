from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
from urllib3.exceptions import NewConnectionError
GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")


class ActionIssueName(Action):
    def name(self):
        return "action_issue_name"

    def run(self, dispatcher, tracker, domain):
        try:
            message = tracker.latest_message.get('text')
            issue_name = message[7:]
        except ValueError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")

        else:
            return [SlotSet('issue_name', issue_name)]
