import re
import html

def convert_to_html(markdown_text: str) -> str:
    """
    Converts a subset of Markdown to HTML.
    Sanitizes the input to prevent XSS.

    Supported:
    - Headers (# to ######)
    - Bold (**text**)
    - Italic (*text*)
    - Paragraphs
    """
    if not markdown_text:
        return ""

    # Sanitize the entire text first to prevent XSS
    sanitized_text = html.escape(markdown_text)

    # Process line by line for headers and paragraphs
    lines = sanitized_text.split('\n')
    html_lines = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Headers
        header_match = re.match(r'^(#{1,6})\s+(.*)', line)
        if header_match:
            level = len(header_match.group(1))
            content = header_match.group(2)
            html_lines.append(f"<h{level}>{content}</h{level}>")
        else:
            # Paragraph
            html_lines.append(f"<p>{line}</p>")

    # Join the lines
    result = '\n'.join(html_lines)

    # Bold and Italic
    result = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', result)
    result = re.sub(r'\*(.+?)\*', r'<em>\1</em>', result)

    return result
