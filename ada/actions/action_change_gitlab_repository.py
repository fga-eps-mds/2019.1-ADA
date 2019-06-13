from rasa_core_sdk import Action
import requests
import os


GITLAB_SERVICE_URL = os.getenv("GITLAB_SERVICE_URL", "")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")


class ChangeGitlabRepo(Action):
    def name(self):
        return "action_change_gitlab_repository"

    def run(self, dispatcher, tracker, domain):
        headers = {'Content-Type': 'application/json'}
        tracker_state = tracker.current_state()
        chat_id = tracker_state["sender_id"]
        requests.get(GITLAB_SERVICE_URL +
                     "user/change_repo_gitlab/{chat_id}"
                     .format(chat_id=chat_id),
                     headers=headers)
