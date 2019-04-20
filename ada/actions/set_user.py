from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests


class ActionSetUser(Action):
    def name(self):
        return "action_set_user"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker_state = tracker.current_state()
            sender_id = tracker_state['sender_id']
            message = tracker.latest_message.get('text')
            message = message.split()
            username = message[len(message)-1]
            dispatcher.utter_message(
                "Seu nome de usuário é: {user}.".format(user=username))
            dispatcher.utter_message(
                "Agora me fala o nome do seu repositório, mas não se esqueça que de escrever repositório: na frente")
            return [SlotSet('usuario', username)]
        except ValueError:
            dispatcher.utter_message(ValueError)
