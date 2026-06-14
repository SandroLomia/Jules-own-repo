import unittest
from secret_santa import generate_pairs

class TestSecretSanta(unittest.TestCase):
    def test_minimum_two_names(self):
        """Test that passing fewer than 2 names raises a ValueError."""
        with self.assertRaises(ValueError):
            generate_pairs([])
        with self.assertRaises(ValueError):
            generate_pairs(["Alice"])

    def test_duplicate_names(self):
        """Test that passing duplicate names raises a ValueError."""
        with self.assertRaises(ValueError):
            generate_pairs(["Alice", "Bob", "Alice"])

    def test_valid_pairing(self):
        """Test that pairing generates a valid mapping and no one gets themselves."""
        names = ["Alice", "Bob", "Charlie", "David", "Eve"]
        for _ in range(10): # Run multiple times due to randomness
            pairs = generate_pairs(names)

            # Everyone should be a giver and receiver exactly once
            self.assertEqual(set(pairs.keys()), set(names))
            self.assertEqual(set(pairs.values()), set(names))

            # No one should get themselves
            for giver, receiver in pairs.items():
                self.assertNotEqual(giver, receiver)

    def test_pair_length_2(self):
        """Test the edge case of exactly two participants."""
        names = ["Alice", "Bob"]
        pairs = generate_pairs(names)
        self.assertEqual(pairs["Alice"], "Bob")
        self.assertEqual(pairs["Bob"], "Alice")

if __name__ == "__main__":
    unittest.main()
