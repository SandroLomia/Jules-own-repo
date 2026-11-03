import unittest
import string
from secure_password_generator import generate_password

class TestSecurePasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        password = generate_password()
        self.assertEqual(len(password), 12)

    def test_custom_length(self):
        password = generate_password(length=20)
        self.assertEqual(len(password), 20)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)
        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_no_character_sets_selected(self):
        with self.assertRaises(ValueError):
            generate_password(
                use_lowercase=False,
                use_uppercase=False,
                use_digits=False,
                use_special=False
            )

    def test_only_lowercase(self):
        password = generate_password(
            length=100,
            use_uppercase=False,
            use_digits=False,
            use_special=False
        )
        for char in password:
            self.assertIn(char, string.ascii_lowercase)

    def test_randomness(self):
        # Generates two passwords and ensures they are not identical
        # The chance of identical passwords for 12 chars is extremely low.
        pw1 = generate_password()
        pw2 = generate_password()
        self.assertNotEqual(pw1, pw2)

if __name__ == '__main__':
    unittest.main()
