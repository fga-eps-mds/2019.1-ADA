import mongoengine
from data.User import User


class Telegram(mongoengine.Document):
    username = mongoengine.StringField()
    token = mongoengine.StringField()

    user_id = mongoengine.ListField()

    def getNotifications(self):
        pass

    def sendNotifications(self):
        pass

# testing
#chat1 = Telegram()
#chat1.username = "chatopsMDS"
#chat1.save()  # salva no banco de dados
#>>>>>>> cf05758d169666c0b051eee444b7511df2506d6b
