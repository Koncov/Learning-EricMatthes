from user912 import User

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
