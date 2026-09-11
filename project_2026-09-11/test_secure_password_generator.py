import unittest
import string
from secure_password_generator import generate_password

class TestSecurePasswordGenerator(unittest.TestCase):

    def test_generate_password_length(self):
        """Test that the password is the correct length."""
        for length in [4, 8, 16, 32]:
            password = generate_password(length=length)
            self.assertEqual(len(password), length)

    def test_generate_password_uppercase_inclusion(self):
        """Test that uppercase characters are included when specified."""
        password = generate_password(length=20, use_uppercase=True, use_numbers=False, use_special_chars=False)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))

        # Test they are excluded when specified False
        password = generate_password(length=20, use_uppercase=False, use_numbers=False, use_special_chars=False)
        self.assertFalse(any(c in string.ascii_uppercase for c in password))

    def test_generate_password_number_inclusion(self):
        """Test that number characters are included when specified."""
        password = generate_password(length=20, use_uppercase=False, use_numbers=True, use_special_chars=False)
        self.assertTrue(any(c in string.digits for c in password))

        # Test they are excluded when specified False
        password = generate_password(length=20, use_uppercase=False, use_numbers=False, use_special_chars=False)
        self.assertFalse(any(c in string.digits for c in password))

    def test_generate_password_special_chars_inclusion(self):
        """Test that special characters are included when specified."""
        password = generate_password(length=20, use_uppercase=False, use_numbers=False, use_special_chars=True)
        self.assertTrue(any(c in string.punctuation for c in password))

        # Test they are excluded when specified False
        password = generate_password(length=20, use_uppercase=False, use_numbers=False, use_special_chars=False)
        self.assertFalse(any(c in string.punctuation for c in password))

    def test_generate_password_variation(self):
        """Test that calling the function multiple times yields different passwords."""
        passwords = [generate_password(length=16) for _ in range(100)]
        # All passwords should be unique
        self.assertEqual(len(set(passwords)), len(passwords))

    def test_generate_password_too_short(self):
        """Test that ValueError is raised if length is too short for constraints."""
        with self.assertRaises(ValueError):
             # Min length should be 4 here
             generate_password(length=3, use_uppercase=True, use_numbers=True, use_special_chars=True)

if __name__ == '__main__':
    unittest.main()
