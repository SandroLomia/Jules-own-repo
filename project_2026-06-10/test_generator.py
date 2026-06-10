import unittest
import string
from generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_default_generation(self):
        # Default should have length 12
        pwd = generate_password()
        self.assertEqual(len(pwd), 12)

    def test_length(self):
        for i in range(1, 20):
            pwd = generate_password(length=i)
            self.assertEqual(len(pwd), i)

    def test_no_upper(self):
        pwd = generate_password(length=20, use_upper=False)
        for char in pwd:
            self.assertNotIn(char, string.ascii_uppercase)

    def test_no_numbers(self):
        pwd = generate_password(length=20, use_numbers=False)
        for char in pwd:
            self.assertNotIn(char, string.digits)

    def test_no_special(self):
        pwd = generate_password(length=20, use_special=False)
        for char in pwd:
            self.assertNotIn(char, string.punctuation)

    def test_only_lowercase(self):
        pwd = generate_password(length=20, use_upper=False, use_numbers=False, use_special=False)
        for char in pwd:
            self.assertIn(char, string.ascii_lowercase)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)

        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_minimum_constraints_met(self):
        # If length is enough, it should have at least one of each requested type
        pwd = generate_password(length=10, use_upper=True, use_numbers=True, use_special=True)

        has_upper = any(c in string.ascii_uppercase for c in pwd)
        has_lower = any(c in string.ascii_lowercase for c in pwd)
        has_number = any(c in string.digits for c in pwd)
        has_special = any(c in string.punctuation for c in pwd)

        self.assertTrue(has_upper)
        self.assertTrue(has_lower)
        self.assertTrue(has_number)
        self.assertTrue(has_special)

if __name__ == '__main__':
    unittest.main()
