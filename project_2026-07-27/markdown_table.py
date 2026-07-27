def json_to_markdown_table(data: list[dict]) -> str:
    """
    Converts a list of dictionaries into a Markdown table.

    Args:
        data: A list of dictionaries representing the rows of the table.
              All dictionaries should ideally have the same keys, but the
              function uses the keys of the first dictionary as headers.

    Returns:
        A string representing the Markdown table. Returns an empty string if data is empty.
    """
    if not data:
        return ""

    headers = list(data[0].keys())

    # Create the header row
    header_row = "| " + " | ".join(headers) + " |"

    # Create the separator row
    separator_row = "| " + " | ".join(["---"] * len(headers)) + " |"

    # Create the data rows
    data_rows = []
    for item in data:
        row_values = []
        for header in headers:
            # Handle missing keys by putting an empty string
            val = item.get(header, "")
            # Convert value to string and escape pipe characters if any
            val_str = str(val).replace("|", "\\|")
            row_values.append(val_str)
        data_rows.append("| " + " | ".join(row_values) + " |")

    # Combine all parts
    table_lines = [header_row, separator_row] + data_rows
    return "\n".join(table_lines)


def markdown_table_to_json(markdown_table: str) -> list[dict]:
    """
    Parses a Markdown table string and returns a list of dictionaries.

    Args:
        markdown_table: A string containing a Markdown table.

    Returns:
        A list of dictionaries representing the rows of the table.
    """
    if not markdown_table or not markdown_table.strip():
        return []

    lines = markdown_table.strip().split('\n')
    if len(lines) < 2: # Need at least header and separator
        return []

    # Parse headers
    header_line = lines[0].strip()
    # Remove leading and trailing pipes
    if header_line.startswith('|'):
        header_line = header_line[1:]
    if header_line.endswith('|'):
        header_line = header_line[:-1]

    headers = [col.strip() for col in header_line.split('|')]

    # The second line is the separator, we skip it

    data = []
    # Parse data rows
    for line in lines[2:]:
        line = line.strip()
        if not line:
            continue

        if line.startswith('|'):
            line = line[1:]
        if line.endswith('|'):
            line = line[:-1]

        # We need to split by | but ignore escaped ones (\|)
        # A simple split might break on escaped pipes, so we handle it manually
        raw_values = line.split('|')
        values = []
        i = 0
        while i < len(raw_values):
            val = raw_values[i]
            # Check if the previous part ended with an escape character
            # In split by '|', a part ending in '\' means the '|' was escaped
            while val.endswith('\\') and i + 1 < len(raw_values):
                val = val[:-1] + '|' + raw_values[i+1]
                i += 1
            values.append(val.strip())
            i += 1

        # Pad values with empty strings if there are fewer values than headers
        while len(values) < len(headers):
            values.append("")

        # Create dict for the row
        row_dict = {}
        for i, header in enumerate(headers):
            # Only use values up to the number of headers
            if i < len(values):
                # Try to parse as int/float/boolean if possible, otherwise keep as string
                val = values[i]

                # We could try to convert types, but since markdown table content is
                # inherently string-based, it's safer to keep them as strings
                # unless they look like standard json types

                # Basic type coercion for common cases
                if val.lower() == 'true':
                    row_dict[header] = True
                elif val.lower() == 'false':
                    row_dict[header] = False
                elif val.lower() == 'null' or val == '':
                    row_dict[header] = None if val.lower() == 'null' else ""
                else:
                    try:
                        if '.' in val:
                            row_dict[header] = float(val)
                        else:
                            row_dict[header] = int(val)
                    except ValueError:
                        # Keep as string and restore escaped pipes
                        row_dict[header] = val
            else:
                row_dict[header] = ""

        data.append(row_dict)

    return data
