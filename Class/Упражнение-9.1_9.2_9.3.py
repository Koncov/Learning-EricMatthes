# Упражнение 9.1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name restaurant is {self.restaurant_name}.")
        print(f"In the restaurant {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open.")


restaurant = Restaurant('Saransk', 'strict')

print(f"Вывод атрибута restaurant_name - {restaurant.restaurant_name}.")
print(f"Вывод атрибута cuisine_type - {restaurant.cuisine_type}. \n")

restaurant.describe_restaurant()
restaurant.open_restaurant()

# Упражнение 9.2
print()
restaurant_1 = Restaurant('Moskva', 'Best')
restaurant_2 = Restaurant('Sant.Petesburg', 'Best')
restaurant_3 = Restaurant('Krasnodar', 'Lite')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

# Упражнение 9.3
print()

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


user_1 = User('Концов', 'Евгений', 46, 'Novokubansk')
user_2 = User('Концова', 'Елена', 40, 'Novokubansk')
user_3 = User('Концова', 'Лилиана', 16, 'Novokubansk')

user_1.describe_user()
user_1.greet_user()
print()
user_2.describe_user()
user_2.greet_user()
print()
user_3.describe_user()
user_3.greet_user()
print()
