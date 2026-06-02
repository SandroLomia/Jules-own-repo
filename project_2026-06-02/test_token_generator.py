import unittest
from token_generator import generate_hex_token, generate_urlsafe_token, generate_bytes_token

class TestTokenGenerator(unittest.TestCase):

    def test_generate_hex_token(self):
        token = generate_hex_token(16)
        self.assertIsInstance(token, str)
        # 16 bytes will result in 32 hex characters
        self.assertEqual(len(token), 32)

    def test_generate_hex_token_zero_bytes(self):
        with self.assertRaises(ValueError):
            generate_hex_token(0)

    def test_generate_urlsafe_token(self):
        token = generate_urlsafe_token(32)
        self.assertIsInstance(token, str)
        # Can't easily assert length as it depends on base64 encoding with/without padding
        self.assertTrue(len(token) > 0)

    def test_generate_urlsafe_token_zero_bytes(self):
        with self.assertRaises(ValueError):
            generate_urlsafe_token(0)

    def test_generate_bytes_token(self):
        token = generate_bytes_token(24)
        self.assertIsInstance(token, bytes)
        self.assertEqual(len(token), 24)

    def test_generate_bytes_token_negative_bytes(self):
        with self.assertRaises(ValueError):
            generate_bytes_token(-5)

if __name__ == '__main__':
    unittest.main()
