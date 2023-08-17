# Упражнение 9.6
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name restaurant is {self.restaurant_name}.")
        print(f"In the restaurant {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open.")


class IceCremStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['plonbir', 'eskimo', 'shokolad']

    def ics(self):
        print(f"Ice Crem Stand {self.flavors}")


restaurant = IceCremStand('Saransk', 'strict')

restaurant.ics()

# Упражнение 9.7
print()
print("Упражнение 9.7")

class User:

    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe_user(self):
        print(f"Информация о пользователе:\nФамилия - {self.first_name}. \nИмя - {self.last_name}. \n"
              f"Возраст - {self.age}.\nМесто жительства - {self.country}. ")

    def greet_user(self):
        print(f"Мы приветствуем Вас - {self.last_name} {self.first_name}!!!")

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
        self.privileges = [
            'Разрешено добавлять пользователя',
            'Разрешено удалять пользователя',
            'Разрешено банить пользователя',
        ]

    def show_privileges(self):
        print(f"Список привилегий 2 - {self.privileges}")

class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges(self)


user_1 = Admin('Концов', 'Евгений', 46, 'Novokubansk')
user_1.privileges.show_privileges()

# Упражнение 9.8
print()
print("Упражнение 9.8")

user_2 = Admin('Концов', 'Евгений', 46, 'Novokubansk')
user_2.privileges.show_privileges()

# Упражнение 9.9
print()
print("Упражнение 9.9")
