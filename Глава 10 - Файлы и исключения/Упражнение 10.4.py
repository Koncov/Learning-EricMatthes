filename = 'guest_book.txt'

name_input = "yes"
while name_input == "yes":
    with open(filename, 'a') as file_object:
        file_object.write(input("Здравствуйте, введите ваше имя: "))
        file_object.write("\n")
    name_input = input("Продолжить ввод пользователей yes\\no: ")
else:
    print("The end!!!")
