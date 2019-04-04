from yping import List

from data.Repository import Repository
from data.Telegram import Telegram
from data.User import User


def create_account(name: str, username: str, is_bot: str) -> User:
    user = User()
    user.name = name
    user.username = username
    user.is_bot = is_bot

    return user


def create_telegram(username: str, token: str) -> Telegram:
    telegram = Telegram
    telegram.username = username

    return telegram


def create_repository(repo_url: str, repo_name: str, repo_description: str) -> Repository:
    repository = Repository
    repository.repo_url = repo_url
    repository.repo_name = repo_name
    repository.repo_description = repo_description

    return repository
