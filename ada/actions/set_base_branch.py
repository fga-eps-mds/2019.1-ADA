from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from urllib3.exceptions import NewConnectionError


class ActionBaseBranch(Action):
    def name(self):
        return "action_base_branch"

    def run(self, dispatcher, tracker, domain):
        try:
            message = tracker.latest_message.get('text')
            message = message.split(": ")
            base_branch = message[1]

            print("Base branch: {base_branch}\n".format
                  (base_branch=base_branch))
        except ValueError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")

        else:
            return [SlotSet('base_branch', base_branch)]