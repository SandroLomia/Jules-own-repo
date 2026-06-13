import unittest
import string
from password_generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):

    def test_default_generation(self):
        generator = PasswordGenerator()
        password = generator.generate(20)
        self.assertEqual(len(password), 20)
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_length(self):
        generator = PasswordGenerator()
        for length in [1, 10, 50, 100]:
            password = generator.generate(length)
            self.assertEqual(len(password), length)

    def test_zero_or_negative_length(self):
        generator = PasswordGenerator()
        with self.assertRaises(ValueError):
            generator.generate(0)
        with self.assertRaises(ValueError):
            generator.generate(-5)

    def test_no_character_types(self):
        generator = PasswordGenerator(use_lower=False, use_upper=False, use_digits=False, use_special=False)
        with self.assertRaises(ValueError):
            generator.generate()

    def test_only_lowercase(self):
        generator = PasswordGenerator(use_upper=False, use_digits=False, use_special=False)
        password = generator.generate(50)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_only_uppercase(self):
        generator = PasswordGenerator(use_lower=False, use_digits=False, use_special=False)
        password = generator.generate(50)
        self.assertTrue(all(c in string.ascii_uppercase for c in password))

    def test_only_digits(self):
        generator = PasswordGenerator(use_lower=False, use_upper=False, use_special=False)
        password = generator.generate(50)
        self.assertTrue(all(c in string.digits for c in password))

    def test_only_special(self):
        generator = PasswordGenerator(use_lower=False, use_upper=False, use_digits=False)
        password = generator.generate(50)
        self.assertTrue(all(c in string.punctuation for c in password))

if __name__ == '__main__':
    unittest.main()
