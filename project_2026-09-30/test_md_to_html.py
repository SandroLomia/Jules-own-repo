import unittest
from md_to_html import convert_markdown_to_html

class TestMarkdownToHtml(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(convert_markdown_to_html(""), "")
        self.assertEqual(convert_markdown_to_html(None), "")

    def test_headers(self):
        self.assertEqual(convert_markdown_to_html("# Header 1"), "<h1>Header 1</h1>")
        self.assertEqual(convert_markdown_to_html("## Header 2"), "<h2>Header 2</h2>")
        self.assertEqual(convert_markdown_to_html("###### Header 6"), "<h6>Header 6</h6>")

    def test_bold(self):
        self.assertEqual(convert_markdown_to_html("This is **bold** text."), "<p>This is <strong>bold</strong> text.</p>")
        self.assertEqual(convert_markdown_to_html("**Bold** at start."), "<p><strong>Bold</strong> at start.</p>")

    def test_italic(self):
        self.assertEqual(convert_markdown_to_html("This is *italic* text."), "<p>This is <em>italic</em> text.</p>")
        self.assertEqual(convert_markdown_to_html("This is _italic_ text too."), "<p>This is <em>italic</em> text too.</p>")

    def test_bold_and_italic(self):
        self.assertEqual(convert_markdown_to_html("This has **bold** and *italic*."), "<p>This has <strong>bold</strong> and <em>italic</em>.</p>")

    def test_lists(self):
        markdown_list = "* Item 1\n* Item 2\n* Item 3"
        expected_html = "<ul>\n<li>Item 1</li>\n<li>Item 2</li>\n<li>Item 3</li>\n</ul>"
        self.assertEqual(convert_markdown_to_html(markdown_list), expected_html)

    def test_mixed_content(self):
        markdown = "# Hello\n\nThis is a **test**.\n\n* List item 1\n* List item 2"
        expected = "<h1>Hello</h1>\n\n<p>This is a <strong>test</strong>.</p>\n\n<ul>\n<li>List item 1</li>\n<li>List item 2</li>\n</ul>"
        self.assertEqual(convert_markdown_to_html(markdown), expected)

    def test_text_after_list(self):
        markdown = "* Item 1\n* Item 2\nSome text here"
        expected = "<ul>\n<li>Item 1</li>\n<li>Item 2</li>\n</ul>\n<p>Some text here</p>"
        self.assertEqual(convert_markdown_to_html(markdown), expected)

    def test_html_escaping(self):
        markdown = "<script>alert('xss');</script>"
        expected = "<p>&lt;script&gt;alert(&#x27;xss&#x27;);&lt;/script&gt;</p>"
        self.assertEqual(convert_markdown_to_html(markdown), expected)

if __name__ == '__main__':
    unittest.main()
