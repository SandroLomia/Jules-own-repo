import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        password = generate_password()
        self.assertEqual(len(password), 12)

    def test_custom_length(self):
        password = generate_password(length=16)
        self.assertEqual(len(password), 16)

    def test_inclusion_of_all_types(self):
        password = generate_password(length=20)
        self.assertTrue(any(c in string.ascii_lowercase for c in password), "Missing lowercase letter")
        self.assertTrue(any(c in string.ascii_uppercase for c in password), "Missing uppercase letter")
        self.assertTrue(any(c in string.digits for c in password), "Missing digit")
        self.assertTrue(any(c in string.punctuation for c in password), "Missing special character")

    def test_only_lowercase(self):
        password = generate_password(use_uppercase=False, use_digits=False, use_special=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in password), "Password contains non-lowercase characters")

    def test_only_uppercase_and_digits(self):
        password = generate_password(use_lowercase=False, use_special=False)
        self.assertTrue(all(c in (string.ascii_uppercase + string.digits) for c in password), "Password contains unexpected characters")
        self.assertTrue(any(c in string.ascii_uppercase for c in password), "Missing uppercase letter")
        self.assertTrue(any(c in string.digits for c in password), "Missing digit")

    def test_invalid_length_too_short(self):
        # All 4 sets enabled, but length is 3 (less than 4)
        with self.assertRaises(ValueError):
            generate_password(length=3)

    def test_no_character_sets_selected(self):
        with self.assertRaises(ValueError):
            generate_password(use_lowercase=False, use_uppercase=False, use_digits=False, use_special=False)

if __name__ == '__main__':
    unittest.main()
