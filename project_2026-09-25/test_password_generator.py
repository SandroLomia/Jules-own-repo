import unittest
import string
from password_generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):

    def test_default_generation(self):
        pwd = PasswordGenerator.generate()
        self.assertEqual(len(pwd), 12)
        self.assertTrue(any(c in string.ascii_uppercase for c in pwd))
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))
        self.assertTrue(any(c in string.digits for c in pwd))
        self.assertTrue(any(c in string.punctuation for c in pwd))

    def test_custom_length(self):
        pwd_short = PasswordGenerator.generate(length=8)
        self.assertEqual(len(pwd_short), 8)

        pwd_long = PasswordGenerator.generate(length=16)
        self.assertEqual(len(pwd_long), 16)

    def test_exclude_uppercase(self):
        pwd = PasswordGenerator.generate(use_uppercase=False)
        self.assertFalse(any(c in string.ascii_uppercase for c in pwd))

    def test_exclude_lowercase(self):
        pwd = PasswordGenerator.generate(use_lowercase=False)
        self.assertFalse(any(c in string.ascii_lowercase for c in pwd))

    def test_exclude_digits(self):
        pwd = PasswordGenerator.generate(use_digits=False)
        self.assertFalse(any(c in string.digits for c in pwd))

    def test_exclude_special(self):
        pwd = PasswordGenerator.generate(use_special=False)
        self.assertFalse(any(c in string.punctuation for c in pwd))

    def test_single_character_class(self):
        pwd = PasswordGenerator.generate(length=10, use_uppercase=False, use_lowercase=True, use_digits=False, use_special=False)
        self.assertEqual(len(pwd), 10)
        self.assertTrue(all(c in string.ascii_lowercase for c in pwd))

    def test_no_classes_selected_raises_error(self):
        with self.assertRaises(ValueError):
            PasswordGenerator.generate(use_uppercase=False, use_lowercase=False, use_digits=False, use_special=False)

    def test_length_too_short_raises_error(self):
        with self.assertRaises(ValueError):
            # 4 classes enabled, so min length must be 4
            PasswordGenerator.generate(length=3)

if __name__ == '__main__':
    unittest.main()
