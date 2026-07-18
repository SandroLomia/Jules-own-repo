import unittest
from markdown_table_generator import MarkdownTableGenerator

class TestMarkdownTableGenerator(unittest.TestCase):

    def test_generate_from_csv_basic(self):
        csv_data = "Name,Age,City\nAlice,30,New York\nBob,25,Los Angeles"
        expected = (
            "| Name | Age | City |\n"
            "| --- | --- | --- |\n"
            "| Alice | 30 | New York |\n"
            "| Bob | 25 | Los Angeles |"
        )
        result = MarkdownTableGenerator.generate_from_csv(csv_data)
        self.assertEqual(result, expected)

    def test_generate_from_csv_empty(self):
        self.assertEqual(MarkdownTableGenerator.generate_from_csv(""), "")
        self.assertEqual(MarkdownTableGenerator.generate_from_csv("   \n   "), "")

    def test_generate_from_csv_missing_columns(self):
        # CSV where the second row has fewer columns than the header
        csv_data = "Col1,Col2,Col3\nVal1,Val2"
        expected = (
            "| Col1 | Col2 | Col3 |\n"
            "| --- | --- | --- |\n"
            "| Val1 | Val2 |  |"
        )
        result = MarkdownTableGenerator.generate_from_csv(csv_data)
        self.assertEqual(result, expected)

    def test_generate_from_dicts_basic(self):
        data = [
            {"Task": "Write Code", "Status": "Done", "Assignee": "Jules"},
            {"Task": "Write Tests", "Status": "In Progress", "Assignee": "Jules"}
        ]
        expected = (
            "| Task | Status | Assignee |\n"
            "| --- | --- | --- |\n"
            "| Write Code | Done | Jules |\n"
            "| Write Tests | In Progress | Jules |"
        )
        result = MarkdownTableGenerator.generate_from_dicts(data)
        self.assertEqual(result, expected)

    def test_generate_from_dicts_empty(self):
        self.assertEqual(MarkdownTableGenerator.generate_from_dicts([]), "")

    def test_generate_from_dicts_missing_keys(self):
        data = [
            {"Name": "Alice", "Role": "Admin"},
            {"Name": "Bob"} # Missing 'Role'
        ]
        expected = (
            "| Name | Role |\n"
            "| --- | --- |\n"
            "| Alice | Admin |\n"
            "| Bob |  |"
        )
        result = MarkdownTableGenerator.generate_from_dicts(data)
        self.assertEqual(result, expected)

    def test_generate_from_dicts_extra_keys_ignored(self):
        data = [
            {"ColA": "1", "ColB": "2"},
            {"ColA": "3", "ColB": "4", "ColC": "5"} # ColC should be ignored
        ]
        expected = (
            "| ColA | ColB |\n"
            "| --- | --- |\n"
            "| 1 | 2 |\n"
            "| 3 | 4 |"
        )
        result = MarkdownTableGenerator.generate_from_dicts(data)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
