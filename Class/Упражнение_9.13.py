from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        result = randint(1, self.sides)
        # print(f"Результат броска кубика - {result}.")
        return result


kubik_6 = Die()
for i in range(10):
    print(f"Бросок №{i + 1}, результат - {kubik_6.roll_die()}")

kubik_10 = Die(10)
print(f"Бросок кубика с 10 гранями - {kubik_10.roll_die()}")

kubik_20 = Die(20)
print(f"Бросок кубика с 20 гранями - {kubik_20.roll_die()}")
