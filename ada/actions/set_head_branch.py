from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from urllib3.exceptions import NewConnectionError
import telegram
import os
import requests

GITHUB_SERVICE_URL = os.getenv("GITHUB_SERVICE_URL", "")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "")


class ActionHeadBranch(Action):
    def name(self):
        return "action_head_branch"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker_state = tracker.current_state()
            chat_id = tracker_state["sender_id"]
            message = tracker.latest_message.get('text')
            message = message.split(": ")
            head_branch = message[1]

            print("Head branch: {head_branch}\n".format
                  (head_branch=head_branch))
            headers = {"Content-Type": "application/json"}
            bot = telegram.Bot(token=ACCESS_TOKEN)

            branches_names = self.select_branches_by_buttons(chat_id,
                                                             headers,
                                                             head_branch)
            reply_markup = telegram.InlineKeyboardMarkup(branches_names)

            bot.send_message(chat_id=chat_id,
                             text="Escolha uma branch para fazer o pull "
                                  "request!",
                             reply_markup=reply_markup)
            return [SlotSet('head_branch', head_branch)]
        except ValueError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")

    def select_branches_by_buttons(self, chat_id, headers, selected_branch):

        url = GITHUB_SERVICE_URL + "branches/names/{chat_id}".format(
                                    chat_id=chat_id)
        response = requests.get(url=url, headers=headers)
        received_branches = response.json()
        buttons = []
        for i in range(len(received_branches["branches"])):
            if received_branches["branches"][i]["name"] == selected_branch:
                del received_branches["branches"][i]
                break
        for branches in received_branches["branches"]:
            for value in branches:
                buttons.append(telegram.InlineKeyboardButton(
                    text=branches["name"],
                    callback_data="Base: " + branches["name"]))
        branches_names = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
        return branches_names
