import unittest
from totp import TOTPGenerator

class TestTOTPGenerator(unittest.TestCase):
    def setUp(self):
        # Known test vectors from RFC 6238 Appendix B
        # The secret is the ASCII string "12345678901234567890" which base32 encodes to:
        self.secret = "GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ"

    def test_totp_rfc6238_vectors(self):
        totp = TOTPGenerator(self.secret, digits=8)

        # Test vector format: (timestamp, expected_8_digit_totp)
        test_vectors = [
            (59, "94287082"),
            (1111111109, "07081804"),
            (1111111111, "14050471"),
            (1234567890, "89005924"),
            (2000000000, "69279037"),
            (20000000000, "65353130")
        ]

        for timestamp, expected in test_vectors:
            with self.subTest(timestamp=timestamp):
                result = totp.generate(for_time=timestamp)
                self.assertEqual(result, expected)

    def test_totp_default_digits(self):
        totp = TOTPGenerator(self.secret) # default digits=6

        test_vectors = [
            (59, "287082"),
            (1111111109, "081804"),
            (1111111111, "050471"),
            (1234567890, "005924"),
            (2000000000, "279037"),
            (20000000000, "353130")
        ]

        for timestamp, expected in test_vectors:
            with self.subTest(timestamp=timestamp):
                result = totp.generate(for_time=timestamp)
                self.assertEqual(result, expected)

    def test_invalid_secret(self):
        with self.assertRaises(ValueError):
            TOTPGenerator("invalid_base32_chars!@#")

if __name__ == '__main__':
    unittest.main()
