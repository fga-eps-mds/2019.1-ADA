from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import requests
import logging
import telegram
import json
import sys
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError

GITLAB_SERVICE_URL = os.environ.get("GITLAB_SERVICE_URL", "")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")


class ActionSetUser(Action):
    def name(self):
        return "action_set_user"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker_state = tracker.current_state()
            sender_id = tracker_state['sender_id']

            message = tracker.latest_message.get('text')
            message = message.split()
            project_owner = message[len(message)-1]

            bot = telegram.Bot(token=ACCESS_TOKEN)
            bot.send_message(chat_id=sender_id,
                             text="Ok, {user}, anotei aqui, vou dar uma conferida pra ver se está tudo certo.".format(user=project_owner))
            headers = {"Content-Type": "application/json"}
            repo_names = self.build_buttons(project_owner, headers)
            reply_markup = telegram.InlineKeyboardMarkup(repo_names)
            bot.send_message(chat_id=sender_id,
                             text="Encontrei esses repositórios na sua conta. Qual você quer que eu monitore? Clica nele!",
                             reply_markup=reply_markup)
            self.save_user_to_db(headers, project_owner, sender_id)
            return [SlotSet('usuario', project_owner)]        
        except KeyError:
            dispatcher.utter_message(
                "Não consegui encontrar o seu usuário no GitLab, por favor verifique ele e me manda novamente.")
        except IndexError:
            dispatcher.utter_message(
                "Não consegui encontrar o seu usuário no GitLab, por favor verifique ele e me manda novamente.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda mais uma mensagem pra ver se dessa vez dá certo.")
        except ValueError:
            dispatcher.utter_message("Estou com problemas para me conectar, me manda mais uma mensagem pra ver se dessa vez dá certo.")
        except HTTPError:
            existent_user = "Eu vi aqui que você já cadastrou o usuário do GitLab. "\
                            "Sinto muito, mas no momento não é possível "\
                            "cadastrar um novo usuário do GitLab "\
                            "ou alterá-lo."
            dispatcher.utter_message(existent_user)
        except Exception:
            dispatcher.utter_message("Oloquinho meu")
        
    def build_buttons(self, project_owner, headers):        
        get_repository = GITLAB_SERVICE_URL + \
            "user/{project_owner}".format(
                project_owner=project_owner)
        response = requests.get(
            url=get_repository, headers=headers)

        received_repositories = response.json()
        buttons = []
        for repositorio in received_repositories["repositories"]:
            project_name = repositorio.split('/')
            project_name = project_name[-1]
            buttons.append(telegram.InlineKeyboardButton(
                text=project_name, callback_data="meu repositorio é " + repositorio))
        repo_names = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
        return repo_names

    def save_user_to_db(self, headers, project_owner, sender_id):
        get_user_id = GITLAB_SERVICE_URL + \
            "user/id/{project_owner}".format(
                project_owner=project_owner)
        response = requests.get(
            url=get_user_id, headers=headers)
        user_id = response.json()
        db_json = {"gitlab_user": project_owner, "chat_id": sender_id,
                   "gitlab_user_id":  str(user_id["user_id"])}
        db_url = GITLAB_SERVICE_URL + \
            "webhooks/user"
        db_json = json.dumps(db_json)
        post_request = requests.post(url=db_url, data=db_json, headers=headers)
        post_request.raise_for_status()
