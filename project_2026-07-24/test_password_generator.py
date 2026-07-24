import unittest
import string
from password_generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = PasswordGenerator()

    def test_default_generation(self):
        password = self.generator.generate()
        self.assertEqual(len(password), 12)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_custom_length(self):
        password = self.generator.generate(length=20)
        self.assertEqual(len(password), 20)

    def test_only_uppercase(self):
        password = self.generator.generate(length=10, use_lower=False, use_digits=False, use_symbols=False)
        self.assertEqual(len(password), 10)
        self.assertTrue(all(c in string.ascii_uppercase for c in password))

    def test_only_digits(self):
        password = self.generator.generate(length=15, use_upper=False, use_lower=False, use_symbols=False)
        self.assertEqual(len(password), 15)
        self.assertTrue(all(c in string.digits for c in password))

    def test_no_character_types(self):
        with self.assertRaisesRegex(ValueError, "At least one character type must be selected."):
            self.generator.generate(use_upper=False, use_lower=False, use_digits=False, use_symbols=False)

    def test_length_too_short_for_constraints(self):
        with self.assertRaisesRegex(ValueError, "is too short to satisfy the selected constraints."):
            self.generator.generate(length=2) # 4 constraints are enabled by default, so length 2 is too short

if __name__ == '__main__':
    unittest.main()
