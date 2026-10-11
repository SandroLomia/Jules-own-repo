import unittest
from markdown_to_html import convert_markdown

class TestMarkdownToHtml(unittest.TestCase):

    def test_headers(self):
        self.assertEqual(convert_markdown("# Header 1"), "<h1>Header 1</h1>")
        self.assertEqual(convert_markdown("## Header 2"), "<h2>Header 2</h2>")
        self.assertEqual(convert_markdown("### Header 3"), "<h3>Header 3</h3>")
        self.assertEqual(convert_markdown("###### Header 6"), "<h6>Header 6</h6>")
        # Ensure non-headers are unaffected
        self.assertEqual(convert_markdown("####### Invalid Header"), "####### Invalid Header")
        self.assertEqual(convert_markdown("#No space header"), "#No space header")

    def test_bold_text(self):
        self.assertEqual(convert_markdown("This is **bold** text."), "This is <strong>bold</strong> text.")
        self.assertEqual(convert_markdown("**Bold** at start."), "<strong>Bold</strong> at start.")
        self.assertEqual(convert_markdown("End with **bold**"), "End with <strong>bold</strong>")

    def test_italic_text(self):
        self.assertEqual(convert_markdown("This is *italic* text."), "This is <em>italic</em> text.")
        self.assertEqual(convert_markdown("*Italic* at start."), "<em>Italic</em> at start.")
        self.assertEqual(convert_markdown("End with *italic*"), "End with <em>italic</em>")

    def test_bold_and_italic(self):
        self.assertEqual(convert_markdown("Text with **bold** and *italic*."), "Text with <strong>bold</strong> and <em>italic</em>.")

    def test_xss_prevention(self):
        # Script tags should be escaped
        malicious_input = "<script>alert('XSS')</script>"
        safe_output = convert_markdown(malicious_input)
        self.assertNotIn("<script>", safe_output)
        self.assertIn("&lt;script&gt;", safe_output)

        # Markdown with malicious payload
        mixed_input = "# Title\n**bold** and <script>attack</script>"
        expected_output = "<h1>Title</h1>\n<strong>bold</strong> and &lt;script&gt;attack&lt;/script&gt;"
        self.assertEqual(convert_markdown(mixed_input), expected_output)

    def test_empty_string(self):
        self.assertEqual(convert_markdown(""), "")
        self.assertEqual(convert_markdown(None), "")

if __name__ == '__main__':
    unittest.main()
