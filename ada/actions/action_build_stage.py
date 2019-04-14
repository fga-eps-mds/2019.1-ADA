from rasa_core_sdk import Action
import requests

class BuildStage(Action):
    def name(self):
        return "action_build_stage"

    def run(self, dispatcher, tracker, domain):
        is_there_any_build = False
        if(is_there_any_build):
            default = "Não há build's em andamento, \
                       mas continuo te informando.\n"
            dispatcher.utter_message(default)
