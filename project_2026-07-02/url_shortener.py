import string
import secrets
from typing import Optional

class URLShortener:
    def __init__(self, code_length: int = 6):
        self.code_length = code_length
        self.url_map = {}
        self.reverse_map = {}
        self.alphabet = string.ascii_letters + string.digits

    def shorten_url(self, long_url: str) -> str:
        if long_url in self.reverse_map:
            return self.reverse_map[long_url]

        while True:
            short_code = ''.join(secrets.choice(self.alphabet) for _ in range(self.code_length))
            if short_code not in self.url_map:
                break

        self.url_map[short_code] = long_url
        self.reverse_map[long_url] = short_code
        return short_code

    def expand_url(self, short_code: str) -> Optional[str]:
        return self.url_map.get(short_code)
