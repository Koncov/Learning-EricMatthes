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
