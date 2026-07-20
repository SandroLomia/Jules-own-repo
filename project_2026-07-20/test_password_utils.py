import unittest
import string
from password_utils import generate_password, analyze_strength

class TestPasswordUtils(unittest.TestCase):
    def test_generate_password_length(self):
        password = generate_password(length=20, upper=True, lower=True, numbers=True, symbols=True)
        self.assertEqual(len(password), 20)

    def test_generate_password_min_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=3, upper=True, lower=True, numbers=True, symbols=True)

    def test_generate_password_no_char_sets(self):
        with self.assertRaises(ValueError):
            generate_password(length=10, upper=False, lower=False, numbers=False, symbols=False)

    def test_generate_password_only_upper(self):
        password = generate_password(length=10, upper=True, lower=False, numbers=False, symbols=False)
        for char in password:
            self.assertIn(char, string.ascii_uppercase)

    def test_generate_password_only_numbers(self):
        password = generate_password(length=10, upper=False, lower=False, numbers=True, symbols=False)
        for char in password:
            self.assertIn(char, string.digits)

    def test_analyze_strength_weak(self):
        self.assertEqual(analyze_strength("abc"), "Weak")
        self.assertEqual(analyze_strength("abcdefg"), "Weak")

    def test_analyze_strength_medium(self):
        self.assertEqual(analyze_strength("Abcdefg1"), "Medium")
        self.assertEqual(analyze_strength("password123"), "Medium")

    def test_analyze_strength_strong(self):
        self.assertEqual(analyze_strength("StrongPassw0rd!"), "Strong")
        self.assertEqual(analyze_strength("aB1!eF2@iJ3#"), "Strong")

if __name__ == "__main__":
    unittest.main()
