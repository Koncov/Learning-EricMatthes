print("Введите два числа для сложения. Для выхода наберите q")
while True:
    a = input("Введите первое число: ")
    if a == 'q':
        break
    b = input("Введите второе число: ")
    if b == 'q':
        break
    try:
        result = int(a) + int(b)
    except ValueError:
        print("Вы ввели не число, повторите ввод.")
    else:
        print(result)


