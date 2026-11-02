class MarkdownTableGenerator:
    """Generates a Markdown table from a 2D array of strings."""
    def __init__(self, data: list[list[str]]):
        self.data = data

    def generate(self) -> str:
        """Returns the formatted Markdown table as a string."""
        if not self.data:
            return ""

        # Determine the maximum number of columns
        num_cols = max(len(row) for row in self.data)
        if num_cols == 0:
            return ""

        # Find maximum width for each column
        col_widths = [0] * num_cols
        for row in self.data:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)))

        # Ensure a minimum width of 3 for Markdown separators (e.g., ---)
        col_widths = [max(3, w) for w in col_widths]

        lines = []

        def format_row(row):
            padded = []
            for i in range(num_cols):
                cell_val = str(row[i]) if i < len(row) else ""
                padded.append(cell_val.ljust(col_widths[i]))
            return "| " + " | ".join(padded) + " |"

        # Add header
        lines.append(format_row(self.data[0]))

        # Add separator
        separator_parts = ["-" * w for w in col_widths]
        lines.append("|-" + "-|-".join(separator_parts) + "-|")

        # Add body
        for row in self.data[1:]:
            lines.append(format_row(row))

        return "\n".join(lines)
