from rasa_core_sdk import Action
import requests
import os
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")


class RerunPipeline(Action):
    def name(self):
        return "action_rerun_pipeline"

    def run(self, dispatcher, tracker, domain):
        try:
            headers = {'Content-Type': 'application/json'}
            tracker_state = tracker.current_state()
            chat_id = tracker_state["sender_id"]
             response = requests.get(GITLAB_SERVICE_URL +
                                     "rerun_pipeline/{chat_id}"
                                     .format(chat_id=chat_id), headers=headers)
             pipelines = response.json()
             pipelines_names = []
             for i in pipelines:
                 pipelines_names.append(i["names"])

            if pipelines_names:
                dispatcher.utter_message("Então... encontrei as seguintes\
                                      pipelines:")
                dispatcher.utter_message(pipelines_names)
                dispatcher.utter_message("Qual delas você quer reiniciar ?\
                                          me fala o nome de uma só viu rsrs")
                # TODO HERE -> pegar a mensagem do usuario p identificar a
                # pipeline que ele quer reiniciar
                # pipeline_to_be_reruned = tracker_state ?????

                # TODO HERE -> fazer a outra requisicao com o id da pipeline
                # para reinicia-la
                # response = requests.get(GITLAB_SERVICE_URL +
                #                    "rerun_pipeline/{chat_id}/{pipeline_id}"
                #                    .format(chat_id=chat_id, pipeline_id=
                #                     pipeline_id), headers=headers)

            else :
                dispatcher.utter_message("Não encontrei nenhuma pipeline\
                                          no seu projeto :/")

        except HTTPError:
            dispatcher.utter_message(
                "Não estou conseguindo ter acesso a seus dados, tem certeza"
                "que seus dados estão certos?")
        except ValueError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
