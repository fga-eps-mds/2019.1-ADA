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
    meta = {'collection': 'users'}
    
    name = db.StringField()
    username = db.StringField()
    telegramID = db.StringField()
    is_bot = db.BooleanField()
    #language_code = mongoengine.StringField()

    # def __init__(self):
    #    """Construtor User"""
    # nao e necessaerio ter metodo __init__(https://stackoverflow.com/questions/38363726/mongoengine-attributeerror)
    def get_user(self):
        """ Retorna o trio nome, user e telegramID"""
        return  self.name, self.last_name, self.username, self.telegramID, self.is_bot
    def new_user(self, name, last_name, username, telegramID, is_bot):
        """Cria um novo usuario e o salva no banco de dados Telegram_User_DataBase"""
        self.name = name
        self.last_name = last_name
        self.username = username
        self.telegramID = telegramID
        self.is_bot = is_bot
        self.save() # acho que isso aqui que realmente salva o usuario no database

    def find_user_by_username(self, username):
        user = self
        user = self.objects(username=username)
        return user

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
        'message': 'user added!'
    })

@app.route("/api/find/user/<username>", methods=["GET"])
def find_user_by_username(username):
    User.objects.get_or_404(username=username)
    return jsonify({
        "status": "success",
        "message": "user finded"
    })
    #search = User()
    #search = search.find_user_by_username(username)
    #if user:
    #    return jsonify({
    #    "status": "success",
    #    "message": "user finded"
    #})
    #return jsonify({
    #    "status": "failed",
    #    "message": "user not found"
    #})

#@app.route('/api/getuser', methods=['GET'])
#def get_user():
#    user = User()
#    user = user.find_user_by_username("erickdev")
#    first_name, last_name, username, telegramID, is_bot = user.getUser()
#    return jsonify({
#        'name': first_name,
#        'last_name': last_name,
#        'username': username,
#        'telegramID': telegramID,
#        'is_bot': is_bot
#    })
