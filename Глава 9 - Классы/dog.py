class Dog:
    """Простая модель собаки"""

    def __init__(self, name, age):
        """Инициализирует атрибуты name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде"""
        print(f"{self.name} is now sitting.")

    def roll_cover(self):
        """Собака перекатывается по команде"""
        print(f"{self.name} rolled over.")


my_dog = Dog('Willie', 6)
your_dog = Dog('Licy', 3)
# my_dog.roll_cover()

print(f"My dog\'s name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()

print(f"My dog\'s name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old")
your_dog.sit()
