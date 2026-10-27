import unittest
from unittest.mock import patch, MagicMock
import os
import tempfile
import urllib.request
from urllib.error import HTTPError

from markdown_link_checker import (
    extract_links,
    validate_url,
    validate_file_path,
    check_markdown_links
)

class TestMarkdownLinkChecker(unittest.TestCase):

    def test_extract_links(self):
        markdown = """
        Here is a [Google](https://google.com) link.
        And here is an [Internal File](./README.md).
        Check out [this anchor](#section).
        """
        links = extract_links(markdown)
        expected = [
            ('Google', 'https://google.com'),
            ('Internal File', './README.md'),
            ('this anchor', '#section')
        ]
        self.assertEqual(links, expected)

    def test_extract_no_links(self):
        markdown = "This text has no links."
        links = extract_links(markdown)
        self.assertEqual(links, [])

    @patch('urllib.request.urlopen')
    def test_validate_url_success(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        # When used as a context manager (with urlopen as response)
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        self.assertTrue(validate_url("https://example.com"))

    @patch('urllib.request.urlopen')
    def test_validate_url_failure(self, mock_urlopen):
        # Setup mock to raise an HTTPError (e.g. 404)
        mock_urlopen.side_effect = HTTPError("url", 404, "Not Found", {}, None)

        self.assertFalse(validate_url("https://example.com/notfound"))

    @patch('urllib.request.urlopen')
    def test_validate_url_exception(self, mock_urlopen):
        # Test generic exception handling
        mock_urlopen.side_effect = Exception("Unknown error")
        self.assertFalse(validate_url("https://example.com"))

    def test_validate_internal_file_exists(self):
        # Create a temporary file to test
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_path = tmp_file.name

        try:
            # Test full path
            self.assertTrue(validate_file_path(tmp_path, base_dir=""))
            # Test relative path by passing the directory as base_dir and filename as path
            base_dir, filename = os.path.split(tmp_path)
            self.assertTrue(validate_file_path(filename, base_dir=base_dir))
        finally:
            os.remove(tmp_path)

    def test_validate_internal_file_missing(self):
        self.assertFalse(validate_file_path("non_existent_file_123.md", base_dir="."))

    def test_validate_anchor_link(self):
        # An anchor link like "#section" should be considered valid internally
        self.assertTrue(validate_file_path("#section", base_dir="."))

        # A file with an anchor like "file.md#section" should validate the file part
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_path = tmp_file.name

        try:
            base_dir, filename = os.path.split(tmp_path)
            self.assertTrue(validate_file_path(f"{filename}#anchor", base_dir=base_dir))
        finally:
            os.remove(tmp_path)

    @patch('markdown_link_checker.validate_url')
    def test_check_markdown_links(self, mock_validate_url):
        # Mock external URL validation to avoid real network requests
        def side_effect(url):
            return url == "https://valid.com"
        mock_validate_url.side_effect = side_effect

        markdown = """
        [Valid Ext](https://valid.com)
        [Invalid Ext](https://invalid.com)
        [Valid Int](valid_test.md)
        [Invalid Int](missing_test.md)
        [Email](mailto:test@example.com)
        """

        # We need a fake valid file for the internal test
        with tempfile.TemporaryDirectory() as tmp_dir:
            valid_file_path = os.path.join(tmp_dir, "valid_test.md")
            with open(valid_file_path, "w") as f:
                f.write("test")

            results = check_markdown_links(markdown, base_dir=tmp_dir)

            self.assertIn(('Valid Ext', 'https://valid.com'), results['valid'])
            self.assertIn(('Valid Int', 'valid_test.md'), results['valid'])
            self.assertIn(('Email', 'mailto:test@example.com'), results['valid'])

            self.assertIn(('Invalid Ext', 'https://invalid.com'), results['invalid'])
            self.assertIn(('Invalid Int', 'missing_test.md'), results['invalid'])

if __name__ == '__main__':
    unittest.main()
