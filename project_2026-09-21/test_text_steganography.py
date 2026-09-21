import unittest
from text_steganography import hide_message, reveal_message

class TestTextSteganography(unittest.TestCase):
    def test_hide_and_reveal_basic(self):
        secret = "secret"
        cover = "Hello World"
        stego_text = hide_message(secret, cover)

        self.assertNotEqual(stego_text, cover)
        self.assertTrue(len(stego_text) > len(cover))

        revealed = reveal_message(stego_text)
        self.assertEqual(revealed, secret)

    def test_non_ascii_characters(self):
        secret = "こんにちは 🌍"
        cover = "Normal text"
        stego_text = hide_message(secret, cover)

        revealed = reveal_message(stego_text)
        self.assertEqual(revealed, secret)

    def test_empty_message(self):
        secret = ""
        cover = "Just some text"
        stego_text = hide_message(secret, cover)
        self.assertEqual(stego_text, cover)

        revealed = reveal_message(stego_text)
        self.assertEqual(revealed, "")

    def test_no_hidden_message(self):
        cover = "Text without hidden message"
        revealed = reveal_message(cover)
        self.assertEqual(revealed, "")

    def test_empty_cover_text(self):
        secret = "Hidden"
        cover = ""
        stego_text = hide_message(secret, cover)

        revealed = reveal_message(stego_text)
        self.assertEqual(revealed, secret)

if __name__ == '__main__':
    unittest.main()
