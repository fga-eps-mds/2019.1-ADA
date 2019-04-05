# services/users/project/__init__.py


import os
from flask import Flask, jsonify, request
# from flask_mongoengine import MongoEngine
from flask_mongoengine import MongoEngine
import sys



# instantiate the app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


# instantiate the db
db = MongoEngine()  # new
db.init_app(app)

class User(db.Document):
    name = db.StringField()
    username = db.StringField()
    telegramID = db.StringField()
    is_bot = db.BooleanField()
    #language_code = mongoengine.StringField()

    # def __init__(self):
    #    """Construtor User"""
    # nao e necessaerio ter metodo __init__(https://stackoverflow.com/questions/38363726/mongoengine-attributeerror)
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


@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


@app.route('/api/register/user', methods=['POST'])
def add_user():
    post_data = request.get_json()
    user = User(name=post_data['name'],
                username=post_data['username'], telegramID=post_data['telegramID'],
                is_bot=post_data['is_bot'])
    user.save()
    return jsonify({
        'status': 'success',
        'message': 'added user!'
    })
