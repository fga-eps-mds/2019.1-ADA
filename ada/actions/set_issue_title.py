from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from urllib3.exceptions import NewConnectionError


class ActionIssueName(Action):
    def name(self):
        return "action_issue_name"

    def run(self, dispatcher, tracker, domain):
        try:
            message = tracker.latest_message.get('text')
            message = message.split(": ")
            issue_name = message[1]

            print("O titulo da Issue é: {issue_name}\n".format
                  (issue_name=issue_name))
        except ValueError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")

        else:
            return [SlotSet('issue_name', issue_name)]
