from rasa_core_sdk import Action
import os
GITHUB_SIGNUP_URL = os.environ.get("GITHUB_SIGNUP_URL", "")
CLIENT_ID_GITHUB = os.environ.get("CLIENT_ID_GITHUB", "")
CLIENT_ID_GITLAB = os.environ.get("CLIENT_ID_GITLAB", "")


class ActionStart(Action):
    def name(self):
        return "action_start"

    def run(self, dispatcher, tracker, domain):
        try:
            tracker_state = tracker.current_state()
            sender_id = tracker_state['sender_id']
            github_signup_url = GITHUB_SIGNUP_URL + str(sender_id)

            url = "https://github.com/login/oauth/authorize?"\
                  "client_id={client_id}"\
                  "&redirect_uri={url}&scope"\
                  "=admin%3Arepo_hook%2Crepo".format(
                   url=github_signup_url, client_id=CLIENT_ID_GITHUB)

            url_2 = "https://gitlab.com/oauth/authorize?"\
                    "client_id={client_id}&redirect_uri="\
                    "http://localhost:5000/user/gitlab/authorize"\
                    "&response_type=code&state={chat_id}".format(
                     chat_id=sender_id, client_id=CLIENT_ID_GITLAB)

            message_github = "Oláaaaa, sou a Ada! Sou responsável "\
                             "por ajudar você no monitoramento de "\
                             "produção com seus repositórios. "\
                             "Caso queira saber mais, me peça ajuda. "\
                             "Agora, pra gente começar, caso você "\
                             "queira que eu monitore seu repositório "\
                             "do GitHub, vou pedir para você "\
                             "clicar nesse link aqui, {link_github}.".format(
                              link_github=url)

            message_gitlab = "Caso você queira que eu monitore seu repositó"\
                             "rio do GitLab, clica nesse link aqui,"\
                             "{link_gitlab}".format(link_gitlab=url_2)

            dispatcher.utter_message(message_github)
            dispatcher.utter_message(message_gitlab)

        except ValueError:
            dispatcher.utter_message("Não consegui me conectar, vamos tentar "
                                     "novamente, ok?")
