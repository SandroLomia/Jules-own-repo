import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password_length(self):
        # Test if the returned string length matches the requested length
        length = 16
        password = generate_password(length)
        self.assertEqual(len(password), length)

    def test_generate_password_character_types(self):
        # Test if the generated password contains uppercase, lowercase, digits, and special characters when all are enabled
        password = generate_password(20, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_generate_password_invalid_config(self):
        # Test if ValueError is raised when all boolean flags are False
        with self.assertRaises(ValueError):
            generate_password(10, use_uppercase=False, use_lowercase=False, use_digits=False, use_special=False)

        # Test if ValueError is raised when length is less than 1
        with self.assertRaises(ValueError):
            generate_password(0)

        # Test if ValueError is raised when length is smaller than number of active constraints
        with self.assertRaises(ValueError):
            generate_password(3, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True)

if __name__ == '__main__':
    unittest.main()
