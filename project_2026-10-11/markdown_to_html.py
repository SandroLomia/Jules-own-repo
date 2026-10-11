import re
import html

def convert_markdown(markdown_text: str) -> str:
    """
    Converts basic Markdown to HTML, with XSS protection.

    Supports:
    - Headers (e.g., # Header 1, ## Header 2)
    - Bold text (**text**)
    - Italic text (*text*)

    Any HTML characters in the input will be escaped to prevent XSS.
    """
    if not markdown_text:
        return ""

    # Prevent XSS by escaping HTML special characters
    safe_text = html.escape(markdown_text)

    # Process lines
    lines = safe_text.split('\n')
    processed_lines = []

    for line in lines:
        # Headers
        # Find headers (1 to 6 hash signs)
        header_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if header_match:
            level = len(header_match.group(1))
            content = header_match.group(2)
            line = f"<h{level}>{content}</h{level}>"

        # Bold text (match **text**)
        line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)

        # Italic text (match *text*)
        # Using negative lookbehind/lookahead to not match the bold ** asterisks
        line = re.sub(r'(?<!\*)\*(.+?)\*(?!\*)', r'<em>\1</em>', line)

        processed_lines.append(line)

    # Join with breaks if we want to preserve lines, but standard markdown
    # usually requires double newline for paragraph. We'll just join with newlines.
    return '\n'.join(processed_lines)
