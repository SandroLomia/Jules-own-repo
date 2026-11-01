import html
import re

class MarkdownConverter:
    """
    A simple Markdown to HTML converter that supports headers, bold, italic,
    and paragraphs, with built-in XSS protection via HTML escaping.
    """

    def __init__(self):
        # Regular expressions for markdown parsing
        self.rules = [
            # Headers
            (re.compile(r'^######\s+(.*)$', re.MULTILINE), r'<h6>\1</h6>'),
            (re.compile(r'^#####\s+(.*)$', re.MULTILINE), r'<h5>\1</h5>'),
            (re.compile(r'^####\s+(.*)$', re.MULTILINE), r'<h4>\1</h4>'),
            (re.compile(r'^###\s+(.*)$', re.MULTILINE), r'<h3>\1</h3>'),
            (re.compile(r'^##\s+(.*)$', re.MULTILINE), r'<h2>\1</h2>'),
            (re.compile(r'^#\s+(.*)$', re.MULTILINE), r'<h1>\1</h1>'),
            # Bold
            (re.compile(r'\*\*(.+?)\*\*'), r'<strong>\1</strong>'),
            (re.compile(r'__(.+?)__'), r'<strong>\1</strong>'),
            # Italic
            (re.compile(r'\*(.+?)\*'), r'<em>\1</em>'),
            (re.compile(r'_(.+?)_'), r'<em>\1</em>'),
        ]

    def convert(self, markdown_text: str) -> str:
        """
        Converts a markdown string to HTML.
        """
        if not markdown_text:
            return ""

        # Sanitize input to prevent XSS
        sanitized_text = html.escape(markdown_text)

        # Apply inline and block formatting rules
        html_text = sanitized_text
        for pattern, replacement in self.rules:
            html_text = pattern.sub(replacement, html_text)

        # Process paragraphs
        blocks = re.split(r'\n\s*\n', html_text)
        formatted_blocks = []
        for block in blocks:
            block = block.strip()
            if not block:
                continue
            # If the block is already wrapped in a block-level tag (like a header), don't wrap in <p>
            if re.match(r'^<h[1-6]>.*</h[1-6]>$', block):
                formatted_blocks.append(block)
            else:
                # Replace single newlines with <br> inside paragraphs if desired,
                # but standard markdown treats single newlines as space. Let's just wrap in <p>.
                # We'll just wrap the block in <p>
                formatted_blocks.append(f'<p>{block}</p>')

        return '\n'.join(formatted_blocks)
