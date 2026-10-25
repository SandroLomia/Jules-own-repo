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

    def test_zero_length_raises_error(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)

    def test_negative_length_raises_error(self):
        with self.assertRaises(ValueError):
            generate_password(length=-5)

    def test_no_character_types_raises_error(self):
        with self.assertRaises(ValueError):
            generate_password(use_upper=False, use_lower=False, use_numbers=False, use_symbols=False)

    def test_only_uppercase(self):
        pwd = generate_password(length=10, use_upper=True, use_lower=False, use_numbers=False, use_symbols=False)
        self.assertTrue(all(c in string.ascii_uppercase for c in pwd))

    def test_only_lowercase(self):
        pwd = generate_password(length=10, use_upper=False, use_lower=True, use_numbers=False, use_symbols=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in pwd))

    def test_only_numbers(self):
        pwd = generate_password(length=10, use_upper=False, use_lower=False, use_numbers=True, use_symbols=False)
        self.assertTrue(all(c in string.digits for c in pwd))

    def test_only_symbols(self):
        pwd = generate_password(length=10, use_upper=False, use_lower=False, use_numbers=False, use_symbols=True)
        self.assertTrue(all(c in string.punctuation for c in pwd))

    def test_all_character_types_included(self):
        # Generate a sufficiently long password to ensure all types are included (the generator guarantees this)
        pwd = generate_password(length=20, use_upper=True, use_lower=True, use_numbers=True, use_symbols=True)
        self.assertTrue(any(c in string.ascii_uppercase for c in pwd))
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))
        self.assertTrue(any(c in string.digits for c in pwd))
        self.assertTrue(any(c in string.punctuation for c in pwd))

    def test_short_length_with_all_types(self):
        # Test edge case where length is smaller than number of requested types
        # Expectation: shouldn't crash, will truncate some guarantees but fill to length
        pwd = generate_password(length=2, use_upper=True, use_lower=True, use_numbers=True, use_symbols=True)
        self.assertEqual(len(pwd), 2)

if __name__ == '__main__':
    unittest.main()
