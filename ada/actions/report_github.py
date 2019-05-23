from rasa_core_sdk import Action
import requests
import os
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import telegram
import sys

GITHUB_SERVICE_URL = os.getenv("GITHUB_SERVICE_URL", "")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")
SECS = 10.0


class ReportGitHub(Action):
    def name(self):
        return "action_get_report_github"

    def run(self, dispatcher, tracker, domain):
        try:
            headers = {'Content-Type': 'application/json'}
            tracker_state = tracker.current_state()
            chat_id = tracker_state["sender_id"]

            try:
                response_branches = requests.get(GITHUB_SERVICE_URL +
                                                 "branches/names/"
                                                 "{chat_id}".format(
                                                  chat_id=chat_id),
                                                 timeout=SECS, headers=headers)
                response_branches_date = requests.get(GITHUB_SERVICE_URL +
                                                      "branches/datecommits/"
                                                      "{chat_id}".format(
                                                       chat_id=chat_id),
                                                      timeout=SECS,
                                                      headers=headers)
                response_pull_request = requests.get(GITHUB_SERVICE_URL +
                                                     "pullrequest/{chat_id}"
                                                     .format(chat_id=chat_id),
                                                     timeout=SECS,
                                                     headers=headers)
                response_releases = requests.get(GITHUB_SERVICE_URL +
                                                 "release/{chat_id}"
                                                 .format(chat_id=chat_id),
                                                 timeout=SECS, headers=headers)
            except requests.exceptions.Timeout:
                text = "Desculpa, não consegui fazer o que você me pediu! 😕"
                bot = telegram.Bot(token=ACCESS_TOKEN)
                bot = bot.send_message(chat_id=chat_id, text=text)
            else:
                branches = response_branches.json()
                branches_date = response_branches_date.json()
                pull_request = response_pull_request.json()
                release = response_releases.json()

                size_branches = "Você possui um total "\
                                "de {size} "\
                                "branches!".format(
                                            size=len(branches["branches"]))
                branches_names = "As branches são as seguintes:\n"

                for item in branches["branches"]:
                    for value in item:
                        branches_names += "➡️ {branches}\n".format(
                                          branches=item["name"])
                dispatcher.utter_message(size_branches)
                dispatcher.utter_message(branches_names)

                branches_date_text = "Os últimos commit's foram "\
                                     "feitos nas branches e nas "\
                                     "datas abaixo:\n"
                for item in branches_date["branches"]:
                    date_json = item["date"]
                    date = date_json[:10]
                    print(date, file=sys.stderr)
                    branches_date_text += "{branch_name} ➡️ {date}\n".format(
                                          branch_name=item["name"], date=date)
                dispatcher.utter_message(branches_date_text)

                pull_request_text = "🛠 Pull requests:\n"
                for item in pull_request["pull_request"]:
                    pull_request_text += "➡️ Título: {title},"\
                                         "URL: {url}\n".format(
                                                       title=item["title"],
                                                       url=item["url"])
                dispatcher.utter_message(pull_request_text)

                date_release_json = release["release"][0]["created_at"]
                date_release = date_release_json[:10]

                release_text = "🛠 Última release:\n"\
                               "Nome: {name}\n"\
                               "Body: {body}\n"\
                               "Criada dia: {date}\n"\
                               "URL: {url}".format(
                                name=release["release"][0]["name"],
                                body=release["release"][0]["body"],
                                date=date_release, url=release
                                ["release"][0]["url"])
                dispatcher.utter_message(release_text)
        except HTTPError:
            dispatcher.utter_message(
                "Não estou conseguindo ter acesso a seus dados, tem certeza"
                "que seus dados estão certos?")
        except ValueError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar, me manda "
                "mais uma mensagem pra ver se dessa vez dá certo.")
