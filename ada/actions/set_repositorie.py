from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import json
import os
import sys

GITLAB_SERVICE_URL = os.environ.get("GITLAB_SERVICE_URL", "")

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
            self.save_repo_to_db(headers, repo_name, message, sender_id)
            dispatcher.utter_message(
                "Ok, vou ficar monitorando o repositório {rep}.".format(rep=repo_name))
            
            return [SlotSet('repositorio', repo_name)]
        except ValueError:
            dispatcher.utter_message(ValueError)

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

    def save_repo_to_db(self, headers, project_name, message, sender_id):
        project_id = self.get_project_id(headers, message)
        db_json = {"project_name": project_name, "chat_id": sender_id,
                   "project_id": str(project_id)}
        db_url = GITLAB_SERVICE_URL + \
            "webhooks/repo"
        db_json = json.dumps(db_json)
        response = requests.post(url=db_url, data=db_json, headers=headers)
        response.raise_for_status()