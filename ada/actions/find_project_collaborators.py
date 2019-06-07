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
        try:
            headers = {'Content-Type': 'application/json'}
            tracker_state = tracker.current_state()
            chat_id = tracker_state["sender_id"]
            # tentar fazer a requisicao
            url = (GITHUB_SERVICE_URL + "api/find_collaborators/{chat_id}"
                   .format(chat_id=chat_id))
            response = requests.get(url, headers=headers)
            response.raise_for_status()

        except HTTPError:
            dispatcher.utter_message(
                "Ai que pena... não consegui encontrar os contribuidores do"
                " seu projeto 😔")
            dispatcher.utter_message(
                "Vamos tentar de novo daqui a pouco, pode ser ? É só você me"
                " lembrar !")
        except ValueError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")

        else:
            project_collaborators = response.json()
            len_collaborators = len(project_collaborators["collaborators"])
            if len_collaborators == 1:
                dispatcher.utter_message("Há uma pessoa trabalhando no seu "
                                         "projeto, o usuário dela é " +
                                         project_collaborators["collaborators"]
                                                              [0])
            elif len_collaborators == 2:
                dispatcher.utter_message("Há duas pessoas colaborando com "
                                         "projeto, os usuários delas são "
                                         "➡️" +
                                         project_collaborators["collaborators"]
                                                              [0])
            elif len_collaborators >= 2:
                dispatcher.utter_message("Existem vários colaboradores "
                                         "no seu projeto.")
                dispatcher.utter_message("Esses são os usuários deles:")
                for item in project_collaborators["collaborators"]:
                    dispatcher.utter_message(item)
            else:
                dispatcher.utter_message("Que pena...ninguém está contribuindo"
                                         " para o seu projeto :(")
