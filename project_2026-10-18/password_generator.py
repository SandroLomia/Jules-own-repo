import secrets
import string

class SecurePasswordGenerator:
    def __init__(self, include_uppercase=True, include_lowercase=True, include_digits=True, include_special=True):
        self.include_uppercase = include_uppercase
        self.include_lowercase = include_lowercase
        self.include_digits = include_digits
        self.include_special = include_special

    def generate_password(self, length=12):
        if length < 4:
            raise ValueError("Password length must be at least 4")

        character_sets = []
        if self.include_uppercase:
            character_sets.append(string.ascii_uppercase)
        if self.include_lowercase:
            character_sets.append(string.ascii_lowercase)
        if self.include_digits:
            character_sets.append(string.digits)
        if self.include_special:
            character_sets.append(string.punctuation)

        if not character_sets:
            raise ValueError("At least one character set must be included")

        # Ensure at least one character from each selected set is included
        password = []
        for char_set in character_sets:
            password.append(secrets.choice(char_set))

        # Fill the rest of the password
        all_chars = ''.join(character_sets)
        for _ in range(length - len(password)):
            password.append(secrets.choice(all_chars))

        # Shuffle the password to make it unpredictable
        # Using secrets.SystemRandom() instead of standard random.shuffle for cryptographic security
        sys_random = secrets.SystemRandom()
        sys_random.shuffle(password)

        return ''.join(password)

    def evaluate_strength(self, password):
        length = len(password)
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)

        score = 0
        if length >= 12:
            score += 2
        elif length >= 8:
            score += 1

        if has_upper and has_lower:
            score += 1
        if has_digit:
            score += 1
        if has_special:
            score += 1

        if score >= 4:
            return "Strong"
        elif score >= 2:
            return "Medium"
        else:
            return "Weak"
