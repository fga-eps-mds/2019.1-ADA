from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import requests
import telegram
import json
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import sys

GITHUB_SIGNUP_URL = os.environ.get("GITHUB_SIGNUP_URL", "")

class ActionStart(Action):
    def name(self):
        return "action_start"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker_state = tracker.current_state()
            sender_id = tracker_state['sender_id']
            
            github_signup_url = GITHUB_SIGNUP_URL + str(sender_id)
            url = "https://github.com/login/oauth/authorize?"\
                  "client_id=320d70aa1e4d730fa181"\
                  "&redirect_uri={url}&scope"\
                  "=admin%3Arepo_hook%2Crepo".format(url=github_signup_url)

            message = "Oláaaaa, sou a Ada! Sou responsável "\
                      "por ajudar você no monitoramento de "\
                      "produção com seus repositórios. "\
                      "Caso queira saber mais, me peça ajuda. "\
                      "Agora, pra gente começar eu vou pedir "\
                      "pra você clicar nesse link aqui, {link}. "\
                      .format(link=url)
            dispatcher.utter_message(message)
        except ValueError:
            dispatcher.utter_message("Deu errado")
            