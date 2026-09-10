import unittest
from markdown_toc_generator import MarkdownTOCGenerator

class TestMarkdownTOCGenerator(unittest.TestCase):

    def test_create_slug(self):
        self.assertEqual(MarkdownTOCGenerator._create_slug("Header One"), "header-one")
        self.assertEqual(MarkdownTOCGenerator._create_slug("Header   With  Spaces"), "header-with-spaces")
        self.assertEqual(MarkdownTOCGenerator._create_slug("Header-with-hyphens"), "header-with-hyphens")
        self.assertEqual(MarkdownTOCGenerator._create_slug("Header with !@#$%^&*() characters"), "header-with-characters")
        self.assertEqual(MarkdownTOCGenerator._create_slug("  Leading and trailing   "), "leading-and-trailing")

    def test_generate_toc_basic(self):
        markdown_text = (
            "# Introduction\n"
            "Some text here.\n\n"
            "## Section 1\n"
            "More text.\n\n"
            "### Subsection 1.1\n"
            "Even more text.\n"
        )
        expected_toc = (
            "- [Introduction](#introduction)\n"
            "  - [Section 1](#section-1)\n"
            "    - [Subsection 1.1](#subsection-11)"
        )
        self.assertEqual(MarkdownTOCGenerator.generate_toc(markdown_text), expected_toc)

    def test_generate_toc_ignores_code_blocks(self):
        markdown_text = (
            "# Main Header\n"
            "```python\n"
            "# This is a comment, not a header\n"
            "## This is also inside a code block\n"
            "```\n"
            "## Actual Subheader\n"
        )
        expected_toc = (
            "- [Main Header](#main-header)\n"
            "  - [Actual Subheader](#actual-subheader)"
        )
        self.assertEqual(MarkdownTOCGenerator.generate_toc(markdown_text), expected_toc)

    def test_inject_toc(self):
        markdown_text = (
            "# My Document\n\n"
            "<!-- TOC -->\n\n"
            "## Chapter 1\n"
            "Content."
        )
        expected_output = (
            "# My Document\n\n"
            "- [My Document](#my-document)\n"
            "  - [Chapter 1](#chapter-1)\n\n"
            "## Chapter 1\n"
            "Content."
        )
        self.assertEqual(MarkdownTOCGenerator.inject_toc(markdown_text), expected_output)

    def test_inject_toc_no_placeholder(self):
        markdown_text = (
            "# My Document\n\n"
            "No placeholder here.\n\n"
            "## Chapter 1\n"
            "Content."
        )
        self.assertEqual(MarkdownTOCGenerator.inject_toc(markdown_text), markdown_text)

if __name__ == '__main__':
    unittest.main()
