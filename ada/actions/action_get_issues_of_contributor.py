from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import os
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import telegram

GITHUB_SERVICE_URL = os.environ.get("GITHUB_SERVICE_URL", "")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")


class ActionGetContributorIssues(Action):
    def name(self):
        return "action_get_issues_of_contributor"

    def run(self, dispatcher, tracker, domain):
        headers = {'Content-Type': 'application/json'}
        tracker_state = tracker.current_state()
        chat_id = tracker_state["sender_id"]
        if self.check_user(chat_id, headers):
            try:

                message = tracker.latest_message.get('text')
                message = message.split(" ")
                name_by_msg = message[-1]
                name_by_msg = name_by_msg.split("?")
                name_by_msg = name_by_msg[0]
                response = requests.get(GITHUB_SERVICE_URL +
                                        "api/get_contributor_issues/"
                                        "{chat_id}"
                                        "/{contributor_name}"
                                        .format(chat_id=chat_id,
                                                contributor_name=name_by_msg),
                                        headers=headers)
                received_issues = response.json()
                bot = telegram.Bot(token=ACCESS_TOKEN)

                bot_message = "Essas são as issues do @{name},"\
                              " Se você clicar na issue você consegue"\
                              " ver mais informações lá no GitHub!".format(
                                                        name=name_by_msg)

                bot.send_message(chat_id=chat_id, text=bot_message,
                                 parse_mode='Markdown',
                                 disable_wen_page_preview=True)
                for received2 in received_issues:
                    message = "📌 [#{issue_number} {issue_title}]({issue_url})"\
                        .format(issue_number=str(received2["issue_number"]),
                                issue_title=received2["title"],
                                issue_url=received2["url"])
                    bot.send_message(chat_id=chat_id, text=message,
                                     parse_mode='Markdown',
                                     disable_web_page_preview=True)

            except HTTPError:
                dispatcher.utter_message(
                    "Não consegui encontrar as issues, tente novamente")
            except NewConnectionError:
                dispatcher.utter_message(
                 "Estou com problemas para encontrar seus dados agora,"
                 "me mande novamente uma mensagem mais tarde.")
            except ValueError:
                dispatcher.utter_message(
                 "Estou com problemas para encontrar seus dados, me mande "
                 "novamente uma mensagem mais tarde.")
            else:
                return [SlotSet('contributor_name', name_by_msg)]
        else:
            dispatcher.utter_message("Para ter acesso as issues"
                                     " é necessário que você tenha um "
                                     "repositório do github cadastrado!")
            dispatcher.utter_message("Quando quiser cadastrar é só avisar!")
            return []

    def check_user(self, chat_id, headers):
        url = GITHUB_SERVICE_URL + "user/infos/{chat_id}".\
            format(chat_id=chat_id)
        response = requests.get(url, headers=headers)
        data = response.json()
        if data["username"] and data["repository"]:
            return True
        return False
