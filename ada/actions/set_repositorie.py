from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError


class ActionSetRepositorie(Action):
    def name(self):
        return "action_set_repositorie"

    def run(self, dispatcher, tracker, domain):
        try:
            message = tracker.latest_message.get('text')
            message_splitted = message.split()
            repository = message_splitted[len(message_splitted)-1]
            dispatcher.utter_message(
                "Ok, vou ficar monitorando o repositório {rep}.".format(rep=repository))
            return [SlotSet('repositorio', repository)]
        except HTTPError:
            dispatcher.utter_message(
                "Não consegui encontrar seu repositório, por favor verifique o nome que enviou e tente novamente.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou tendo problemas para me conectar com o gitlab.")
        except ValueError:
            dispatcher.utter_message(
                "Estou tendo alguns problemas, tente mais tarde.")
        except Exception:
            dispatcher.utter_message(
                "Estou tendo alguns problemas, tente mais tarde.")
