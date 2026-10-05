import unittest
from markdown_converter import convert_to_html

class TestMarkdownConverter(unittest.TestCase):
    def test_headers(self):
        self.assertEqual(convert_to_html("# Header 1"), "<h1>Header 1</h1>")
        self.assertEqual(convert_to_html("###### Header 6"), "<h6>Header 6</h6>")

    def test_paragraphs(self):
        self.assertEqual(convert_to_html("Just a paragraph."), "<p>Just a paragraph.</p>")

    def test_bold_and_italic(self):
        self.assertEqual(convert_to_html("**Bold** text"), "<p><strong>Bold</strong> text</p>")
        self.assertEqual(convert_to_html("*Italic* text"), "<p><em>Italic</em> text</p>")
        self.assertEqual(convert_to_html("**Bold** and *Italic*"), "<p><strong>Bold</strong> and <em>Italic</em></p>")

    def test_xss_prevention(self):
        # The script tag should be escaped
        xss_input = "<script>alert('xss')</script>"
        expected_output = "<p>&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;</p>"
        self.assertEqual(convert_to_html(xss_input), expected_output)

    def test_empty_input(self):
        self.assertEqual(convert_to_html(""), "")
        self.assertEqual(convert_to_html("   "), "")

if __name__ == '__main__':
    unittest.main()
