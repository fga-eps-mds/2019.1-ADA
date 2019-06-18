from rasa_core_sdk import Action
import requests
import os
from urllib3.exceptions import NewConnectionError
from requests.exceptions import HTTPError
import telegram


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
                                "branches!✅".format(
                                            size=len(branches["branches"]))
                branches_names = "As branches são as seguintes:\n"

                for item in branches["branches"]:
                    for value in item:
                        branches_names += "➡️ {branches}\n".format(
                                          branches=item["name"])
                dispatcher.utter_message(size_branches)
                dispatcher.utter_message(branches_names)

                branches_date_text = "E essa é a quantidade de dias "\
                                     "desde que foram feitos commit's "\
                                     "nelas:\n"
                for item in branches_date["branches"]:
                    branches_date_text += "⏱{branch_name}: {date}"\
                                          " dia(s).\n".format(
                                           branch_name=item["name"],
                                           date=item["last_commit_days"])
                dispatcher.utter_message(branches_date_text)

                if not pull_request["pull_request"]:
                    dispatcher.utter_message(
                        "📌Não existe nenhum Pull Request aberto "
                        "no seu repositório.")
                else:
                    pull_request_len = len(pull_request["pull_request"])
                    if(pull_request_len > 5):
                        pull_request["pull_request"] = (
                            pull_request["pull_request"][:5])
                    pull_request_size = len(pull_request["pull_request"])
                    pull_request_text = "🛠 Pull requests:\n"
                    pull_request_text += "Existem {pull_request_size} pull's "\
                                         "requests abertos no seu repositório"\
                                         ".\n".format(
                                          pull_request_size=pull_request_len)
                    pull_request_text += "Estes são os últimos "\
                                         "{pull_request_size} pull request's:"\
                                         "\n".format(
                                          pull_request_size=pull_request_size)

                    for item in pull_request["pull_request"]:
                        pull_request_text += "📌 Título: {title}\n"\
                                            "📌URL: {url}\n".format(
                                                        title=item["title"],
                                                        url=item["url"])
                    dispatcher.utter_message(pull_request_text)

                if not release["release"]:
                    dispatcher.utter_message(
                        "Não existe nenhuma Release criada"
                        " no seu repositório.❗")
                else:
                    date_release_json = release["release"][0]["created_at"]
                    date_release = date_release_json[:10]
                    day = date_release[8:10]
                    month = date_release[5:7]
                    year = date_release[0:4]
                    release_text = "🛠 Última release:\n"\
                                   "📌Nome: {name}\n"\
                                   "📌Descrição: {body}\n"\
                                   "📌Criada dia: {day}/{month}/{year}\n"\
                                   "📌URL: {url}".format(
                                        name=release["release"][0]["name"],
                                        body=release["release"][0]["body"],
                                        day=day, month=month, year=year,
                                        url=release["release"][0]["url"])
                    dispatcher.utter_message(release_text)
        except HTTPError:
            dispatcher.utter_message(
                "Não estou conseguindo ter acesso a seus dados, tem certeza"
                "que seus dados estão certos?")
        except ValueError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar agora, me mande "
                "novamente uma mensagem mais tarde.")
        except NewConnectionError:
            dispatcher.utter_message(
                "Estou com problemas para me conectar agora, me mande "
                "novamente uma mensagem mais tarde.")
