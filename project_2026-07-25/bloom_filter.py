import math
import hashlib

class BloomFilter:
    """
    A simple, space-efficient probabilistic data structure.
    """

    def __init__(self, capacity: int, error_rate: float):
        """
        Initializes the BloomFilter.

        Args:
            capacity: The expected number of items to be inserted.
            error_rate: The desired false positive rate (0 < error_rate < 1).
        """
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0.")
        if error_rate <= 0 or error_rate >= 1:
            raise ValueError("Error rate must be between 0 and 1 exclusive.")

        self.capacity = capacity
        self.error_rate = error_rate

        self.size = self._get_size(capacity, error_rate)
        self.hash_count = self._get_hash_count(self.size, capacity)

        # Initialize the bit array as a single large integer for memory efficiency in Python
        self.bit_array = 0
        self.inserted_count = 0

    def _get_size(self, capacity: int, error_rate: float) -> int:
        """
        Calculates the required size of the bit array based on capacity and error rate.
        Formula: m = -(n * ln(p)) / (ln(2)^2)
        """
        m = -(capacity * math.log(error_rate)) / (math.log(2) ** 2)
        return int(math.ceil(m))

    def _get_hash_count(self, size: int, capacity: int) -> int:
        """
        Calculates the optimal number of hash functions to use.
        Formula: k = (m / n) * ln(2)
        """
        k = (size / capacity) * math.log(2)
        return max(1, int(math.ceil(k)))

    def _get_hashes(self, item: str) -> list[int]:
        """
        Generates 'hash_count' distinct hash values for the given item.
        Uses double hashing technique.
        """
        # Create two base hash values using SHA256 (split in half)
        hash_bytes = hashlib.sha256(item.encode('utf-8')).digest()
        # Take first 16 bytes for hash1, last 16 for hash2
        hash1 = int.from_bytes(hash_bytes[:16], byteorder='big')
        hash2 = int.from_bytes(hash_bytes[16:], byteorder='big')

        # Generate 'k' hashes using h(i) = (hash1 + i * hash2) % size
        hashes = []
        for i in range(self.hash_count):
            h = (hash1 + i * hash2) % self.size
            hashes.append(h)
        return hashes

    def add(self, item: str) -> None:
        """
        Adds an item to the Bloom filter.
        """
        hashes = self._get_hashes(item)
        for h in hashes:
            # Set the h-th bit to 1
            self.bit_array |= (1 << h)
        self.inserted_count += 1

    def __contains__(self, item: str) -> bool:
        """
        Checks if an item might be in the Bloom filter.
        Returns True if it might be, False if it definitely is not.
        """
        hashes = self._get_hashes(item)
        for h in hashes:
            # Check if the h-th bit is 0
            if (self.bit_array & (1 << h)) == 0:
                return False
        return True
