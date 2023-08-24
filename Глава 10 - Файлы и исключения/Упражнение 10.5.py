filename = 'programming_opros.txt'

otvet = True
while otvet:
    with open(filename, 'w') as file_object:
        file_object.write(input("Почему Вам нравится программировать? "))
    otvet = input("Продолжить опрос? yes\\no: ")
    if otvet == "yes":
        otvet = True
    elif otvet == "no":
        otvet = False
    else:
        print("Не правильный параметр, введите yes или no: ")
        break
