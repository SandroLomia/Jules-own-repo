import re
import os
import urllib.request
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse

def extract_links(markdown_content):
    """
    Extracts all links from the given markdown content.
    Returns a list of tuples: (text, url)
    """
    # Matches [text](url) format
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.findall(pattern, markdown_content)

def validate_url(url):
    """
    Validates an external URL using a HEAD request.
    Returns True if reachable (status < 400), False otherwise.
    """
    try:
        # Some servers block Python-urllib user agent, so we add a generic one
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        # We try a GET request if HEAD is not supported by the server, but default to HEAD for efficiency
        req.get_method = lambda: 'HEAD'

        with urllib.request.urlopen(req, timeout=10) as response:
            return response.status < 400
    except (HTTPError, URLError, ValueError):
        return False
    except Exception:
        return False

def validate_file_path(path, base_dir="."):
    """
    Validates if an internal file path exists relative to the base_dir.
    """
    # Remove fragment/hash from internal links if present (e.g. file.md#section)
    clean_path = path.split('#')[0]

    # If the path is empty after splitting, it was just a local fragment like '#section'
    if not clean_path:
        return True

    full_path = os.path.join(base_dir, clean_path)
    return os.path.exists(full_path)

def check_markdown_links(content, base_dir="."):
    """
    Extracts and checks all links in the given markdown content.
    Returns a dictionary of valid and invalid links.
    """
    links = extract_links(content)
    results = {
        'valid': [],
        'invalid': []
    }

    for text, link in links:
        parsed = urlparse(link)

        # Check if it's an external URL (http/https)
        if parsed.scheme in ('http', 'https'):
            is_valid = validate_url(link)
        # Check if it's an email link (mailto)
        elif parsed.scheme == 'mailto':
             # We won't validate emails rigorously, assume valid format is okay
            is_valid = True
        # Assume internal file path
        else:
            is_valid = validate_file_path(link, base_dir)

        if is_valid:
            results['valid'].append((text, link))
        else:
            results['invalid'].append((text, link))

    return results
