# from car import Car, ElectricCar
#
# my_beetle = Car('volkswagen', 'beetle', 2009)
# print(my_beetle.get_descriptive_name())
#
# my_roadster = ElectricCar('tesla', 'roadster', 2019)
# print(my_roadster.get_descriptive_name())

from car import Car
from electric_car import ElectricCar as EC

my_beetle = Car('volkswagen', 'beetle', 2009)
print(my_beetle.get_descriptive_name())

my_roadster = EC('tesla', 'roadster', 2019)
print(my_roadster.get_descriptive_name())
