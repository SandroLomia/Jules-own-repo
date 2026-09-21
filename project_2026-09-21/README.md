# Daily Project - 2026-09-21: Text Steganography

## Overview

Today's project is a Python tool for **Text Steganography**. It allows you to hide secret messages within plain text by leveraging zero-width characters, making the hidden message completely invisible to the naked eye.

This is extremely useful when you want to embed watermarks, secret tokens, or hidden messages inside normal communication channels without arousing suspicion.

## How It Works

The tool uses two specific Unicode characters that are typically invisible in standard text rendering:
1. **Zero-width space** (`\u200B`) representing the binary bit `0`.
2. **Zero-width non-joiner** (`\u200C`) representing the binary bit `1`.

The hiding process involves:
1. Converting the secret message to its UTF-8 byte representation.
2. Converting each byte into an 8-bit binary string.
3. Replacing `0`s and `1`s with their corresponding zero-width characters.
4. Injecting these invisible characters right after the first character of the cover text (so the hidden payload stays contiguous).

The revealing process is simply the reverse: extracting the invisible characters, converting them back to binary, parsing it into bytes, and decoding the bytes into a UTF-8 string.

## Usage

```python
from text_steganography import hide_message, reveal_message

# Hide a message
secret = "This is a secret message!"
cover = "This looks like a completely normal sentence."
stego_text = hide_message(secret, cover)

print(stego_text)
# Output: "This looks like a completely normal sentence." (visually identical)

# Reveal the message
revealed = reveal_message(stego_text)
print(revealed)
# Output: "This is a secret message!"
```
