import unittest
import string
from password_generator import SecurePasswordGenerator

class TestSecurePasswordGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = SecurePasswordGenerator()

    def test_default_generation(self):
        password = self.generator.generate()
        self.assertEqual(len(password), 16)
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_custom_length(self):
        password = self.generator.generate(length=24)
        self.assertEqual(len(password), 24)

    def test_only_lowercase(self):
        password = self.generator.generate(use_upper=False, use_digits=False, use_symbols=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_only_digits(self):
        password = self.generator.generate(use_lower=False, use_upper=False, use_symbols=False)
        self.assertTrue(all(c in string.digits for c in password))

    def test_no_symbols(self):
        password = self.generator.generate(use_symbols=False)
        self.assertFalse(any(c in string.punctuation for c in password))

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            self.generator.generate(length=0)
        with self.assertRaises(ValueError):
            self.generator.generate(length=-5)

    def test_length_too_short_for_requirements(self):
        # Requires 4 chars (one of each), asking for length 3
        with self.assertRaises(ValueError):
            self.generator.generate(length=3)

    def test_no_character_types(self):
        with self.assertRaises(ValueError):
            self.generator.generate(use_lower=False, use_upper=False, use_digits=False, use_symbols=False)

if __name__ == '__main__':
    unittest.main()
