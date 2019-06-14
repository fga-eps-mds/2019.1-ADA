from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import os
import requests
import json
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import sys

GITHUB_SERVICE_URL = os.getenv("GITHUB_SERVICE_URL", "")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "")


class ActionCommentIssue(Action):
    def name(self):
        return "action_comment_issue"

    def run(self, dispatcher, tracker, domain):
        try:
            headers = {'Content-Type': 'application/json'}
            tracker_state = tracker.current_state()
            chat_id = tracker_state["sender_id"]

            message = tracker.latest_message.get('text')

            delete_webhook_url = "https://api.telegram.org/bot" + \
                                 ACCESS_TOKEN + "/deleteWebhook"
            print("Delete url: ", delete_webhook_url, "\n\n", file=sys.stderr)
            get_updates_url = "https://api.telegram.org/bot" + ACCESS_TOKEN + \
                              "/getUpdates"
            print("Updates url: ", get_updates_url, "\n\n", file=sys.stderr)
            peguei_issue_number = False
            try:  # delete webhook
                delete_response = requests.get(url=delete_webhook_url)
                delete_response.raise_for_status()
            except HTTPError:
                dispatcher.utter_message("Delete webhook falhou")
            else:

                try:  # get updates
                    get_updates_response = requests.get(url=get_updates_url)
                    get_updates_response.raise_for_status()
                    get_updates_response = get_updates_response.json()
                    reply_to_message = get_updates_response["result"][-1][
                                       "message"]["reply_to_message"]
                except HTTPError:
                    print("Get updates falhou", file=sys.stderr)
                except KeyError:
                    print("Reply to message ERROR -> não existe",
                          file=sys.stderr)
                else:
                    reply_text = reply_to_message["text"]
                    print("Reply text: ", reply_text, "\n\n", file=sys.stderr)
                    issue_number = reply_text.split("#")
                    issue_number = issue_number[1][0]
                    print("issue number: ", issue_number, "\n\n",
                          file=sys.stderr)
                    peguei_issue_number = True

            splited_message = message.split(": ")
            comment_body = splited_message[-1]

            if(not peguei_issue_number):
                print("Nao peguei issue number pela api do telegram",
                      file=sys.stderr)
                splited_message = splited_message[0].split('#')
                issue_number = splited_message[-1]

            data = {"body": comment_body, "issue_number": issue_number}
            url = GITHUB_SERVICE_URL + "api/comment_issue/{chat_id}".format(
                  chat_id=chat_id)
            response = requests.post(url=url, data=json.dumps(data),
                                     headers=headers)
            response.raise_for_status()
        except HTTPError:
            dispatcher.utter_message(
                "Não consegui comentar a issue, tente novamente")
        except ValueError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        else:
            return [SlotSet('issue_number', issue_number)]
