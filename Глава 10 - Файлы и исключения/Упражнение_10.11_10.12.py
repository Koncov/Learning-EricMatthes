import json


def read_like_user_number():
    """Читает любимое число, если оно записано в файл."""

    filename = 'user_number.json'
    try:
        with open(filename) as f:
            like_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return like_number


def write_like_user_number():
    """Записывает любимое число, если оно не существует."""

    filename = 'user_number.json'
    like_number = int(input("Введите любимое Ваше любимое число: "))
    with open(filename, 'w') as f:
        json.dump(like_number, f)
    return like_number


def print_like_user_number():
    """Выводит на экран любимое число."""

    like_number = read_like_user_number()
    if like_number:
        print(f"Я знаю ваше любимое число. Это - {like_number}")
    else:
        like_number = write_like_user_number()
        print(f"Ваше число - {like_number} сохранено.")


print_like_user_number()
