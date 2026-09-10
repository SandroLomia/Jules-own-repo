import re

class MarkdownTOCGenerator:
    """
    A utility class to generate and inject a Table of Contents (TOC)
    into a Markdown document.
    """

    @staticmethod
    def _create_slug(header_text: str) -> str:
        """
        Creates a GitHub-flavored Markdown slug from a header text.
        """
        # Convert to lowercase
        slug = header_text.lower()
        # Remove non-word characters except spaces and hyphens
        slug = re.sub(r'[^\w\s-]', '', slug)
        # Replace spaces with hyphens
        slug = re.sub(r'[-\s]+', '-', slug)
        # Strip leading/trailing hyphens
        return slug.strip('-')

    @staticmethod
    def generate_toc(markdown_text: str) -> str:
        """
        Parses Markdown text and generates a nested Table of Contents structure.
        Code blocks (```...```) are ignored when searching for headers.
        """
        # Regex to match code blocks to ignore their contents
        code_block_pattern = re.compile(r'```.*?```', re.DOTALL)

        # Replace code blocks with placeholders so we don't parse headers inside them
        text_without_code = re.sub(code_block_pattern, '', markdown_text)

        # Regex to match Markdown headers (e.g., # Header, ## Subheader)
        header_pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)

        toc_lines = []
        for match in header_pattern.finditer(text_without_code):
            level = len(match.group(1))
            header_text = match.group(2).strip()
            slug = MarkdownTOCGenerator._create_slug(header_text)

            # Formatting for the nested list: 2 spaces per level depth, starting from level 1 (so H1 is 0 spaces, H2 is 2 spaces...)
            indent = "  " * (level - 1)
            toc_lines.append(f"{indent}- [{header_text}](#{slug})")

        return "\n".join(toc_lines)

    @staticmethod
    def inject_toc(markdown_text: str, placeholder: str = "<!-- TOC -->") -> str:
        """
        Generates a TOC for the given Markdown text and replaces the specified
        placeholder with the generated TOC. If the placeholder is not found,
        the original text is returned unchanged.
        """
        if placeholder not in markdown_text:
            return markdown_text

        toc = MarkdownTOCGenerator.generate_toc(markdown_text)
        return markdown_text.replace(placeholder, toc)
