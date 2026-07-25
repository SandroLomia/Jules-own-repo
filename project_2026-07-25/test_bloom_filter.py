import unittest
import secrets
import string
from bloom_filter import BloomFilter

class TestBloomFilter(unittest.TestCase):
    def test_add_and_check(self):
        bf = BloomFilter(capacity=1000, error_rate=0.01)
        items_to_add = ["apple", "banana", "cherry", "date", "elderberry"]

        # Initially, shouldn't contain items
        for item in items_to_add:
            self.assertFalse(item in bf)

        # Add items
        for item in items_to_add:
            bf.add(item)

        # Now, should contain items
        for item in items_to_add:
            self.assertTrue(item in bf)

    def test_false_positive_rate(self):
        capacity = 10000
        target_error_rate = 0.05
        bf = BloomFilter(capacity=capacity, error_rate=target_error_rate)

        # Generate some random strings to insert
        def generate_random_string(length=10):
            chars = string.ascii_letters + string.digits
            return ''.join(secrets.choice(chars) for _ in range(length))

        inserted_items = set(generate_random_string() for _ in range(capacity))

        for item in inserted_items:
            bf.add(item)

        # Verify all inserted items are present
        for item in inserted_items:
            self.assertTrue(item in bf)

        # Generate new items to test false positive rate
        test_size = 10000
        test_items = set()
        while len(test_items) < test_size:
            item = generate_random_string()
            if item not in inserted_items:
                test_items.add(item)

        false_positives = 0
        for item in test_items:
            if item in bf:
                false_positives += 1

        actual_error_rate = false_positives / test_size

        # The actual error rate should be close to the target error rate.
        # We use a loose bound for probabilistic testing, checking it doesn't exceed target * 1.5
        self.assertLessEqual(actual_error_rate, target_error_rate * 1.5)

    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            BloomFilter(capacity=-10, error_rate=0.01)

        with self.assertRaises(ValueError):
            BloomFilter(capacity=0, error_rate=0.01)

        with self.assertRaises(ValueError):
            BloomFilter(capacity=1000, error_rate=-0.5)

        with self.assertRaises(ValueError):
            BloomFilter(capacity=1000, error_rate=1.5)

        with self.assertRaises(ValueError):
            BloomFilter(capacity=1000, error_rate=0)

        with self.assertRaises(ValueError):
            BloomFilter(capacity=1000, error_rate=1)

if __name__ == '__main__':
    unittest.main()
