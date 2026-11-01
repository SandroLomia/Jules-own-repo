import unittest
from markdown_converter import MarkdownConverter

class TestMarkdownConverter(unittest.TestCase):
    def setUp(self):
        self.converter = MarkdownConverter()

    def test_empty_string(self):
        self.assertEqual(self.converter.convert(""), "")

    def test_headers(self):
        self.assertEqual(self.converter.convert("# Header 1"), "<h1>Header 1</h1>")
        self.assertEqual(self.converter.convert("## Header 2"), "<h2>Header 2</h2>")
        self.assertEqual(self.converter.convert("### Header 3"), "<h3>Header 3</h3>")
        self.assertEqual(self.converter.convert("#### Header 4"), "<h4>Header 4</h4>")
        self.assertEqual(self.converter.convert("##### Header 5"), "<h5>Header 5</h5>")
        self.assertEqual(self.converter.convert("###### Header 6"), "<h6>Header 6</h6>")

    def test_bold(self):
        self.assertEqual(self.converter.convert("**Bold text**"), "<p><strong>Bold text</strong></p>")
        self.assertEqual(self.converter.convert("__Bold text__"), "<p><strong>Bold text</strong></p>")

    def test_italic(self):
        self.assertEqual(self.converter.convert("*Italic text*"), "<p><em>Italic text</em></p>")
        self.assertEqual(self.converter.convert("_Italic text_"), "<p><em>Italic text</em></p>")

    def test_paragraphs(self):
        md = "Paragraph 1\n\nParagraph 2"
        expected = "<p>Paragraph 1</p>\n<p>Paragraph 2</p>"
        self.assertEqual(self.converter.convert(md), expected)

    def test_mixed_formatting(self):
        md = "# Title\n\nThis is a **bold** and _italic_ paragraph."
        expected = "<h1>Title</h1>\n<p>This is a <strong>bold</strong> and <em>italic</em> paragraph.</p>"
        self.assertEqual(self.converter.convert(md), expected)

    def test_xss_sanitization(self):
        md = "<script>alert('XSS')</script>"
        expected = "<p>&lt;script&gt;alert(&#x27;XSS&#x27;)&lt;/script&gt;</p>"
        self.assertEqual(self.converter.convert(md), expected)

        md = "# <script>alert(1)</script>"
        expected = "<h1>&lt;script&gt;alert(1)&lt;/script&gt;</h1>"
        self.assertEqual(self.converter.convert(md), expected)

if __name__ == '__main__':
    unittest.main()
