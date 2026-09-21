def hide_message(secret_message: str, cover_text: str) -> str:
    """
    Hides a secret message within a cover text using zero-width characters.
    """
    if not secret_message:
        return cover_text

    # Encode string to UTF-8 bytes to support all characters
    utf8_bytes = secret_message.encode('utf-8')
    binary_message = ''.join(format(byte, '08b') for byte in utf8_bytes)

    zero_width_chars = {'0': '\u200B', '1': '\u200C'} # Zero-width space and Zero-width non-joiner

    hidden_part = ''.join(zero_width_chars[bit] for bit in binary_message)

    if not cover_text:
        return hidden_part
    return cover_text[0] + hidden_part + cover_text[1:]

def reveal_message(stego_text: str) -> str:
    """
    Reveals a secret message hidden within text using zero-width characters.
    """
    if not stego_text:
        return ""

    hidden_bits = []
    zero_width_to_bit = {'\u200B': '0', '\u200C': '1'}

    for char in stego_text:
        if char in zero_width_to_bit:
            hidden_bits.append(zero_width_to_bit[char])

    if not hidden_bits:
        return ""

    binary_string = ''.join(hidden_bits)

    # Read in chunks of 8 bits
    byte_array = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        if len(byte) == 8:
            byte_array.append(int(byte, 2))

    try:
        return byte_array.decode('utf-8')
    except UnicodeDecodeError:
        # If decode fails, it might not be a valid hidden message or corrupted
        return ""
