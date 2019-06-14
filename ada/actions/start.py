from rasa_core_sdk import Action
import os
import telegram

GITLAB_SIGNUP_URL = os.environ.get("GITLAB_SIGNUP_URL", "")
GITHUB_SIGNUP_URL = os.environ.get("GITHUB_SIGNUP_URL", "")
CLIENT_ID_GITHUB = os.environ.get("CLIENT_ID_GITHUB", "")
CLIENT_ID_GITLAB = os.environ.get("CLIENT_ID_GITLAB", "")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")


class ActionStart(Action):
    def name(self):
        return "action_start"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker_state = tracker.current_state()
            sender_id = tracker_state['sender_id']
            github_signup_url = GITHUB_SIGNUP_URL + str(sender_id)
            gitlab_signup_url = GITLAB_SIGNUP_URL

            bot = telegram.Bot(token=ACCESS_TOKEN)

            url = "https://github.com/login/oauth/authorize?"\
                  "client_id={client_id}"\
                  "&redirect_uri={url}&scope"\
                  "=admin%3Arepo_hook%2Crepo".format(
                   url=github_signup_url, client_id=CLIENT_ID_GITHUB)

            url_2 = "https://gitlab.com/oauth/authorize?"\
                    "client_id={client_id}&redirect_uri="\
                    "{url}&response_type=code&state={chat_id}".format(
                     url=gitlab_signup_url, chat_id=sender_id,
                     client_id=CLIENT_ID_GITLAB)

            message_github = "Olá, sou a Ada! Sou responsável "\
                             "por ajudar você no monitoramento de "\
                             "produção com seus repositórios. "\
                             "Caso queira saber mais, me peça ajuda. "\
                             "Agora, pra gente começar, caso você "\
                             "queira que eu monitore seu repositório "\
                             "do GitHub, clique [aqui]({url}) "\
                             "para cadastrá-lo".format(url=url)

            bot.send_message(chat_id=sender_id,
                             text=message_github, parse_mode=telegram.
                             ParseMode.MARKDOWN,
                             disable_web_page_preview=False)

            message_gitlab = "Caso você queira que eu monitore seu repositó"\
                             "rio do GitLab, clique [aqui]({url}) para "\
                             "cadastrá-lo".format(
                              url=url_2)

            bot.send_message(chat_id=sender_id,
                             text=message_gitlab,
                             parse_mode=telegram.ParseMode.MARKDOWN,
                             disable_web_page_preview=False)

        except ValueError:
            dispatcher.utter_message("Não consegui me conectar, vamos tentar "
                                     "novamente, ok?")
