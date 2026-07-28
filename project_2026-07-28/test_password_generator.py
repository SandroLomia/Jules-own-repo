import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_generation(self):
        password = generate_password()
        self.assertEqual(len(password), 12)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_custom_length(self):
        password = generate_password(length=20)
        self.assertEqual(len(password), 20)

    def test_no_uppercase(self):
        password = generate_password(use_uppercase=False)
        self.assertFalse(any(c in string.ascii_uppercase for c in password))

    def test_no_lowercase(self):
        password = generate_password(use_lowercase=False)
        self.assertFalse(any(c in string.ascii_lowercase for c in password))

    def test_no_digits(self):
        password = generate_password(use_digits=False)
        self.assertFalse(any(c in string.digits for c in password))

    def test_no_symbols(self):
        password = generate_password(use_symbols=False)
        self.assertFalse(any(c in string.punctuation for c in password))

    def test_only_uppercase(self):
        password = generate_password(
            use_lowercase=False,
            use_digits=False,
            use_symbols=False
        )
        self.assertTrue(all(c in string.ascii_uppercase for c in password))

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)
        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_length_too_short_for_requirements(self):
        with self.assertRaises(ValueError):
            generate_password(length=3, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True)

    def test_no_types_selected(self):
        with self.assertRaises(ValueError):
            generate_password(
                use_uppercase=False,
                use_lowercase=False,
                use_digits=False,
                use_symbols=False
            )

if __name__ == '__main__':
    unittest.main()
