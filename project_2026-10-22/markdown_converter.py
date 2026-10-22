import html
import re

def convert_to_html(markdown_text: str) -> str:
    """
    Converts basic markdown elements to HTML and sanitizes the input.
    """
    if not isinstance(markdown_text, str):
        raise TypeError("Input must be a string")

    # Sanitize the input to prevent XSS
    sanitized_text = html.escape(markdown_text)

    lines = sanitized_text.split('\n')
    html_lines = []

    for line in lines:
        # Convert headers (h1 to h6)
        header_match = re.match(r'^(#{1,6})\s+(.*)$', line)
        if header_match:
            level = len(header_match.group(1))
            text = header_match.group(2)
            line = f"<h{level}>{text}</h{level}>"

        # Convert bold text (**text** or __text__)
        line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
        line = re.sub(r'__(.*?)__', r'<b>\1</b>', line)

        # Convert italic text (*text* or _text_)
        line = re.sub(r'\*([^\*]+)\*', r'<i>\1</i>', line)
        line = re.sub(r'_([^_]+)_', r'<i>\1</i>', line)

        # Paragraphs (simple lines without headers)
        if not header_match and line.strip() != "":
            # Wrap simple text in paragraph if it doesn't already have tags
            # (Very basic paragraph handling)
            line = f"<p>{line}</p>"
        elif line.strip() == "":
            line = "" # Skip empty lines for simplicity or keep them as blank

        if line.strip():
            html_lines.append(line)

    return '\n'.join(html_lines)
