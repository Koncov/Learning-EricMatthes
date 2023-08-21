# class Car:
#     """Простая модель автомобиля"""
#
#     def __init__(self, make, model, year):
#         """Инициализирует атрибуты автомобиля"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """Возвращает аккуратно отформатированное описание"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#     def read_odometer(self):
#         """Выводит пробег машины"""
#         print(f"This car has {self.odometer_reading} miles on it")
#
#     def update_odometer(self, mileage):
#         """Устанавливает заданное показание на одометре.
#             При попытке обратной подкрутки изменение отклоняется."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("Бро, харе сматывать счетчик")
#
#     def increment_odometer(self, miles):
#         """Увеличивает показания одометра с приращением."""
#         self.odometer_reading += miles


from car import Car


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


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты характерные для электромобилей"""
        super().__init__(make, model, year)
        self.battery = Battery()


# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
