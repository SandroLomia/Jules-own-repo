import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_length(self):
        for length in [1, 5, 10, 50, 100]:
            password = generate_password(length)
            self.assertEqual(len(password), length)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(0)
        with self.assertRaises(ValueError):
            generate_password(-5)

    def test_with_symbols(self):
        # We test with a reasonably large length to ensure high probability
        # of containing a symbol, though the algorithm guarantees it for length >= 4
        password = generate_password(20, use_symbols=True)
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_without_symbols(self):
        password = generate_password(50, use_symbols=False)
        self.assertFalse(any(char in string.punctuation for char in password))

    def test_required_character_classes_with_symbols(self):
        password = generate_password(10, use_symbols=True)
        self.assertTrue(any(char in string.ascii_lowercase for char in password))
        self.assertTrue(any(char in string.ascii_uppercase for char in password))
        self.assertTrue(any(char in string.digits for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_required_character_classes_without_symbols(self):
        password = generate_password(10, use_symbols=False)
        self.assertTrue(any(char in string.ascii_lowercase for char in password))
        self.assertTrue(any(char in string.ascii_uppercase for char in password))
        self.assertTrue(any(char in string.digits for char in password))
        self.assertFalse(any(char in string.punctuation for char in password))

    def test_short_passwords(self):
        # Should not raise exception, just return a password of correct length
        self.assertEqual(len(generate_password(1)), 1)
        self.assertEqual(len(generate_password(2)), 2)
        self.assertEqual(len(generate_password(3, use_symbols=True)), 3)

if __name__ == '__main__':
    unittest.main()
