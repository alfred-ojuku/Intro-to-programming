import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the employee class"""

    def setUp(self):
        """Creates new employee instance"""
        self.employee1 = Employee('alfred', 'ojuku', 200000)

    def test_give_default_raise(self):
        """Tests if the default amount of raise is correct"""
        self.default_raise = self.employee1.give_raise()
        self.assertEqual(self.default_raise, 205000)

    def test_give_custom_raise(self):
        """Tests for the custom raise"""
        self.custom_raise = self.employee1.give_raise(10000)
        self.assertEqual(self.custom_raise, 210000)

if __name__ == '__main__':
    unittest.main()


