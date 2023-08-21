# Упражнение 8.9
def show_message(text_message):
    for message in text_message:
        print(message)


list_message = [
    'Я ведь лучше собаки!? Погуляй со мной... ',
    'Увидеть тебя - зрелище не для слабонервных.',
    'Доехала нормально, целую. Твоя крыша.',
    'Извини сегодня прийти не смогу. Приду завтра. Похмелье.',
    'Не говори, что мне нужно делать, и я не скажу, куда тебе нужно идти.',
]

show_message(list_message)
print("END 8.9\n")

# Упражнение 8.10

def send_message(text_message):
    while text_message:
        message = text_message.pop()
        print(message)
        list_message_end.append(message)

    print(f"List list_message_start 8.10 {list_message_start}")
    print(f"List list_message_end 8.10 {list_message_end}")


list_message_start = [
    'Я ведь лучше собаки!? Погуляй со мной... ',
    'Увидеть тебя - зрелище не для слабонервных.',
    'Доехала нормально, целую. Твоя крыша.',
    'Извини сегодня прийти не смогу. Приду завтра. Похмелье.',
    'Не говори, что мне нужно делать, и я не скажу, куда тебе нужно идти.',
]
list_message_end = []

send_message(list_message_start)
print("END 8.10\n")

# Упражнение 8.11

def send_message_i(text_message):
    while text_message:
        message = text_message.pop()
        print(message)
        list_message_end_i.append(message)

    print(f"List list_message_start_i 8.11 {list_message_start_i}")
    print(f"List list_message_end_i 8.11 {list_message_end_i}")


list_message_start_i = [
    'Я ведь лучше собаки!? Погуляй со мной... ',
    'Увидеть тебя - зрелище не для слабонервных.',
    'Доехала нормально, целую. Твоя крыша.',
    'Извини сегодня прийти не смогу. Приду завтра. Похмелье.',
    'Не говори, что мне нужно делать, и я не скажу, куда тебе нужно идти.',
]
list_message_end_i = []

send_message_i(list_message_start_i[:])
print("END 8.11")
