from rasa_core_sdk import Action
import requests
import os


GITHUB_SERVICE_URL = os.environ.get("GITHUB_SERVICE_URL", "")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")


class ChangeGithubRepo(Action):
    def name(self):
        return "action_change_github_repository"

    def run(self, dispatcher, tracker, domain):
        try:
            headers = {'Content-Type': 'application/json'}
            tracker_state = tracker.current_state()
            chat_id = tracker_state["sender_id"]
            requests.get(GITHUB_SERVICE_URL +
                        "user/change_repo/{chat_id}"
                        .format(chat_id=chat_id),
                        headers=headers)
        except KeyError:
            dispatcher.utter_message(
                "Não consegui encontrar o seu usuário no GitHub, "
                "por favor verifique ele e me manda novamente.")
        except IndexError:
            dispatcher.utter_message(
                "Não consegui encontrar o seu usuário no GitHub, "
                "por favor verifique ele e me manda novamente.")
        except ValueError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
          
