from rasa_core_sdk import Action
import requests
import os

from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError


GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")


class BuildStage(Action):
    def name(self):
        return "action_build_stage"

    def run(self, dispatcher, tracker, domain):
        is_there_any_build = False
        try:
            tracker_state = tracker.current_state()
            sender_id = tracker_state['sender_id']

            dispatcher.utter_message("Certo! Encontrei a build mais "
                                     "recente do seu repositório.")
            headers = {'Content-Type': 'application/json'}            
            response = requests.get(GITLAB_SERVICE_URL +
                                    "build/{sender_id}"
                                    .format(sender_id=sender_id),
                                    headers=headers)
            job_build = response.json()

            text_message = "Os passos da build são:\n"

            for i, item in enumerate(job_build):

                if job_build[i]['status'] == "success":
                    status = "✅"
                elif job_build[i]['status'] == "failed":
                    status = "❌"
                else:
                    status = "🔄"

                text_message += "{status} {job_name}\n" \
                                .format(status=status,
                                        job_name=job_build[i]['job_name'])

            dispatcher.utter_message('A build #{job_id} '
                                     'da branch {branch}, '
                                     'commit "{commit}", '
                                     'está no estágio de "{stage}".'
                                     .format(job_id=job_build[0]['job_id'],
                                             branch=job_build[0]['branch'],
                                             commit=job_build[0]['commit'],
                                             stage=job_build[0]['stage']))

            dispatcher.utter_message(text_message)

            dispatcher.utter_message("Para visualizar sua build "
                                     "no GitLab acesse o link {pipe_url}"
                                     .format(pipe_url=job_build[0]['web_url']))

            is_there_any_build = True
        except HTTPError:
            dispatcher.utter_message(
                "Não estou conseguindo achar uma build no seu repositório, certifique-se que realmente existe uma.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou tendo problemas para me conectar com o gitlab.")
        except ValueError:
            dispatcher.utter_message(
                "Estou tendo alguns problemas, tente mais tarde.")
            if(not is_there_any_build):
                default = "Não há build's em andamento, "\
                    "mas continuo te informando."
                dispatcher.utter_message(default)
