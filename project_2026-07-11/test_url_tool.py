import unittest
from url_tool import encode_url, decode_url

class TestUrlTool(unittest.TestCase):
    def test_encode_url_alphanumeric(self):
        self.assertEqual(encode_url("HelloWorld123"), "HelloWorld123")

    def test_encode_url_spaces(self):
        self.assertEqual(encode_url("Hello World"), "Hello%20World")

    def test_encode_url_special_chars(self):
        self.assertEqual(encode_url("a=1&b=2?c/d"), "a%3D1%26b%3D2%3Fc%2Fd")

    def test_encode_url_empty_string(self):
        self.assertEqual(encode_url(""), "")

    def test_decode_url_alphanumeric(self):
        self.assertEqual(decode_url("HelloWorld123"), "HelloWorld123")

    def test_decode_url_spaces(self):
        self.assertEqual(decode_url("Hello%20World"), "Hello World")

    def test_decode_url_special_chars(self):
        self.assertEqual(decode_url("a%3D1%26b%3D2%3Fc%2Fd"), "a=1&b=2?c/d")

    def test_decode_url_empty_string(self):
        self.assertEqual(decode_url(""), "")

    def test_encode_decode_roundtrip(self):
        original = "Complex string with spaces and & special = chars !@#$"
        encoded = encode_url(original)
        decoded = decode_url(encoded)
        self.assertEqual(original, decoded)

if __name__ == "__main__":
    unittest.main()
