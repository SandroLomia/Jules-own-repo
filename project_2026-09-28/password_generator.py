import string
import secrets

class PasswordGenerator:
    def __init__(self):
        pass

    def generate_password(self, length=12, use_upper=True, use_numbers=True, use_symbols=True):
        if length < 1:
            raise ValueError("Password length must be at least 1.")

        characters = list(string.ascii_lowercase)
        required_chars = [secrets.choice(string.ascii_lowercase)]

        if use_upper:
            characters.extend(list(string.ascii_uppercase))
            required_chars.append(secrets.choice(string.ascii_uppercase))
        if use_numbers:
            characters.extend(list(string.digits))
            required_chars.append(secrets.choice(string.digits))
        if use_symbols:
            # Common symbols, omitting ambiguous ones
            symbols = list("!@#$%^&*()_+~`|}{[]:;?><,./-=")
            characters.extend(symbols)
            required_chars.append(secrets.choice(symbols))

        if length < len(required_chars):
            raise ValueError(f"Password length must be at least {len(required_chars)} to satisfy the specified requirements.")

        remaining_length = length - len(required_chars)
        password_chars = required_chars + [secrets.choice(characters) for _ in range(remaining_length)]

        # Cryptographically secure shuffle
        secrets.SystemRandom().shuffle(password_chars)

        return "".join(password_chars)
