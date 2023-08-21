# Упражнение 9.4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_server = 0

    def describe_restaurant(self):
        print(f"Name restaurant is {self.restaurant_name}.")
        print(f"In the restaurant {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open.")

    def set_number_served(self, user_server):
        self.number_server = user_server

    def increment_number_served(self, user_server):
        self.number_server += user_server


restaurant = Restaurant('Saransk', 'strict')

print(f"Вывод атрибута restaurant_name - {restaurant.restaurant_name}.")
print(f"Вывод атрибута cuisine_type - {restaurant.cuisine_type}. \n")

restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"Количество обслуженных посетителей {restaurant.number_server}.")
restaurant.set_number_served(5)
print(f"Количество обслуженных посетителей {restaurant.number_server}.")
restaurant.increment_number_served(34)
print(f"Количество обслуженных посетителей {restaurant.number_server}.")

# Упражнение 9.5
class User:

    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print(f"Информация о пользователе:\nФамилия - {self.first_name}. \nИмя - {self.last_name}. \n"
              f"Возраст - {self.age}.\nМесто жительства - {self.country}. ")

    def greet_user(self):
        print(f"Мы приветствуем Вас - {self.last_name} {self.first_name}!!!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_3 = User('Концова', 'Лилиана', 16, 'Novokubansk')

print(user_3.login_attempts)
user_3.increment_login_attempts()
print(user_3.login_attempts)
user_3.increment_login_attempts()
print(user_3.login_attempts)
user_3.increment_login_attempts()
print(user_3.login_attempts)
user_3.increment_login_attempts()
print(user_3.login_attempts)
user_3.reset_login_attempts()
print(user_3.login_attempts)
