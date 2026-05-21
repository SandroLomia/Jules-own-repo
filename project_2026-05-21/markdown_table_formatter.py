import os
import argparse
import re
from typing import List

def is_table_divider(line: str) -> bool:
    """Check if a line is a markdown table divider (e.g. |---|---|)."""
    line = line.strip()
    if not line.startswith('|') or not line.endswith('|'):
        return False
    # Remove leading and trailing pipes
    content = line[1:-1]
    cells = content.split('|')
    for cell in cells:
        # Check if cell is only dashes, spaces, and optional colons for alignment
        if not re.match(r'^\s*:?-+:?\s*$', cell):
            return False
    return True

def parse_table_row(line: str) -> List[str]:
    """Parse a markdown table row into a list of cells."""
    line = line.strip()
    if not line.startswith('|') or not line.endswith('|'):
        # If it's malformed but we think it's a table row, do our best
        pass

    # Remove leading and trailing pipes for splitting
    content = line[1:-1] if line.startswith('|') and line.endswith('|') else line

    # Split by pipe, but we could handle escaped pipes if we wanted to be more robust
    # For now, simple split
    cells = [cell.strip() for cell in content.split('|')]
    return cells

def format_table(table_lines: List[str]) -> List[str]:
    """Format a list of table lines to have aligned columns."""
    if not table_lines:
        return []

    # Find the divider index to preserve alignment indicators if present
    divider_index = -1
    for i, line in enumerate(table_lines):
        if is_table_divider(line):
            divider_index = i
            break

    if divider_index == -1:
        # Not a valid table if no divider found, just return original
        return table_lines

    # Parse all rows into cells
    parsed_rows = [parse_table_row(line) for line in table_lines]

    # Find maximum number of columns
    num_cols = max(len(row) for row in parsed_rows)

    # Normalize rows to have the same number of columns
    for row in parsed_rows:
        while len(row) < num_cols:
            row.append("")

    # Calculate max width for each column
    col_widths = [0] * num_cols
    for row_idx, row in enumerate(parsed_rows):
        if row_idx == divider_index:
            continue # Don't count the divider row for width calculation
        for col_idx, cell in enumerate(row):
            col_widths[col_idx] = max(col_widths[col_idx], len(cell))

    # Minimum width of 3 for divider dashes
    for i in range(num_cols):
        col_widths[i] = max(col_widths[i], 3)

    # Reconstruct the table
    formatted_lines = []
    for row_idx, row in enumerate(parsed_rows):
        if row_idx == divider_index:
            # Reconstruct divider
            cells = []
            for col_idx in range(num_cols):
                orig_cell = row[col_idx] if col_idx < len(row) else "-"

                # Check for alignment indicators
                left_align = orig_cell.strip().startswith(':')
                right_align = orig_cell.strip().endswith(':')

                if left_align and right_align:
                    cell = ":" + "-" * (col_widths[col_idx] - 2) + ":"
                elif left_align:
                    cell = ":" + "-" * (col_widths[col_idx] - 1)
                elif right_align:
                    cell = "-" * (col_widths[col_idx] - 1) + ":"
                else:
                    cell = "-" * col_widths[col_idx]
                cells.append(cell)
            formatted_lines.append("| " + " | ".join(cells) + " |")
        else:
            # Reconstruct data row
            cells = []
            for col_idx, cell in enumerate(row):
                cells.append(cell.ljust(col_widths[col_idx]))
            formatted_lines.append("| " + " | ".join(cells) + " |")

    return formatted_lines

def format_markdown_file(filepath: str, inplace: bool = False):
    """Format all markdown tables in a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        output_lines = []
        i = 0
        while i < len(lines):
            line = lines[i].rstrip('\n')

            # Simple check to see if we might be starting a table
            if line.strip().startswith('|'):
                table_lines = [line]
                j = i + 1
                while j < len(lines) and lines[j].strip().startswith('|'):
                    table_lines.append(lines[j].rstrip('\n'))
                    j += 1

                # Check if it actually has a divider
                if any(is_table_divider(l) for l in table_lines):
                    formatted_table = format_table(table_lines)
                    output_lines.extend(formatted_table)
                    i = j
                    continue

            output_lines.append(line)
            i += 1

        output_text = '\n'.join(output_lines) + '\n'

        if inplace:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(output_text)
            print(f"Formatted tables in {filepath}")
        else:
            print(output_text, end="")

    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Format Markdown tables to align columns.")
    parser.add_argument("filepath", help="Path to the markdown file to format")
    parser.add_argument("-i", "--inplace", action="store_true", help="Modify the file in-place instead of printing to stdout")

    args = parser.parse_args()

    if not os.path.exists(args.filepath):
        print(f"Error: File '{args.filepath}' does not exist.")
        return

    format_markdown_file(args.filepath, args.inplace)

if __name__ == "__main__":
    main()
