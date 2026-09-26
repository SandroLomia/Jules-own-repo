import unittest
import string
from password_utils import generate_password, evaluate_strength

class TestPasswordUtils(unittest.TestCase):

    def test_generate_password_length(self):
        # Test exact lengths
        self.assertEqual(len(generate_password(length=8)), 8)
        self.assertEqual(len(generate_password(length=12)), 12)
        self.assertEqual(len(generate_password(length=20)), 20)

        # Test length validation
        with self.assertRaises(ValueError):
            generate_password(length=3)

    def test_generate_password_inclusion(self):
        pwd = generate_password(length=12, include_uppercase=True, include_numbers=True, include_special=True)
        self.assertTrue(any(c.isupper() for c in pwd))
        self.assertTrue(any(c.isdigit() for c in pwd))
        self.assertTrue(any(c in string.punctuation for c in pwd))

    def test_generate_password_exclusion(self):
        pwd = generate_password(length=12, include_uppercase=False, include_numbers=False, include_special=False)
        self.assertFalse(any(c.isupper() for c in pwd))
        self.assertFalse(any(c.isdigit() for c in pwd))
        self.assertFalse(any(c in string.punctuation for c in pwd))
        self.assertTrue(all(c.islower() for c in pwd))

    def test_evaluate_strength_weak(self):
        # Length 7, lowercase only
        self.assertEqual(evaluate_strength("abcdefg"), 0)

        # Length 8, lowercase only
        self.assertEqual(evaluate_strength("abcdefgh"), 1)

    def test_evaluate_strength_medium(self):
        # Length 8, mixed case
        self.assertEqual(evaluate_strength("Abcdefgh"), 2)

        # Length 8, mixed case, number
        self.assertEqual(evaluate_strength("Abcdefg1"), 3)

    def test_evaluate_strength_strong(self):
        # Length 12, mixed case, number, special
        self.assertEqual(evaluate_strength("Abcdefg1!abc"), 4)

        # Super long with everything (max score 4)
        self.assertEqual(evaluate_strength("VeryL0ngP@ssw0rd!withEverything"), 4)

if __name__ == '__main__':
    unittest.main()
