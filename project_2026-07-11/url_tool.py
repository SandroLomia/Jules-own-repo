import argparse
import urllib.parse
import sys

def encode_url(text: str) -> str:
    """URL-encode the given text."""
    return urllib.parse.quote(text, safe='')

def decode_url(text: str) -> str:
    """URL-decode the given text."""
    return urllib.parse.unquote(text)

def main():
    parser = argparse.ArgumentParser(description="A simple CLI tool to URL encode or decode strings.")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--encode', action='store_true', help="URL-encode the provided string")
    group.add_argument('--decode', action='store_true', help="URL-decode the provided string")

    parser.add_argument('text', type=str, help="The string to encode or decode")

    args = parser.parse_args()

    if args.encode:
        print(encode_url(args.text))
    elif args.decode:
        print(decode_url(args.text))

if __name__ == "__main__":
    main()
