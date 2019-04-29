from rasa_core_sdk import Action
import requests
import os

from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError


GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")


class ActionGetPipeline(Action):
    def name(self):
        return "action_get_pipeline"

    def run(self, dispatcher, tracker, domain):
        try:

            headers = {"Content-Type": "application/json"}

            project_owner = tracker.current_slot_values()['usuario']
            project_name = tracker.current_slot_values()['repositorio']
            get_pipeline_url = GITLAB_SERVICE_URL + \
                "pipeline/{project_owner}/{project_name}".format(
                    project_owner=project_owner, project_name=project_name)
            response = requests.get(
                get_pipeline_url, headers=headers)
            received_pipeline = response.json()
            dispatcher.utter_message("Aqui está o pipeline mais recente")
            if received_pipeline["status"] == "success":
                status = "ele nos critérios de aceitação."
            else:
                status = "ele não passou nos critérios de aceitação."

            text_message = 'O Pipeline mais recente do '\
                + 'seu repositório: {status}'.format(
                    status=status)+'\n'+'Para visualizar o'\
                + 'Pipeline no GitLab acesse o link '\
                + '{web_url}'.format(status=status,
                                     web_url=received_pipeline["web_url"])

            dispatcher.utter_message(text_message)
            return []
        except HTTPError:
            dispatcher.utter_message(
                "Não consegui achar um pipeline no seu repositório, certifique-se que exite um.")
        except ValueError:
            dispatcher.utter_message(
                "Estou tendo alguns problemas, tente mais tarde.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou tendo problemas para me conectar com o gitlab.")
        except Exception:
            dispatcher.utter_message(
                "Estou tendo problemas para me conectar com o gitlab.")
