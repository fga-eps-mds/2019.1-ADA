from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import json
import os
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import telegram

GITLAB_SERVICE_URL = os.environ.get("GITLAB_SERVICE_URL", "")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")


class SetRepositoryGitLab(Action):
    def name(self):
        return "action_set_repository_gitlab"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker_state = tracker.current_state()
            sender_id = tracker_state['sender_id']
            message = tracker.latest_message.get('text')

            headers = {"Content-Type": "application/json"}
            message_list = message.split()
            repo_id = message_list[-1]
            bot = telegram.Bot(token=ACCESS_TOKEN)
            project_name = self.get_project_name(headers, repo_id,
                                                 sender_id)
            self.save_repo_to_db(headers, repo_id, project_name,
                                 sender_id)
            selected_repo = "Ok, vou ficar monitorando "\
                            "o repositório {rep}!".format(
                                rep=project_name)
            bot.send_message(chat_id=sender_id,
                             text=selected_repo)
            info_message = "Caso queira saber o que eu faço, "\
                           "me peça ajuda 😉"
            bot.send_message(chat_id=sender_id,
                             text=info_message)
            return [SlotSet('repository_gitlab', repo_id)]
        except ValueError:
            dispatcher.utter_message("Estou tendo dificuldade pra encontrar "
                                     "os dados do repositório. "
                                     "Tenta de novo mais tarde. Ok?")
        except HTTPError:
            existent_repo = "Eu vi aqui que você já tem um projeto "\
                            "cadastrado. Sinto muito, mas no momento não é "\
                            "possível cadastrar um projeto novo ou alterá-lo."
            dispatcher.utter_message(existent_repo)
        except KeyError:
            dispatcher.utter_message(
                "Não consegui encontrar o seu repositório no GitLab, "
                "por favor verifique ele e me manda novamente.")
        except IndexError:
            dispatcher.utter_message(
                "Não consegui encontrar o seu repositório no GitLab, "
                "por favor verifique ele e me manda novamente.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou tendo alguns problemas, tenta me mandar essa "
                "mensagem de novo ou de uma forma diferente")

    def get_project_name(self, headers, project_id, sender_id):
        url = GITLAB_SERVICE_URL + \
              "user/project/{sender_id}/"\
              "{project_id}".format(sender_id=sender_id,
                                    project_id=project_id)
        response = requests.get(url=url, headers=headers)
        project_json = response.json()
        project_name = project_json["project_fullname"]
        return project_name

    def save_repo_to_db(self, headers, project_id, project_fullname,
                        sender_id):
        db_json = {"project_name": project_fullname, "chat_id": sender_id,
                   "project_id": str(project_id)}
        db_url = GITLAB_SERVICE_URL + \
            "webhooks/repo"\
            .format(sender_id=sender_id)
        db_json = json.dumps(db_json)
        response = requests.post(url=db_url, data=db_json, headers=headers)
        response.raise_for_status()
        set_webhook_url = GITLAB_SERVICE_URL + \
            "webhook"
        webhook_json = {
            "project_id": str(project_id),
            "chat_id": sender_id
        }
        webhook_json = json.dumps(webhook_json)
        response = requests.post(url=set_webhook_url,
                                 data=webhook_json,
                                 headers=headers)
        response.raise_for_status()
