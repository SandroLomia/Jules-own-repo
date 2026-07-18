import csv
import io
from typing import List, Dict, Any

class MarkdownTableGenerator:
    """
    A utility class to generate formatted Markdown tables from various data sources.
    """

    @staticmethod
    def _format_row(row: List[str]) -> str:
        """Helper to format a single row with Markdown table syntax."""
        return "| " + " | ".join(str(cell) for cell in row) + " |"

    @staticmethod
    def _generate_separator(num_columns: int) -> str:
        """Helper to generate the separator row."""
        return "| " + " | ".join(["---"] * num_columns) + " |"

    @classmethod
    def generate_from_csv(cls, csv_string: str) -> str:
        """
        Generates a Markdown table from a CSV string.

        Args:
            csv_string (str): A string containing CSV data.

        Returns:
            str: The formatted Markdown table.
        """
        if not csv_string or not csv_string.strip():
            return ""

        f = io.StringIO(csv_string.strip())
        reader = csv.reader(f)

        rows = list(reader)
        if not rows:
            return ""

        headers = rows[0]
        data_rows = rows[1:]

        markdown_rows = []
        markdown_rows.append(cls._format_row(headers))
        markdown_rows.append(cls._generate_separator(len(headers)))

        for row in data_rows:
            # Pad row if it has fewer columns than headers
            padded_row = row + [""] * (len(headers) - len(row))
            # Truncate if it has more
            padded_row = padded_row[:len(headers)]
            markdown_rows.append(cls._format_row(padded_row))

        return "\n".join(markdown_rows)

    @classmethod
    def generate_from_dicts(cls, data: List[Dict[str, Any]]) -> str:
        """
        Generates a Markdown table from a list of dictionaries.
        The keys of the first dictionary are used as the table headers.
        Missing keys in subsequent dictionaries are treated as empty strings.

        Args:
            data (List[Dict[str, Any]]): A list of dictionaries representing the table data.

        Returns:
            str: The formatted Markdown table.
        """
        if not data:
            return ""

        headers = list(data[0].keys())

        markdown_rows = []
        markdown_rows.append(cls._format_row(headers))
        markdown_rows.append(cls._generate_separator(len(headers)))

        for item in data:
            row = [str(item.get(key, "")) for key in headers]
            markdown_rows.append(cls._format_row(row))

        return "\n".join(markdown_rows)
