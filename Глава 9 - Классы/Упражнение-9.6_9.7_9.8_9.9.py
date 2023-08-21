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


class Car:
    """Простая модель автомобиля"""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """Устанавливает заданное показание на одометре.
            При попытке обратной подкрутки изменение отклоняется."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Бро, харе сматывать счетчик")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с приращением."""
        self.odometer_reading += miles


class Battery:
    """Простая модель аккумуляторной батареи."""

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print(f"This car has a {self.battery_size} - kwh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car cam go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Меняет размер аккумуляторной батареи."""
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты характерные для электромобилей"""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
