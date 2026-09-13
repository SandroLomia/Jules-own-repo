import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        password = generate_password()
        self.assertEqual(len(password), 16)

    def test_custom_length(self):
        password = generate_password(length=24)
        self.assertEqual(len(password), 24)

    def test_exclude_uppercase(self):
        password = generate_password(length=20, use_uppercase=False)
        self.assertFalse(any(char in string.ascii_uppercase for char in password))

        # Verify it still has other types
        self.assertTrue(any(char in string.ascii_lowercase for char in password))
        self.assertTrue(any(char in string.digits for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_all_character_types_present(self):
        # We test this by generating a password and ensuring at least one of each required character is present
        # Since it guarantees at least one of each type if selected
        password = generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True)

        self.assertTrue(any(char in string.ascii_lowercase for char in password))
        self.assertTrue(any(char in string.ascii_uppercase for char in password))
        self.assertTrue(any(char in string.digits for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_minimum_length_error(self):
        with self.assertRaises(ValueError):
            # If all are True, minimum length is 4. Passing 3 should fail.
            generate_password(length=3, use_uppercase=True, use_numbers=True, use_special=True)

if __name__ == '__main__':
    unittest.main()
