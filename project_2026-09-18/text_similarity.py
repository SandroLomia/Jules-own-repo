import math
import collections
import re

class TextSimilarity:
    """
    A utility for calculating the cosine similarity between two texts.
    It uses simple tokenization and word frequencies to represent text
    as vectors, and calculates the cosine of the angle between them.
    """

    @staticmethod
    def _tokenize(text: str) -> list[str]:
        """
        Tokenizes the input string by making it lowercase and extracting words.
        """
        if not text:
            return []
        # Convert to lowercase and find all alphanumeric sequences
        return re.findall(r'\b\w+\b', text.lower())

    @staticmethod
    def _get_word_frequencies(tokens: list[str]) -> dict[str, int]:
        """
        Calculates the frequency of each word in the token list.
        """
        return dict(collections.Counter(tokens))

    @staticmethod
    def compute_cosine_similarity(text1: str, text2: str) -> float:
        """
        Computes the cosine similarity between two strings based on their word frequencies.
        Returns a float between 0.0 (completely dissimilar) and 1.0 (identical).
        """
        tokens1 = TextSimilarity._tokenize(text1)
        tokens2 = TextSimilarity._tokenize(text2)

        # If both are empty or don't have valid words, they are either perfectly identical or we can't compare
        if not tokens1 and not tokens2:
            return 1.0
        if not tokens1 or not tokens2:
            return 0.0

        freq1 = TextSimilarity._get_word_frequencies(tokens1)
        freq2 = TextSimilarity._get_word_frequencies(tokens2)

        # All unique words across both texts
        all_words = set(freq1.keys()).union(set(freq2.keys()))

        # Dot product
        dot_product = sum(freq1.get(word, 0) * freq2.get(word, 0) for word in all_words)

        # Magnitudes
        magnitude1 = math.sqrt(sum(freq1.get(word, 0)**2 for word in all_words))
        magnitude2 = math.sqrt(sum(freq2.get(word, 0)**2 for word in all_words))

        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0

        return dot_product / (magnitude1 * magnitude2)
