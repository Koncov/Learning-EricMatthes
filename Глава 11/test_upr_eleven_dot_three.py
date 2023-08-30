import unittest
from upr_eleven_dot_three import Employee


class TestEmployee(unittest.TestCase):
    """Тесты для класса Employee"""

    def setUp(self) -> None:
        """Создаем экземпляр класса с заданными атрибутами."""
        self.user = Employee('Evgen', 'Nekto', 6000)

    def test_give_default_raise(self):
        """Проверяем метод с данными оклада по умолчанию"""
        user = self.user.give_raise()
        self.assertEqual(user, 'Evgen Nekto с окладом на конец года 11000 с прибавкой равной 5000.')

    def test_give_custom_raise(self):
        """Проверяем метод с измененными данными оклада."""
        user = self.user.give_raise(1000)
        self.assertEqual(user, 'Evgen Nekto с окладом на конец года 7000 с прибавкой равной 1000.')


if __name__ == '__main__':
    unittest.main()
