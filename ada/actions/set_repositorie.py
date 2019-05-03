from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import json
import os
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError

GITLAB_SERVICE_URL = os.environ.get("GITLAB_SERVICE_URL", "")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")
GITLAB_WEBHOOK_URL = os.environ.get("GITLAB_WEBHOOK_URL", "")


class ActionSetRepositorie(Action):
    def name(self):
        return "action_set_repositorie"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker_state = tracker.current_state()
            sender_id = tracker_state['sender_id']
            message = tracker.latest_message.get('text')

            headers = {"Content-Type": "application/json"}
            message_list = message.split('/')
            repo_name = message_list[-1]
            # bot = telegram.Bot(token=ACCESS_TOKEN)
            glab_webhook_url = self.save_repo_to_db(headers, repo_name,
                                                    message, sender_id)
            selected_repo = "Ok, vou ficar monitorando "\
                            "o repositório {rep}. "\
                            "Agora, você pode me pedir "\
                            "informações sobre seus pipelines ou "\
                            "relatórios informacionais "\
                            "do seu repositório.".format(rep=repo_name)
            # bot_message = bot.send_message(chat_id=sender_id,
            #                  text=selected_repo)
            # bot.editMessageReplyMarkup(chat_id=sender_id,
            #                            message_id =
            #                            bot_message.message_id - 1,
            #                            reply_markup=[])
            set_webhook_msg = "Para receber notificações sobre "\
                              "resultados do pipeline "\
                              "adicione esse link {} "\
                              "nas configurações de integração do "\
                              "seu repositório, que ficam aqui "\
                              "{}. Após selecione a opção "\
                              "de pipeline events para eu enviar "\
                              "notificação sobre os seus pipelines"\
                              .format(glab_webhook_url["gitlab_webhook_url"],
                                      glab_webhook_url["webhook_url"])

            dispatcher.utter_message(selected_repo)
            dispatcher.utter_message(set_webhook_msg)

            return [SlotSet('repositorio', repo_name)]
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

    def get_project_id(self, headers, message):
        message_list = message.split('/')
        project_owner = message_list[0]
        project_owner = project_owner.split(' ')
        project_owner = project_owner[-1]
        project_name = message_list[-1]
        get_user_repo = GITLAB_SERVICE_URL + \
            "user/repo/{project_owner}/"\
            "{project_name}".format(
                project_owner=project_owner,
                project_name=project_name)
        project_response = requests.get(
            url=get_user_repo, headers=headers)
        project_id = project_response.json()
        return project_id["project_id"]

    def get_user_id(self, message, headers):
        message_list = message.split('/')
        project_owner = message_list[0]
        project_owner = project_owner.split(' ')
        project_owner = project_owner[-1]
        user_url = GITLAB_SERVICE_URL + "user/id/{}".format(project_owner)
        user_response = requests.get(url=user_url, headers=headers)
        user_json = user_response.json()
        user_id = user_json["user_id"]
        return str(user_id)

    def save_repo_to_db(self, headers, project_name, message, sender_id):
        project_id = self.get_project_id(headers, message)
        db_json = {"project_name": project_name, "chat_id": sender_id,
                   "project_id": str(project_id)}
        db_url = GITLAB_SERVICE_URL + \
            "webhooks/repo"
        db_json = json.dumps(db_json)
        response = requests.post(url=db_url, data=db_json, headers=headers)
        response.raise_for_status()
        user_id = self.get_user_id(message, headers)

        message_list = message.split('/')
        project_owner = message_list[0]
        project_owner = project_owner.split(' ')
        project_owner = project_owner[-1]
        project_name = message_list[-1]
        gitlab_webhook_url = GITLAB_WEBHOOK_URL + str(user_id) + '/'\
                                                + str(project_id)
        set_webhook_url = 'https://gitlab.com/' + project_owner + '/'\
                                                + project_name\
                                                + '/settings/integrations'
        return {"gitlab_webhook_url": gitlab_webhook_url,
                "webhook_url": set_webhook_url}
