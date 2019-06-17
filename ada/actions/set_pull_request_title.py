from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from urllib3.exceptions import NewConnectionError
import os
import requests
import telegram

GITHUB_SERVICE_URL = os.getenv("GITHUB_SERVICE_URL", "")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "")


class ActionPullRequestTitle(Action):
    def name(self):
        return "action_pull_request_title"

    def run(self, dispatcher, tracker, domain):
        slot_repo = tracker.get_slot("repository_github")
        if slot_repo:
            try:
                tracker_state = tracker.current_state()
                chat_id = tracker_state["sender_id"]
                message = tracker.latest_message.get('text')
                message = message.split(": ")
                pull_request_title = message[-1]

                headers = {"Content-Type": "application/json"}
                bot = telegram.Bot(token=ACCESS_TOKEN)

                branches_names = self.select_branches_by_buttons(chat_id,
                                                                 headers)
                reply_markup = telegram.InlineKeyboardMarkup(branches_names)

                bot.send_message(chat_id=chat_id,
                                 text="Encontrei essas branches!",
                                 reply_markup=reply_markup)
            except ValueError:
                dispatcher.utter_message(
                    "Estou com problemas para me conectar, me manda "
                    "mais uma mensagem pra ver se dessa vez dá certo.")
            except NewConnectionError:
                dispatcher.utter_message(
                    "Estou com problemas para me conectar, me manda "
                    "mais uma mensagem pra ver se dessa vez dá certo.")
            except KeyError:
                dispatcher.utter_message(
                    "Não consegui me conectar, talvez você não esteja "
                    "com nenhum repositório cadastrado, vamos tentar mais "
                    "tarde"
                )
            else:
                return [SlotSet('pull_request_title', pull_request_title)]
        else:
            dispatcher.utter_message("Para que você crie um Pull Request"
                                     " é necessário que você"
                                     " tenha um repositório cadastrado!")
            return []

    def select_branches_by_buttons(self, chat_id, headers):
        url = GITHUB_SERVICE_URL + "branches/names/{chat_id}".format(
                                    chat_id=chat_id)
        response = requests.get(url=url, headers=headers)

        received_branches = response.json()
        buttons = []

        for branches in received_branches["branches"]:
            for value in branches:
                buttons.append(telegram.InlineKeyboardButton(
                    text=branches["name"],
                    callback_data="head: " +
                                  branches["name"]))
        branches_names = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
        return branches_names
