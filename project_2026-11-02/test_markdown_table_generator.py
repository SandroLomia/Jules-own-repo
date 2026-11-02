import unittest
from markdown_table_generator import MarkdownTableGenerator

class TestMarkdownTableGenerator(unittest.TestCase):
    def test_empty_list(self):
        generator = MarkdownTableGenerator([])
        self.assertEqual(generator.generate(), "")

    def test_empty_inner_lists(self):
        generator = MarkdownTableGenerator([[], []])
        self.assertEqual(generator.generate(), "")

    def test_standard_data(self):
        data = [
            ["Name", "Age", "City"],
            ["Alice", "30", "New York"],
            ["Bob", "25", "San Francisco"]
        ]
        generator = MarkdownTableGenerator(data)
        expected = (
            "| Name  | Age | City          |\n"
            "|-------|-----|---------------|\n"
            "| Alice | 30  | New York      |\n"
            "| Bob   | 25  | San Francisco |"
        )
        self.assertEqual(generator.generate(), expected)

    def test_uneven_row_lengths(self):
        data = [
            ["ID", "Description"],
            ["1", "Item One", "Extra Info"], # Row is longer than header
            ["2"] # Row is shorter than header
        ]
        generator = MarkdownTableGenerator(data)
        expected = (
            "| ID  | Description |            |\n"
            "|-----|-------------|------------|\n"
            "| 1   | Item One    | Extra Info |\n"
            "| 2   |             |            |"
        )
        self.assertEqual(generator.generate(), expected)

    def test_minimum_column_width(self):
        data = [
            ["A", "B"],
            ["1", "2"]
        ]
        generator = MarkdownTableGenerator(data)
        expected = (
            "| A   | B   |\n"
            "|-----|-----|\n"
            "| 1   | 2   |"
        )
        self.assertEqual(generator.generate(), expected)

if __name__ == "__main__":
    unittest.main()
