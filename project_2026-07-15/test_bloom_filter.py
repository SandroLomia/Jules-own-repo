import unittest
from bloom_filter import BloomFilter
import secrets

class TestBloomFilter(unittest.TestCase):
    def test_add_and_check(self):
        bf = BloomFilter(size=1000, hash_count=5)

        # Test adding strings
        bf.add("apple")
        bf.add("banana")
        bf.add("cherry")

        self.assertTrue(bf.check("apple"))
        self.assertTrue(bf.check("banana"))
        self.assertTrue(bf.check("cherry"))

        # Elements not added should likely be False (though false positives are possible, with this size/count and small input set, it's very unlikely)
        self.assertFalse(bf.check("grape"))
        self.assertFalse(bf.check("orange"))

    def test_false_positives(self):
        bf = BloomFilter(size=100, hash_count=2)

        # Fill it up a bit
        for i in range(20):
            bf.add(f"item_{i}")

        # Check false positive rate
        false_positives = 0
        trials = 1000
        for i in range(trials):
            # random string using secrets
            random_str = secrets.token_hex(8)
            if bf.check(random_str):
                false_positives += 1

        # With size 100, hash count 2, and 20 items, FP rate should be roughly (1 - e^(-2*20/100))^2 = (1 - e^-0.4)^2 ≈ (1 - 0.67)^2 ≈ 0.33^2 ≈ 0.11 or 11%
        # So false_positives should be around 110. Let's just assert it's somewhat small but > 0
        self.assertGreater(false_positives, 0)
        self.assertLess(false_positives, trials * 0.5)

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            BloomFilter(size=0, hash_count=5)

        with self.assertRaises(ValueError):
            BloomFilter(size=-10, hash_count=5)

        with self.assertRaises(ValueError):
            BloomFilter(size=100, hash_count=0)

if __name__ == '__main__':
    unittest.main()
