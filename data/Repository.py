import mongoengine


mongoengine.register_connection(alias='core', name='Telegram_User_DataBase')


class Repo(mongoengine.Document):
    repo_url = mongoengine.StringField()
    repo_name = mongoengine.StringField()
    repo_description = mongoengine.StringField()

    user_id = mongoengine.ListField()
    telegram_id = mongoengine.ListField()

    def getRepo(self):
        """ Retorna o nome, url e descricao do repositório"""
        return (self.repo_name, self.repo_url, self.repo_description)

    def newRepo(repo_url, repo_name, repo_description):
        """Cria um novo repositório"""
        self.repo_url = repo.url
        self.repo_name = last_name
        self.repo_description = repo_description
        # self.save() # acho que isso aqui que realmente salva o usuario no database

    meta = {
        'db_alias': 'core',
        'collection': 'repository'
    }
