import unittest
from markdown_converter import convert_to_html

class TestMarkdownConverter(unittest.TestCase):
    def test_header_conversion(self):
        self.assertEqual(convert_to_html("# Header 1"), "<h1>Header 1</h1>")
        self.assertEqual(convert_to_html("## Header 2"), "<h2>Header 2</h2>")
        self.assertEqual(convert_to_html("###### Header 6"), "<h6>Header 6</h6>")
        # Should be a paragraph if not a valid header
        self.assertEqual(convert_to_html("####### Header 7"), "<p>####### Header 7</p>")
        self.assertEqual(convert_to_html("#Not a header"), "<p>#Not a header</p>")

    def test_bold_text_conversion(self):
        self.assertEqual(convert_to_html("**bold**"), "<p><b>bold</b></p>")
        self.assertEqual(convert_to_html("__bold__"), "<p><b>bold</b></p>")
        self.assertEqual(convert_to_html("Some **bold** text"), "<p>Some <b>bold</b> text</p>")

    def test_italic_text_conversion(self):
        self.assertEqual(convert_to_html("*italic*"), "<p><i>italic</i></p>")
        self.assertEqual(convert_to_html("_italic_"), "<p><i>italic</i></p>")
        self.assertEqual(convert_to_html("Some *italic* text"), "<p>Some <i>italic</i> text</p>")

    def test_combined_formatting(self):
        self.assertEqual(convert_to_html("# Header with **bold**"), "<h1>Header with <b>bold</b></h1>")
        self.assertEqual(convert_to_html("## Header with *italic*"), "<h2>Header with <i>italic</i></h2>")

    def test_xss_sanitization(self):
        # The html should be escaped before applying our markdown regexes
        self.assertEqual(
            convert_to_html("<script>alert('xss')</script>"),
            "<p>&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;</p>"
        )
        self.assertEqual(
            convert_to_html("# <script>alert(1)</script>"),
            "<h1>&lt;script&gt;alert(1)&lt;/script&gt;</h1>"
        )
        self.assertEqual(
            convert_to_html("**<img src=x onerror=alert(1)>**"),
            "<p><b>&lt;img src=x onerror=alert(1)&gt;</b></p>"
        )

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            convert_to_html(123)
        with self.assertRaises(TypeError):
            convert_to_html(None)

    def test_multiline(self):
        markdown = "# Hello\n\nThis is a **test**."
        expected = "<h1>Hello</h1>\n<p>This is a <b>test</b>.</p>"
        self.assertEqual(convert_to_html(markdown), expected)

if __name__ == '__main__':
    unittest.main()
