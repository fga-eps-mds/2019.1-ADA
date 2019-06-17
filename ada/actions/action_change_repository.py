from rasa_core_sdk import Action
import os
import telegram
from telegram import Bot
import sys

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")


class ChangeRepo(Action):
    def name(self):
        return "action_change_repository"

    def run(self, dispatcher, tracker, domain):
        bot = Bot(token=ACCESS_TOKEN)
        buttons = []
        tracker_state = tracker.current_state()
        chat_id = tracker_state["sender_id"]
        git_service = ["Github", "Gitlab"]
        for name in git_service:
            print("###"*30 + "\n" + name + "###"*30 + "\n", file=sys.stderr)
            buttons.append(telegram.InlineKeyboardButton(
                text=name,
                callback_data="muda meu repositório do " + name))
        service_name = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
        reply_markup = telegram.InlineKeyboardMarkup(service_name)
        bot.send_message(chat_id=chat_id,
                         text="Em qual serviço você" +
                         " deseja recadastrar o repositório?",
                         reply_markup=reply_markup)
