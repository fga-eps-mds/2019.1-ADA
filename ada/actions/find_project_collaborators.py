from rasa_core_sdk import Action
import requests
import os
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import telegram

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
            response = requests.get(GITHUB_SERVICE_URL + "/api/\
                                    find_collaborators/{chat_id}".format(
                                    chat_id=chat_id
                                    ))
            response.raise_for_status()

        except HTTPError:
            dispatcher.utter_message(
                "Ai que pena... não consegui encontrar os contribuidores do \
                 seu projeto 😔")
            dispatcher.utter_message(
                "Vamos tentar de novo daqui a pouco, pode ser ? É só você me \
                 lembrar !")
        except ValueError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")

        else:
            project_collaborators = json.loads(response) # converte o json em
            if len(project_collaborators) > 2:           # lista
                dispatcher.utter_message("Hmmm parece que você não está \
                                          trabalhando sozinho :)")
                dispatcher.utter_message("Esses são seus colegas de trabalho:")
                for item in project_collaborators:
                    dispatcher.utter_message(item)

            elif len(project_collaborators) == 2:
                dispatcher.utter_message("Só há 2 pessoas trabalhando no seu \
                                          projeto:")
                dispatcher.utter_message("São elas " + project_collaborators[0]
                                          + "e " + project_collaborators[1])

            elif len(project_collaborators) == 1:
                dispatcher.utter_message("A princípio só " +
                                          project_collaborators[0] + "trabalha \
                                          no seu projeto...")

            else: # ninguém trabalha no projeto
                dispatcher.utter_message("Que pena...ninguém está contribuindo \
                                          para o seu projeto :(")
