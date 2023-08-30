class Employee:
    """Класс представляющий работника."""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.result_annual_salary = 0

    def give_raise(self, default_annual_salary=5000):
        """Увеличивает оклад на 5000 по умолчанию, либо с вводимым значением."""
        if default_annual_salary == 5000:
            self.result_annual_salary = self.annual_salary + default_annual_salary
            user_info = f"{self.first_name} {self.last_name} с окладом на конец года {self.result_annual_salary} с " \
                        f"прибавкой равной {default_annual_salary}."
        else:
            self.result_annual_salary = self.annual_salary + default_annual_salary
            user_info = f"{self.first_name} {self.last_name} с окладом на конец года {self.result_annual_salary} с " \
                        f"прибавкой равной {default_annual_salary}."
        return user_info


# user = Employee('Evgen', 'Nekto', 6000)
# print(user.give_raise(1000))
