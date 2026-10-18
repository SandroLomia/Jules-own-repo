import unittest
import string
from password_generator import SecurePasswordGenerator

class TestSecurePasswordGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = SecurePasswordGenerator()

    def test_default_length(self):
        password = self.generator.generate_password()
        self.assertEqual(len(password), 12)

    def test_custom_length(self):
        password = self.generator.generate_password(16)
        self.assertEqual(len(password), 16)

    def test_short_length_error(self):
        with self.assertRaises(ValueError):
            self.generator.generate_password(3)

    def test_all_character_types_included_by_default(self):
        password = self.generator.generate_password(20)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_special = any(c in string.punctuation for c in password)

        self.assertTrue(has_upper)
        self.assertTrue(has_lower)
        self.assertTrue(has_digit)
        self.assertTrue(has_special)

    def test_no_special_characters(self):
        gen = SecurePasswordGenerator(include_special=False)
        password = gen.generate_password(20)
        has_special = any(c in string.punctuation for c in password)
        self.assertFalse(has_special)

    def test_evaluate_strength_strong(self):
        self.assertEqual(self.generator.evaluate_strength("StrongPassw0rd!"), "Strong")

    def test_evaluate_strength_medium(self):
        self.assertEqual(self.generator.evaluate_strength("MediumPass"), "Medium")

    def test_evaluate_strength_weak(self):
        self.assertEqual(self.generator.evaluate_strength("abc"), "Weak")
        self.assertEqual(self.generator.evaluate_strength("12345"), "Weak")

if __name__ == "__main__":
    unittest.main()
