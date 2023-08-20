from random import choice

lottery_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'Y']

lottery = str()
for i in range(4):
    lottery += str(choice(lottery_list))

print(f"Выигрышный билет с номером - {lottery}")
