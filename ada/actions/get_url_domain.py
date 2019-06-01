from rasa_core_sdk import Action
import requests
import os
import json
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import telegram

GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")

class UrlDeploy(Action):
    def name(self):
        return "action_get_url_domain"

    def run(self, dispatcher, tracker, domain):
        try:
            headers = {'Content-Type': 'application/json'}
            tracker_state = tracker.current_state()
            chat_id = tracker_state["sender_id"]
            message = tracker.latest_message.get("text")
            user_domain= {"domain":message}
            user_domain=json.dumps(user_domain)
            response = requests.post(GITLAB_SERVICE_URL + "user/domain/{chat_id}"
                                                        .format(chat_id=chat_id),
                                                        data=user_domain,
                                                        headers=headers)
            dispatcher.utter_message("Tudo certo! Ficarei monitorando para você, caso aconteça algo eu irei te avisar.")

        except ValueError:
            dispatcher.utter_message("Estou tendo dificuldade pra encontrar "
                                     "sua aplicação. "
                                     "Tenta de novo mais tarde. Ok?")
        except HTTPError:
            dispatcher.utter_message("Sinto muito, mas no momento não consigo "
                                     "cadastrar seu domínio. "
                                     "Tenta de novo mais tarde. Ok?")
