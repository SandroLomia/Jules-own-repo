import re
import html as html_lib

def convert_markdown_to_html(markdown_text):
    if not markdown_text:
        return ""

    # Sanitize input to prevent basic XSS
    markdown_text = html_lib.escape(markdown_text)

    # Process lines for lists and headers
    lines = markdown_text.split('\n')
    html_lines = []

    in_list = False

    for line in lines:
        # Headers
        header_match = re.match(r'^(#{1,6})\s+(.*)$', line)
        if header_match:
            if in_list:
                html_lines.append("</ul>")
                in_list = False

            level = len(header_match.group(1))
            content = header_match.group(2)
            html_lines.append(f"<h{level}>{content}</h{level}>")
            continue

        # Lists
        list_match = re.match(r'^\*\s+(.*)$', line)
        if list_match:
            if not in_list:
                html_lines.append("<ul>")
                in_list = True

            content = list_match.group(1)
            html_lines.append(f"<li>{content}</li>")
            continue

        # Normal lines
        if in_list:
            html_lines.append("</ul>")
            in_list = False

        if not in_list:
            # Only wrap in <p> if it's not empty
            if line.strip():
                html_lines.append(f"<p>{line}</p>")
            else:
                html_lines.append("")

    if in_list:
        html_lines.append("</ul>")

    html = '\n'.join(html_lines)

    # Inline formatting: Bold
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)

    # Inline formatting: Italic (handles *text* and _text_)
    # Use negative lookbehind and lookahead to not match bold
    html = re.sub(r'(?<!\*)\*(?!\*)(.*?)(?<!\*)\*(?!\*)', r'<em>\1</em>', html)
    html = re.sub(r'(?<!_)_(?!_)(.*?)(?<!_)_(?!_)', r'<em>\1</em>', html)

    return html.strip()
