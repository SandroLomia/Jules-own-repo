import math
import string

class PasswordAnalyzer:
    """
    Analyzes the strength of a password by calculating its Shannon entropy.
    """

    @staticmethod
    def calculate_pool_size(password):
        """
        Determines the effective character pool size based on the characters present in the password.
        """
        pool_size = 0

        has_lower = any(c in string.ascii_lowercase for c in password)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_symbol = any(c in string.punctuation for c in password)

        # Handle other unicode characters roughly
        has_other = not all(c in string.ascii_letters + string.digits + string.punctuation for c in password)

        if has_lower:
            pool_size += 26
        if has_upper:
            pool_size += 26
        if has_digit:
            pool_size += 10
        if has_symbol:
            pool_size += len(string.punctuation)
        if has_other:
            # A rough estimate for extended character sets. Can be very large.
            pool_size += 100

        # If the password is empty, pool size is 0
        if not password:
            return 0

        return pool_size

    @staticmethod
    def calculate_entropy(password):
        """
        Calculates the Shannon entropy (H = L * log2(R)) where:
        L = password length
        R = character pool size
        """
        if not password:
            return 0.0

        pool_size = PasswordAnalyzer.calculate_pool_size(password)

        if pool_size == 0:
            return 0.0

        entropy = len(password) * math.log2(pool_size)
        return round(entropy, 2)

    @staticmethod
    def categorize_strength(entropy):
        """
        Categorizes password strength based on entropy bits.
        Ranges are approximate and widely accepted guidelines.
        """
        if entropy < 28:
            return "Very Weak"
        elif entropy < 36:
            return "Weak"
        elif entropy < 60:
            return "Reasonable"
        elif entropy < 128:
            return "Strong"
        else:
            return "Very Strong"

    def analyze(self, password):
        """
        Returns a dictionary containing the entropy score and categorization.
        """
        entropy = self.calculate_entropy(password)
        strength = self.categorize_strength(entropy)

        return {
            "password_length": len(password),
            "estimated_pool_size": self.calculate_pool_size(password),
            "entropy": entropy,
            "strength": strength
        }
