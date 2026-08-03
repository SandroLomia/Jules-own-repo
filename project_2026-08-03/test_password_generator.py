import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        pwd = generate_password()
        self.assertEqual(len(pwd), 12)

    def test_custom_length(self):
        pwd = generate_password(length=20)
        self.assertEqual(len(pwd), 20)

    def test_includes_upper(self):
        pwd = generate_password(length=10, use_upper=True, use_lower=False, use_digits=False, use_symbols=False)
        self.assertTrue(all(c in string.ascii_uppercase for c in pwd))
        self.assertTrue(any(c in string.ascii_uppercase for c in pwd))

    def test_includes_lower(self):
        pwd = generate_password(length=10, use_upper=False, use_lower=True, use_digits=False, use_symbols=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in pwd))
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))

    def test_includes_digits(self):
        pwd = generate_password(length=10, use_upper=False, use_lower=False, use_digits=True, use_symbols=False)
        self.assertTrue(all(c in string.digits for c in pwd))
        self.assertTrue(any(c in string.digits for c in pwd))

    def test_includes_symbols(self):
        pwd = generate_password(length=10, use_upper=False, use_lower=False, use_digits=False, use_symbols=True)
        self.assertTrue(all(c in string.punctuation for c in pwd))
        self.assertTrue(any(c in string.punctuation for c in pwd))

    def test_guarantees_character_types(self):
        # Even with a small length (e.g. 4), it should guarantee one of each type if all 4 are selected
        pwd = generate_password(length=4, use_upper=True, use_lower=True, use_digits=True, use_symbols=True)
        self.assertEqual(len(pwd), 4)
        self.assertTrue(any(c in string.ascii_uppercase for c in pwd))
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))
        self.assertTrue(any(c in string.digits for c in pwd))
        self.assertTrue(any(c in string.punctuation for c in pwd))

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)
        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_length_too_small_for_requirements(self):
        with self.assertRaises(ValueError):
            # 4 sets required, but length is 3
            generate_password(length=3, use_upper=True, use_lower=True, use_digits=True, use_symbols=True)

    def test_no_character_sets_selected(self):
        with self.assertRaises(ValueError):
            generate_password(use_upper=False, use_lower=False, use_digits=False, use_symbols=False)

if __name__ == '__main__':
    unittest.main()
