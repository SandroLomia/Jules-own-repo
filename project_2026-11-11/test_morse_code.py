import unittest
from morse_code import MorseCodeTranslator

class TestMorseCodeTranslator(unittest.TestCase):
    def setUp(self):
        self.translator = MorseCodeTranslator()

    def test_text_to_morse(self):
        self.assertEqual(self.translator.text_to_morse("HELLO WORLD"), ".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
        self.assertEqual(self.translator.text_to_morse("hello world"), ".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
        self.assertEqual(self.translator.text_to_morse("SOS"), "... --- ...")
        self.assertEqual(self.translator.text_to_morse("123"), ".---- ..--- ...--")

    def test_morse_to_text(self):
        self.assertEqual(self.translator.morse_to_text(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."), "HELLO WORLD")
        self.assertEqual(self.translator.morse_to_text("... --- ..."), "SOS")
        self.assertEqual(self.translator.morse_to_text(".---- ..--- ...--"), "123")

    def test_empty_string(self):
        self.assertEqual(self.translator.text_to_morse(""), "")
        self.assertEqual(self.translator.morse_to_text(""), "")
        self.assertEqual(self.translator.text_to_morse("   "), "")
        self.assertEqual(self.translator.morse_to_text("   "), "")

    def test_unknown_characters_text_to_morse(self):
        self.assertEqual(self.translator.text_to_morse("HELLO ~WORLD"), ".... . .-.. .-.. --- / .-- --- .-. .-.. -..")

    def test_unknown_characters_morse_to_text(self):
         self.assertEqual(self.translator.morse_to_text(".... . .-.. .-.. --- / .-- --- .-. .-.. -.. ......."), "HELLO WORLD?")

if __name__ == '__main__':
    unittest.main()
