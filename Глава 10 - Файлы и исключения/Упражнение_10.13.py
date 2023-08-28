import json
# Программа загружает имя пользователя, если оно существует.
# В противном случае она запрашивает имя пользователя и сохраняет его.


def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""

    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username(username_verification=None):
    """Запрашивает новое имя пользователя."""

    filename = 'username.json'
    if username_verification:
        username = username_verification
        with open(filename, 'w') as f:
            json.dump(username, f)
        return username
    else:
        username = input(f"What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
        return username


def greet_user():
    """Приветствуем пользователя по имени."""

    username = get_stored_username()
    if username:
        username_verification = input("What is your name? ")
        if username_verification == username:
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(username_verification)
            print(f"We`ll remember you when com back, {username}.")


greet_user()
