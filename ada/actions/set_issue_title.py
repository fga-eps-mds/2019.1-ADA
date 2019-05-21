from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import sys
import telegram

class ActionIssueName(Action):
    def name(self):
        return "action_issue_name"

    def run(self, dispatcher, tracker, domain):
        try:
            message = tracker.latest_message.get('text')
            message = message.split(": ")
            issue_name = message[1]
            print("O titulo da Issue é: {issue_name}\n"
                  .format(issue_name=issue_name))
        except ValueError:
            dispatcher.utter_message("Desculpe, mas não consegui criar a Issue!")
        else:
            return [SlotSet('issue_name', issue_name)]
