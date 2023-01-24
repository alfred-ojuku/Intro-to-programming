import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function code'"""

    def test_first_last_name(self):
        """Do names like 'Alfred Ojuku' work?"""
        formatted_name = get_formatted_name('alfred', 'ojuku')
        self.assertEqual(formatted_name, 'Alfred Ojuku')

    def test_first_middle_last_name(self):
        """Do names like 'Alfred Ojuku Okinyi' work?"""
        formatted_name = get_formatted_name('alfred', 'okinyi', 'ojuku')
        self.assertEqual(formatted_name, 'Alfred Ojuku Okinyi')

if __name__ == '__main__':
    unittest.main()