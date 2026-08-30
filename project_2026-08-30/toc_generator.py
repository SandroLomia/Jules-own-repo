import re
import urllib.parse

def generate_toc(markdown_text: str) -> str:
    """
    Parses Markdown text, extracts headings (levels 2-6),
    and generates a Table of Contents with indentation and anchor links.
    Skips headings inside code blocks.
    """
    toc_lines = []

    # Simple state machine to track if we're inside a code block
    in_code_block = False

    for line in markdown_text.split('\n'):
        # Check for code block markers
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        # Match headings, e.g., "## Heading 2", "### Heading 3"
        match = re.match(r'^(#{1,6})\s+(.+?)\s*$', line)
        if match:
            level = len(match.group(1))
            heading_text = match.group(2)

            # For TOC we often start at level 2 as top level
            # Adjust indentation based on level
            indent = "  " * (level - 1)

            # Generate anchor link
            # Convert to lowercase, remove punctuation, replace spaces with hyphens
            anchor = heading_text.lower()
            anchor = re.sub(r'[^\w\s-]', '', anchor)
            anchor = re.sub(r'[-\s]+', '-', anchor).strip('-')

            # Use urllib to ensure it's a valid URL fragment if needed,
            # though github style mostly just uses hyphens.

            toc_lines.append(f"{indent}- [{heading_text}](#{anchor})")

    return "\n".join(toc_lines)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            content = f.read()
        print(generate_toc(content))
    else:
        print("Usage: python3 toc_generator.py <markdown_file>")
