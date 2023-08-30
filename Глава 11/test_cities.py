import unittest
from upr_eleven_dot_one import locations


class LocationsTest(unittest.TestCase):
    """Тесты для upr_eleven_dot_one.py."""

    def test_country_city(self):
        """Проверяет вывод страны и города вида 'Россия, Воронеж'"""
        formatted_location = locations('Россия', 'Воронеж')
        self.assertEqual(formatted_location, 'Россия, Воронеж')

    def test_country_city_population(self):
        """Проверяет вывод страны и города вида 'Россия, Воронеж - population = 500000'"""
        formatted_location = locations('Россия', 'Воронеж', 500000)
        self.assertEqual(formatted_location, 'Россия, Воронеж - population = 500000')


if __name__ == '__main__':
    unittest.main()
