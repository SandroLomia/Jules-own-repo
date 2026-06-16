import base64
import hashlib
import hmac
import struct
import time

class TOTPGenerator:
    """
    A Time-based One-Time Password (TOTP) generator implementation based on RFC 6238.
    """
    def __init__(self, secret: str, digits: int = 6, interval: int = 30):
        """
        Initializes the TOTP Generator.

        :param secret: A Base32 encoded secret string.
        :param digits: The number of digits for the generated TOTP (default: 6).
        :param interval: The time step in seconds (default: 30).
        """
        self.secret = secret
        self.digits = digits
        self.interval = interval

        # Ensure the secret string is correctly padded before decoding
        padding_needed = len(self.secret) % 8
        if padding_needed != 0:
            self.secret += '=' * (8 - padding_needed)

        # Decode the base32 secret
        try:
            self.key = base64.b32decode(self.secret, casefold=True)
        except base64.binascii.Error as e:
            raise ValueError(f"Invalid Base32 secret: {e}")

    def generate_hotp(self, counter: int) -> str:
        """
        Generates an HMAC-based One-Time Password (HOTP) based on RFC 4226.

        :param counter: The counter value.
        :return: A zero-padded string representing the HOTP.
        """
        # Pack the counter into an 8-byte big-endian format
        counter_bytes = struct.pack('>Q', counter)

        # Compute the HMAC-SHA1 hash
        hmac_digest = hmac.new(self.key, counter_bytes, hashlib.sha1).digest()

        # Perform dynamic truncation (RFC 4226)
        # The offset is the lower 4 bits of the last byte of the HMAC digest
        offset = hmac_digest[-1] & 0x0F

        # Extract a 4-byte dynamic binary code
        # We drop the most significant bit (using & 0x7F) to avoid sign confusion
        code = struct.unpack('>I', hmac_digest[offset:offset+4])[0] & 0x7FFFFFFF

        # Reduce the code to the requested number of digits
        hotp = code % (10 ** self.digits)

        # Format as zero-padded string
        return str(hotp).zfill(self.digits)

    def generate(self, for_time: float = None) -> str:
        """
        Generates a TOTP for a specific time or the current time.

        :param for_time: A specific UNIX timestamp (default: current time).
        :return: The generated TOTP.
        """
        if for_time is None:
            for_time = time.time()

        # Calculate the time counter
        counter = int(for_time / self.interval)

        return self.generate_hotp(counter)

if __name__ == "__main__":
    import secrets
    # Generate a random 16-character base32 secret
    random_bytes = secrets.token_bytes(10)
    secret = base64.b32encode(random_bytes).decode('utf-8')

    print(f"Generated Secret: {secret}")
    totp = TOTPGenerator(secret)
    print(f"Current TOTP: {totp.generate()}")
