import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_length(self):
        self.assertEqual(len(generate_password(length=12)), 12)
        self.assertEqual(len(generate_password(length=8)), 8)
        self.assertEqual(len(generate_password(length=32)), 32)

    def test_character_inclusion(self):
        # Test only uppercase
        pwd = generate_password(length=10, lowercase=False, numbers=False, special=False)
        self.assertTrue(all(c in string.ascii_uppercase for c in pwd))
        self.assertTrue(any(c in string.ascii_uppercase for c in pwd))

        # Test only lowercase
        pwd = generate_password(length=10, uppercase=False, numbers=False, special=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in pwd))
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))

        # Test only numbers
        pwd = generate_password(length=10, uppercase=False, lowercase=False, special=False)
        self.assertTrue(all(c in string.digits for c in pwd))
        self.assertTrue(any(c in string.digits for c in pwd))

        # Test only special
        pwd = generate_password(length=10, uppercase=False, lowercase=False, numbers=False)
        self.assertTrue(all(c in string.punctuation for c in pwd))
        self.assertTrue(any(c in string.punctuation for c in pwd))

        # Test all inclusions
        pwd = generate_password(length=10, uppercase=True, lowercase=True, numbers=True, special=True)
        self.assertTrue(any(c in string.ascii_uppercase for c in pwd))
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))
        self.assertTrue(any(c in string.digits for c in pwd))
        self.assertTrue(any(c in string.punctuation for c in pwd))

    def test_value_error_exceptions(self):
        # Test negative length
        with self.assertRaises(ValueError):
            generate_password(length=-1)

        # Test zero length
        with self.assertRaises(ValueError):
            generate_password(length=0)

        # Test no options selected
        with self.assertRaises(ValueError):
            generate_password(uppercase=False, lowercase=False, numbers=False, special=False)

        # Test length too short for selected criteria
        with self.assertRaises(ValueError):
            generate_password(length=3, uppercase=True, lowercase=True, numbers=True, special=True)

if __name__ == '__main__':
    unittest.main()
