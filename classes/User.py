import mongoengine

#mongoengine.register_connection(alias='core', name='Telegram_User_DataBase')
#mongoengine.connect(db="Telegram_User_DataBase")#, alias="telegramUDB", host="MacBook-Pro-de-Erick.local:27017", port=27017)
#ATENCAO:
#erro na linha 4 caso descomente: you have not defined a default connection

class User(mongoengine.Document):
    name = mongoengine.StringField()
    last_name = mongoengine.StringField()
    username = mongoengine.StringField()
    telegramID = mongoengine.StringField()
    is_bot = mongoengine.BooleanField()
    #language_code = mongoengine.StringField()

    #def __init__(self):
    #    """Construtor User"""
    #nao e necessaerio ter metodo __init__(https://stackoverflow.com/questions/38363726/mongoengine-attributeerror)

    def getUser(self):
        """ Retorna o trio nome, user e telegramID"""
        return  self.name, self.last_name, self.username, self.telegramID, self.is_bot
    def newUser(self, name, last_name, username, telegramID, is_bot):
        """Cria um novo usuario e o salva no banco de dados Telegram_User_DataBase"""
        self.name = name
        self.last_name = last_name
        self.username = username
        self.telegramID = telegramID
        self.is_bot = is_bot
        self.save() # acho que isso aqui que realmente salva o usuario no database

# testing ...
#user1 = User()
#user1.newUser("erick", "giff", "egf", "1234", False)
##user1.name = input("qual o seu nome ? ")
#print(user1.name) # eu queria converter isso pra string normal
#print(type(user1))
#
#print(user1.getUser())
