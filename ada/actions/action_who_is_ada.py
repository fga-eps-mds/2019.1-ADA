from rasa_core_sdk import Action


class WhoIsAda(Action):
    def name(self):
        return "action_who_is_ada"

    def run(self, dispatcher, tracker, domain):
        message = {
          "text": "Eu fui desenvolvida por um grupo de estudantes de \
                   Engenharia de Software da Universidade de Brasília, \
                   em 2019.",
          "text2": "Meu nome e personalidade foram escolhidos em  homenagem à \
                    Ada Lovelace, uma grande escritora e matemática do século \
                    XIX, filha do poeta Lord Byron. A ela é atribuído o  \
                    título de primeira mulher programadora, uma vez que ela \
                    foi responsável por criar o priemiro algoritmo coma  \
                    intenção de ser executado por uma máquina de computação, \
                    além de ter reconhecido o enorme potencial desse tipo de \
                    máquina.",
          "text3": "Você pode entender mais sobre minha personalidade por \
                    meio desse link: https://www.celebrities-galore.com/\
                    celebrities/ada-lovelace/home/" + "\n" +
                   "E por aqui você encontra mais sobre minha história e  \
                    sobre meus trabalhos: https://pt.wikipedia.org/wiki/\
                    Ada_Lovelace"
          }

        dispatcher.utter_message(message['text'])
        dispatcher.utter_message(message["text2"])
        dispatcher.utter_message(message["text3"])
