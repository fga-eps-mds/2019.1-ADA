from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import requests
import telegram
import json
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import sys

GITHUB_SERVICE_URL = os.environ.get("GITHUB_SERVICE_URL", "")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")

class SetRepositoryGitHub(Action):
    def name(self):
        return "action_set_repository_github"

    def run(self, dispatcher, tracker, domain):
        try:
            headers = {"Content-Type": "application/json"}
            tracker_state = tracker.current_state()
            sender_id = tracker_state['sender_id']
            message = tracker.latest_message.get('text')

            message_list = message.split()
            repo_name = message_list[-1]

            bot = telegram.Bot(token=ACCESS_TOKEN)
            self.save_repo_to_db(headers, message, repo_name, sender_id)
            selected_repo = "Ok, vou ficar monitorando "\
                            "o repositório {rep}.".format(
                                rep=repo_name)
            dispatcher.utter_message(selected_repo)

            return [SlotSet('repository_github', repo_name)]
        except KeyError:
            dispatcher.utter_message(
                "Não consegui encontrar o seu usuário no GitHub, "
                "por favor verifique ele e me manda novamente.")
        except IndexError:
            dispatcher.utter_message(
                "Não consegui encontrar o seu usuário no GitHub, "
                "por favor verifique ele e me manda novamente.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        except ValueError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        except HTTPError:
            existent_user = "Eu vi aqui que você já cadastrou o usuário "\
                            "do GitHub. Sinto muito, mas no momento "\
                            "não é possível cadastrar um novo usuário"\
                            " do GitHub ou alterá-lo."
            dispatcher.utter_message(existent_user)

    def save_repo_to_db(self, headers, message, repo_name, sender_id):
        db_json = {"repository_name": repo_name, "chat_id": sender_id}
        db_url = GITHUB_SERVICE_URL + \
            "user/repo"
        db_json = json.dumps(db_json)
        response = requests.post(url=db_url, data=db_json, headers=headers)
        response.raise_for_status()
