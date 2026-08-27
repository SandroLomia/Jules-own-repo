import unittest
import string
from securepass import generate_password, evaluate_strength

class TestSecurePass(unittest.TestCase):

    def test_generate_password_length(self):
        self.assertEqual(len(generate_password(length=8)), 8)
        self.assertEqual(len(generate_password(length=20)), 20)

    def test_generate_password_character_sets(self):
        # Test full character sets
        pwd = generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_special=True)
        self.assertTrue(any(c in string.ascii_uppercase for c in pwd))
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))
        self.assertTrue(any(c in string.digits for c in pwd))
        self.assertTrue(any(c in string.punctuation for c in pwd))

        # Test specific sets (e.g. only lowercase and digits)
        pwd2 = generate_password(length=12, use_upper=False, use_lower=True, use_digits=True, use_special=False)
        self.assertFalse(any(c in string.ascii_uppercase for c in pwd2))
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd2))
        self.assertTrue(any(c in string.digits for c in pwd2))
        self.assertFalse(any(c in string.punctuation for c in pwd2))

    def test_generate_password_invalid(self):
        with self.assertRaises(ValueError):
            generate_password(length=0)

        with self.assertRaises(ValueError):
            generate_password(length=16, use_upper=False, use_lower=False, use_digits=False, use_special=False)

        with self.assertRaises(ValueError):
            generate_password(length=2, use_upper=True, use_lower=True, use_digits=True, use_special=True)

    def test_evaluate_strength_weak_password(self):
        result = evaluate_strength("password")
        self.assertLess(result["score"], 2)

        result_short = evaluate_strength("ab1")
        self.assertEqual(result_short["score"], 0)

    def test_evaluate_strength_strong_password(self):
        # Should be a strong password due to mix and length
        result = evaluate_strength("aB3$xyz9L!pQ2@mN")
        self.assertGreaterEqual(result["score"], 3)
        self.assertGreater(result["entropy"], 70)

if __name__ == '__main__':
    unittest.main()
