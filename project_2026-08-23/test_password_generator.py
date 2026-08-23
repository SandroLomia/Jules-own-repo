import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_length(self):
        for length in [1, 8, 16, 128]:
            password = generate_password(length, True, True, True, True)
            self.assertEqual(len(password), length)

    def test_all_character_types(self):
        password = generate_password(16, True, True, True, True)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_only_lowercase(self):
        password = generate_password(8, False, True, False, False)
        self.assertEqual(len(password), 8)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_only_uppercase(self):
        password = generate_password(8, True, False, False, False)
        self.assertEqual(len(password), 8)
        self.assertTrue(all(c in string.ascii_uppercase for c in password))

    def test_only_numbers(self):
        password = generate_password(8, False, False, True, False)
        self.assertEqual(len(password), 8)
        self.assertTrue(all(c in string.digits for c in password))

    def test_only_special(self):
        password = generate_password(8, False, False, False, True)
        self.assertEqual(len(password), 8)
        self.assertTrue(all(c in string.punctuation for c in password))

    def test_short_length_with_many_types(self):
        password = generate_password(2, True, True, True, True)
        self.assertEqual(len(password), 2)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(0, True, True, True, True)
        with self.assertRaises(ValueError):
            generate_password(-1, True, True, True, True)

    def test_no_character_types(self):
        with self.assertRaises(ValueError):
            generate_password(8, False, False, False, False)

if __name__ == "__main__":
    unittest.main()
