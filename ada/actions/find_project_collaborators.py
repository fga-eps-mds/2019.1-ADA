from rasa_core_sdk import Action
import requests
import os
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError


ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")
GITHUB_SERVICE_URL = os.getenv("GITHUB_SERVICE_URL", "")


class FindProjectCollaborators(Action):
    def name(self):
        return "action_find_project_collaborators"

    def run(self, dispatcher, tracker, domain):
        headers = {'Content-Type': 'application/json'}
        tracker_state = tracker.current_state()
        chat_id = tracker_state["sender_id"]
        if self.check_user(chat_id, headers):
            try:
                url = (GITHUB_SERVICE_URL + "api/find_collaborators/{chat_id}"
                       .format(chat_id=chat_id))
                response = requests.get(url, headers=headers)
                response.raise_for_status()

            except HTTPError:
                dispatcher.utter_message(
                    "Ai que pena... não consegui encontrar os "
                    "contribuidores do seu projeto 😔")
                dispatcher.utter_message(
                    "Vamos tentar de novo daqui a pouco, pode ser ? É só "
                    "você me lembrar !")
            except ValueError:
                dispatcher.utter_message(
                 "Estou com problemas para encontrar seus dados agora,"
                 "me mande novamente uma mensagem mais tarde.")
            except NewConnectionError:
                dispatcher.utter_message(
                 "Estou com problemas para me conectar agora, me mande "
                 "novamente uma mensagem mais tarde.")

            else:
                project_collaborators = response.json()
                len_collaborators = len(project_collaborators["collaborators"])
                if len_collaborators == 1:
                    dispatcher.utter_message("Há uma pessoa trabalhando no seu"
                                             " projeto, o usuário dela é " +
                                             project_collaborators
                                             ["collaborators"][0])
                elif len_collaborators == 2:
                    dispatcher.utter_message("Há duas pessoas colaborando com "
                                             "projeto, os usuários delas são "
                                             "➡️" +
                                             project_collaborators
                                             ["collaborators"][0] +
                                             "➡️" +
                                             project_collaborators
                                             ["collaborators"][1])
                elif len_collaborators > 2:
                    dispatcher.utter_message("Existem vários colaboradores "
                                             "no seu projeto.")
                    dispatcher.utter_message("Esses são os usuários deles:")
                    for item in project_collaborators["collaborators"]:
                        dispatcher.utter_message(item)
                else:
                    dispatcher.utter_message(
                     "Que pena...ninguém está contribuindo para o seu projeto"
                     " :(")
        else:
            dispatcher.utter_message("Para ter acesso aos contribuidores"
                                     " é necessário que você tenha um "
                                     "repositório do github cadastrado!")
            dispatcher.utter_message("Quando quiser cadastrar é só avisar!")
            return []

    def check_user(self, chat_id, headers):
        url = GITHUB_SERVICE_URL + "user/infos/{chat_id}".\
            format(chat_id=chat_id)
        response = requests.get(url, headers=headers)
        data = response.json()
        if data["username"] and data["repository"]:
            return True
        return False
