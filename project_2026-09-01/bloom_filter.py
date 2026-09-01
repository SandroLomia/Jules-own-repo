import hashlib
import math

class BloomFilter:
    """
    A simple probabilistic data structure that tells you if an item is definitely not in the set or possibly in the set.
    """
    def __init__(self, capacity: int, error_rate: float):
        """
        Initializes the Bloom filter.

        Args:
            capacity (int): The expected number of items to be stored.
            error_rate (float): The acceptable false positive rate (0.0 < error_rate < 1.0).
        """
        if not (0 < error_rate < 1):
            raise ValueError("Error rate must be between 0 and 1.")
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")

        # Size of bit array (m)
        self.size = self._get_size(capacity, error_rate)
        # Number of hash functions (k)
        self.hash_count = self._get_hash_count(self.size, capacity)
        # Bit array initialized to 0s
        self.bit_array = [0] * self.size

    def _get_size(self, capacity: int, error_rate: float) -> int:
        """Calculates optimal size of the bit array based on capacity and error_rate."""
        m = -(capacity * math.log(error_rate)) / (math.log(2) ** 2)
        return int(m)

    def _get_hash_count(self, size: int, capacity: int) -> int:
        """Calculates the optimal number of hash functions."""
        k = (size / capacity) * math.log(2)
        return int(k)

    def _hashes(self, item: str) -> list[int]:
        """Generates `k` hash values for a given item using cryptographic hashes to simulate multiple hashes."""
        # Using sha256 as our base hash
        base_hash = hashlib.sha256(item.encode('utf-8')).hexdigest()

        # We can simulate multiple independent hash functions by hashing the item with different seeds.
        # However, a simpler common approach is to split a large cryptographic hash or use string concatenation with index.
        hashes = []
        for i in range(self.hash_count):
            h = hashlib.sha256((item + str(i)).encode('utf-8')).hexdigest()
            hashes.append(int(h, 16) % self.size)
        return hashes

    def add(self, item: str) -> None:
        """
        Adds an item to the Bloom filter.

        Args:
            item (str): The string to add.
        """
        for i in self._hashes(item):
            self.bit_array[i] = 1

    def check(self, item: str) -> bool:
        """
        Checks if an item is in the Bloom filter.

        Args:
            item (str): The string to check.

        Returns:
            bool: True if the item is *possibly* in the set, False if it is *definitely not* in the set.
        """
        for i in self._hashes(item):
            if self.bit_array[i] == 0:
                return False
        return True
