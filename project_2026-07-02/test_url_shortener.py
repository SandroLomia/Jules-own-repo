import unittest
from url_shortener import URLShortener

class TestURLShortener(unittest.TestCase):
    def setUp(self):
        self.shortener = URLShortener()

    def test_shorten_and_expand(self):
        long_url = "https://www.google.com"
        short_code = self.shortener.shorten_url(long_url)

        self.assertEqual(len(short_code), 6)
        self.assertTrue(short_code.isalnum())

        expanded_url = self.shortener.expand_url(short_code)
        self.assertEqual(expanded_url, long_url)

    def test_same_url_returns_same_code(self):
        long_url = "https://www.openai.com"
        short_code1 = self.shortener.shorten_url(long_url)
        short_code2 = self.shortener.shorten_url(long_url)

        self.assertEqual(short_code1, short_code2)

    def test_invalid_code_returns_none(self):
        expanded_url = self.shortener.expand_url("invalid")
        self.assertIsNone(expanded_url)

    def test_different_urls_different_codes(self):
        url1 = "https://example.com/1"
        url2 = "https://example.com/2"

        code1 = self.shortener.shorten_url(url1)
        code2 = self.shortener.shorten_url(url2)

        self.assertNotEqual(code1, code2)

if __name__ == '__main__':
    unittest.main()
