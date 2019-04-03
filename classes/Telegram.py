import mongoengine
import User

class Telegram(mongoengine.Document):
    username = mongoengine.StringField()
    token = mongoengine.StringField()

    users = list() #lista de usuarios ?

    def getNotifications():
        pass

    def sendNotifications():
        pass

#testing
#chat1 = Telegram()
#chat1.username = "chatopsMDS"
#chat1.save() #salva no banco de dados
