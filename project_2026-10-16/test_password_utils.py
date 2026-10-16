import unittest
import string
from password_utils import generate_password, evaluate_strength

class TestPasswordUtils(unittest.TestCase):

    def test_generate_password_length(self):
        self.assertEqual(len(generate_password(length=8)), 8)
        self.assertEqual(len(generate_password(length=16)), 16)
        with self.assertRaises(ValueError):
            generate_password(length=0)

    def test_generate_password_character_sets(self):
        # Only lowercase
        pwd = generate_password(length=10, use_uppercase=False, use_lowercase=True, use_digits=False, use_special=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in pwd))

        # Only digits
        pwd = generate_password(length=10, use_uppercase=False, use_lowercase=False, use_digits=True, use_special=False)
        self.assertTrue(all(c in string.digits for c in pwd))

        # No character sets selected
        with self.assertRaises(ValueError):
            generate_password(use_uppercase=False, use_lowercase=False, use_digits=False, use_special=False)

    def test_evaluate_strength_levels(self):
        # Strong: >=12 length, >=3 character types
        self.assertEqual(evaluate_strength("StrongPass123!"), "Strong")

        # Medium: >=8 length, >=2 character types
        self.assertEqual(evaluate_strength("Medium123"), "Medium")

        # Weak: <8 length or <2 character types
        self.assertEqual(evaluate_strength("weak"), "Weak")
        self.assertEqual(evaluate_strength("1234567"), "Weak")

if __name__ == '__main__':
    unittest.main()
