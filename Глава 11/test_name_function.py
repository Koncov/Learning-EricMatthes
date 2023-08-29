import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'."""

    def test_first_last_name(self):
        """Имена вида 'Jon Jonson' работают правильно."""
        formatted_name = get_formatted_name('jon', 'jonson')
        self.assertEqual(formatted_name, 'Jon Jonson')

    def test_first_last_middle_name(self):
        """Имена вида 'Jon Jonson Patrick' работают правильно."""
        formatted_name = get_formatted_name('jon', 'patrick', 'jonson')
        self.assertEqual(formatted_name, 'Jon Jonson Patrick')


if __name__ == '__main__':
    unittest.main()
