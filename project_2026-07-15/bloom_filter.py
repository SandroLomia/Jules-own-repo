import hashlib

class BloomFilter:
    def __init__(self, size: int, hash_count: int):
        if size <= 0:
            raise ValueError("Size must be a positive integer.")
        if hash_count <= 0:
            raise ValueError("Hash count must be a positive integer.")
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [False] * size

    def _get_hashes(self, item: str):
        hashes = []
        for i in range(self.hash_count):
            # Create a unique string for each hash function
            item_with_salt = f"{i}:{item}"
            # Use SHA-256 for hashing
            digest = hashlib.sha256(item_with_salt.encode('utf-8')).hexdigest()
            # Convert hex to integer and mod by size
            hash_val = int(digest, 16) % self.size
            hashes.append(hash_val)
        return hashes

    def add(self, item: str):
        hashes = self._get_hashes(item)
        for h in hashes:
            self.bit_array[h] = True

    def check(self, item: str) -> bool:
        hashes = self._get_hashes(item)
        for h in hashes:
            if not self.bit_array[h]:
                return False
        return True
