from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random

class ActionGetBuild(Action):
   def name(self):
      return "get_build"

   def run(self, dispatcher, tracker, domain):
        try:
          dispatcher.utter_message("Status das últimas builds do processo:")
          headers = {
              'Content-Type': 'application/json',
              'PRIVATE-TOKEN': '[GITLAB_TOKEN]',
          }
          response = requests.get('https://gitlab.com/api/v4/projects/adabot%2Fada-gitlab/jobs', headers=headers)
          requests_build = response.json()
          for i in [0,1,2]:
            dispatcher.utter_message(requests_build[i]['web_url'])
            dispatcher.utter_message(requests_build[i]['status'])
        except ValueError:
          dispatcher.utter_message(ValueError)