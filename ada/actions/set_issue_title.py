from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from urllib3.exceptions import NewConnectionError


class ActionIssueName(Action):
    def name(self):
        return "action_issue_name"

    def run(self, dispatcher, tracker, domain):
        slot_repo = tracker.get_slot("repository_github")
        if slot_repo:
            try:
                message = tracker.latest_message.get('text')
                message = message.split(": ")
                issue_name = message[1]

                print("O titulo da Issue é: {issue_name}\n".format(
                     issue_name=issue_name))
            except ValueError:
                dispatcher.utter_message(
                 "Estou com problemas para me conectar agora, me mande "
                 "novamente uma mensagem mais tarde.")
            except NewConnectionError:
                dispatcher.utter_message(
                 "Estou com problemas para me conectar agora, me mande "
                 "novamente uma mensagem mais tarde.")

            else:
                return [SlotSet('issue_name', issue_name)]
        else:
            dispatcher.utter_message("Para criar uma issue"
                                     " é necessário que você tenha um "
                                     "repositório do github cadastrado!")
            dispatcher.utter_message("Quando quiser cadastrar é só avisar!")
            return []
