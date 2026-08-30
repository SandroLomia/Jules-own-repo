import unittest
from toc_generator import generate_toc

class TestTOCGenerator(unittest.TestCase):

    def test_basic_headings(self):
        markdown = """
# Main Title
## Section 1
### Subsection 1.1
## Section 2
"""
        expected = """- [Main Title](#main-title)
  - [Section 1](#section-1)
    - [Subsection 1.1](#subsection-11)
  - [Section 2](#section-2)"""
        self.assertEqual(generate_toc(markdown).strip(), expected.strip())

    def test_code_block_exclusion(self):
        markdown = """
## Valid Heading
```python
# Not a heading
## Still not a heading
```
### Valid Subheading
"""
        expected = """  - [Valid Heading](#valid-heading)
    - [Valid Subheading](#valid-subheading)"""
        self.assertEqual(generate_toc(markdown).strip(), expected.strip())

    def test_special_characters_in_anchors(self):
        markdown = """
## What is "Markdown"?
### API @ 100%
#### Ready, set, go!
"""
        expected = """  - [What is "Markdown"?](#what-is-markdown)
    - [API @ 100%](#api-100)
      - [Ready, set, go!](#ready-set-go)"""
        self.assertEqual(generate_toc(markdown).strip(), expected.strip())

    def test_empty_input(self):
        self.assertEqual(generate_toc(""), "")

if __name__ == "__main__":
    unittest.main()
