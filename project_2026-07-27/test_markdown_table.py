import unittest
from markdown_table import json_to_markdown_table, markdown_table_to_json

class TestMarkdownTableUtility(unittest.TestCase):

    def test_json_to_markdown_table_empty(self):
        self.assertEqual(json_to_markdown_table([]), "")

    def test_json_to_markdown_table_basic(self):
        data = [
            {"name": "Alice", "age": 30, "city": "New York"},
            {"name": "Bob", "age": 25, "city": "London"}
        ]
        expected = (
            "| name | age | city |\n"
            "| --- | --- | --- |\n"
            "| Alice | 30 | New York |\n"
            "| Bob | 25 | London |"
        )
        self.assertEqual(json_to_markdown_table(data), expected)

    def test_json_to_markdown_table_missing_keys(self):
        data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "city": "London"} # missing age, has extra city which will be ignored based on logic
        ]
        # It uses keys of the first dict as headers
        expected = (
            "| name | age |\n"
            "| --- | --- |\n"
            "| Alice | 30 |\n"
            "| Bob |  |"
        )
        self.assertEqual(json_to_markdown_table(data), expected)

    def test_json_to_markdown_table_escaped_pipe(self):
        data = [
            {"name": "Alice | Smith", "age": 30}
        ]
        expected = (
            "| name | age |\n"
            "| --- | --- |\n"
            "| Alice \\| Smith | 30 |"
        )
        self.assertEqual(json_to_markdown_table(data), expected)

    def test_markdown_table_to_json_empty(self):
        self.assertEqual(markdown_table_to_json(""), [])
        self.assertEqual(markdown_table_to_json("   \n  "), [])

    def test_markdown_table_to_json_basic(self):
        markdown = (
            "| name | age | city |\n"
            "| --- | --- | --- |\n"
            "| Alice | 30 | New York |\n"
            "| Bob | 25 | London |"
        )
        expected = [
            {"name": "Alice", "age": 30, "city": "New York"},
            {"name": "Bob", "age": 25, "city": "London"}
        ]
        self.assertEqual(markdown_table_to_json(markdown), expected)

    def test_markdown_table_to_json_type_coercion(self):
        markdown = (
            "| id | active | score | name |\n"
            "| --- | --- | --- | --- |\n"
            "| 1 | true | 95.5 | Alice |\n"
            "| 2 | false | 80.0 | Bob |"
        )
        expected = [
            {"id": 1, "active": True, "score": 95.5, "name": "Alice"},
            {"id": 2, "active": False, "score": 80.0, "name": "Bob"}
        ]
        self.assertEqual(markdown_table_to_json(markdown), expected)

    def test_markdown_table_to_json_escaped_pipe(self):
        markdown = (
            "| name | desc |\n"
            "| --- | --- |\n"
            "| Alice | A \\| B |"
        )
        expected = [
            {"name": "Alice", "desc": "A | B"}
        ]
        self.assertEqual(markdown_table_to_json(markdown), expected)

    def test_round_trip(self):
        data = [
            {"name": "Alice", "age": 30, "active": True},
            {"name": "Bob", "age": 25, "active": False}
        ]
        markdown = json_to_markdown_table(data)
        parsed_data = markdown_table_to_json(markdown)
        self.assertEqual(parsed_data, data)

if __name__ == '__main__':
    unittest.main()
