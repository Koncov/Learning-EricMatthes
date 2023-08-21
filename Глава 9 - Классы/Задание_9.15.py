from random import choices

lottery_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'Y']
my_ticket = choices(lottery_list, k=4)
lottery = []
count_step = 0
while lottery != my_ticket:
    lottery = choices(lottery_list, k=4)
    count_step += 1
print(f"Количество попыток для выигрыша - {count_step}")


"""Вариант совпадения стремится к 0"""
# my_ticket = []
# while lottery != my_ticket:
#     for i in range(4):
#         my_ticket += str(choice(lottery))
#     count_step += 1
#     print(f"Выигрышный билет с номером - {my_ticket} --- шаг ---{count_step}")
#     my_ticket = []
# else:
#     count_step += 1
#
# print(f"Количество попыток для выигрыша - {count_step}")

"""Вариант совпадения стремится к 0"""
# lottery = []
# my_ticket = ['8', 'C', '7', '9']
# count_step = 0
# while lottery != my_ticket:
#     for i in range(4):
#         lottery += str(choice(lottery_list))
#     count_step += 1
#     print(f"Выигрышный билет с номером - {lottery} --- шаг ---{count_step}")
#     lottery = []
# else:
#     count_step += 1
#
# print(f"Количество попыток для выигрыша - {count_step}")
