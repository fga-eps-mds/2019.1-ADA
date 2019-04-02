import mongoengine

mongoengine.register_connection(alias='core', name='Telegram_User_DataBase')


class User(mongoengine.Document):
    name = mongoengine.StringField()
    user = mongoengine.StringField()
    telegramID = mongoengine.StringField()

    #def __init__(self):
    #    """Construtor User"""
    #nao e necessaerio ter metodo __init__(https://stackoverflow.com/questions/38363726/mongoengine-attributeerror)

    def getUser(self):
        """ Retorna o trio nome, user e telegramID"""
        return  self.name, self.user, self.telegramID
    def newUser(self, name, user, telegramID):
        """Cria um novo usuario"""
        self.name = name
        self.user = user
        self.telegramID = telegramID
        #self.save() # acho que isso aqui que realmente salva o usuario no database

# testing ...
user1 = User()
user1.newUser("erick", "eu", "1234")
#user1.name = input("qual o seu nome ? ")
print(user1.name) # eu queria converter isso pra string normal
print(type(user1))

print(user1.getUser())
