import unittest
import string
from password_generator import SecurePasswordGenerator

class TestSecurePasswordGenerator(unittest.TestCase):

    def test_default_generation(self):
        generator = SecurePasswordGenerator()
        password = generator.generate()
        self.assertEqual(len(password), 16)

        # Test guaranteed characters
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_custom_length(self):
        generator = SecurePasswordGenerator()
        password = generator.generate(length=24)
        self.assertEqual(len(password), 24)

    def test_only_lowercase(self):
        generator = SecurePasswordGenerator(include_uppercase=False, include_digits=False, include_symbols=False)
        password = generator.generate(length=10)
        self.assertEqual(len(password), 10)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_no_types_selected_raises_error(self):
        with self.assertRaises(ValueError):
            SecurePasswordGenerator(include_uppercase=False, include_lowercase=False, include_digits=False, include_symbols=False)

    def test_length_too_short_raises_error(self):
        generator = SecurePasswordGenerator()
        # Default generator requires at least 4 chars (one of each type)
        with self.assertRaises(ValueError):
            generator.generate(length=3)

    def test_custom_symbols(self):
        custom_symbols = "!@#"
        generator = SecurePasswordGenerator(include_lowercase=False, include_uppercase=False, include_digits=False, custom_symbols=custom_symbols)
        password = generator.generate(length=10)
        self.assertTrue(all(c in custom_symbols for c in password))

if __name__ == '__main__':
    unittest.main()
