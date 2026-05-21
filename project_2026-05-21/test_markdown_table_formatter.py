import unittest
import os
import tempfile
from markdown_table_formatter import is_table_divider, parse_table_row, format_table, format_markdown_file

class TestMarkdownTableFormatter(unittest.TestCase):

    def test_is_table_divider(self):
        self.assertTrue(is_table_divider("|---|---|"))
        self.assertTrue(is_table_divider("|:---|---:|:---:|"))
        self.assertTrue(is_table_divider("| - | - |"))
        self.assertFalse(is_table_divider("| a | b |"))
        self.assertFalse(is_table_divider("Not a divider"))
        self.assertFalse(is_table_divider("|---|---")) # Missing trailing pipe

    def test_parse_table_row(self):
        self.assertEqual(parse_table_row("| a | b |"), ["a", "b"])
        self.assertEqual(parse_table_row("|a|b|"), ["a", "b"])
        self.assertEqual(parse_table_row("| a |  b  | c |"), ["a", "b", "c"])
        self.assertEqual(parse_table_row("| | b |"), ["", "b"])

    def test_format_table(self):
        input_lines = [
            "|Header 1|H2|",
            "|---|---|",
            "|Val 1|Longer Value 2|"
        ]
        expected_output = [
            "| Header 1 | H2             |",
            "| -------- | -------------- |",
            "| Val 1    | Longer Value 2 |"
        ]
        self.assertEqual(format_table(input_lines), expected_output)

    def test_format_table_with_alignment(self):
        input_lines = [
            "|Left|Center|Right|",
            "|:---|:---:|---:|",
            "|1|2|3|"
        ]
        expected_output = [
            "| Left | Center | Right |",
            "| :--- | :----: | ----: |",
            "| 1    | 2      | 3     |"
        ]
        self.assertEqual(format_table(input_lines), expected_output)

    def test_format_table_missing_columns(self):
        input_lines = [
            "|Col 1|Col 2|Col 3|",
            "|---|---|---|",
            "|Val 1|Val 2|"
        ]
        expected_output = [
            "| Col 1 | Col 2 | Col 3 |",
            "| ----- | ----- | ----- |",
            "| Val 1 | Val 2 |       |"
        ]
        self.assertEqual(format_table(input_lines), expected_output)

    def test_format_markdown_file_inplace(self):
        # Create a temporary file with unformatted tables
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as temp_file:
            temp_file.write("# Test\n\n")
            temp_file.write("Some text here.\n\n")
            temp_file.write("|Col1|Column2|\n")
            temp_file.write("|---|---|\n")
            temp_file.write("|A|B|\n\n")
            temp_filepath = temp_file.name

        try:
            # Format the file
            format_markdown_file(temp_filepath, inplace=True)

            # Read back and verify
            with open(temp_filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            expected_content = (
                "# Test\n\n"
                "Some text here.\n\n"
                "| Col1 | Column2 |\n"
                "| ---- | ------- |\n"
                "| A    | B       |\n\n"
            )
            self.assertEqual(content, expected_content)
        finally:
            # Clean up
            if os.path.exists(temp_filepath):
                os.remove(temp_filepath)

if __name__ == '__main__':
    unittest.main()
