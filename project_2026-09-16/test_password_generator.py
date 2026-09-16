import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_valid_password_length(self):
        # Test default length
        pwd = generate_password()
        self.assertEqual(len(pwd), 12)

        # Test specific length
        pwd = generate_password(length=20)
        self.assertEqual(len(pwd), 20)

    def test_all_character_types_included(self):
        pwd = generate_password(length=100, use_upper=True, use_lower=True, use_numbers=True, use_special=True)

        has_upper = any(c in string.ascii_uppercase for c in pwd)
        has_lower = any(c in string.ascii_lowercase for c in pwd)
        has_digit = any(c in string.digits for c in pwd)
        has_special = any(c in string.punctuation for c in pwd)

        self.assertTrue(has_upper, "Password should contain at least one uppercase letter.")
        self.assertTrue(has_lower, "Password should contain at least one lowercase letter.")
        self.assertTrue(has_digit, "Password should contain at least one number.")
        self.assertTrue(has_special, "Password should contain at least one special character.")

    def test_invalid_length_edge_case(self):
        # Test zero or negative length
        with self.assertRaises(ValueError):
            generate_password(length=0)

        with self.assertRaises(ValueError):
            generate_password(length=-5)

        # Test length shorter than the number of selected types
        with self.assertRaises(ValueError):
            generate_password(length=3, use_upper=True, use_lower=True, use_numbers=True, use_special=True)

    def test_no_types_selected(self):
        with self.assertRaises(ValueError):
            generate_password(use_upper=False, use_lower=False, use_numbers=False, use_special=False)

if __name__ == '__main__':
    unittest.main()
