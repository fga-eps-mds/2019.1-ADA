from rasa_core_sdk import Action

class ActionDoReport(Action):
    def name(self):
        return "action_do_report"

    def run(self, dispatcher, tracker, domain):
        # verificar se o repo está cadastrado
        default = "Desculpa, mas o seu repositório ainda não foi cadastrado.\
                   Me peça ajuda para que o façamos!"
        not_registered = False
        if(not_registered):
            utter.dispatcher(default)

        # se o repo esta cadastrado, buscar as info via ada-gitlab
        
        # com as info, montar o relatorio e gerar o arquivo
