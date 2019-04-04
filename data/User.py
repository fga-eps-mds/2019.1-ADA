import mongoengine

#mongoengine.register_connection(alias='core', name='Telegram_User_DataBase')
# , alias="telegramUDB", host="MacBook-Pro-de-Erick.local:27017", port=27017)
mongoengine.connect(db="Telegram_User_DataBase")
# ATENCAO:
# erro na linha 4 caso descomente: you have not defined a default connection


class User(mongoengine.Document):
    name = mongoengine.StringField()
    username = mongoengine.StringField()
    telegramID = mongoengine.ListField()
    is_bot = mongoengine.BooleanField()
    #language_code = mongoengine.StringField()

    # def __init__(self):
    #    """Construtor User"""
    # nao e necessaerio ter metodo __init__(https://stackoverflow.com/questions/38363726/mongoengine-attributeerror)
