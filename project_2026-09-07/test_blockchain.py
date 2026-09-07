import unittest
from blockchain import Block, Blockchain

class TestBlockchain(unittest.TestCase):
    def test_calculate_hash(self):
        block = Block(1, [{"amount": 10}], "prevhash")
        hash1 = block.calculate_hash()

        # Hash should be deterministic for the same data
        hash2 = block.calculate_hash()
        self.assertEqual(hash1, hash2)

        # Changing data should change the hash
        block.transactions = [{"amount": 20}]
        hash3 = block.calculate_hash()
        self.assertNotEqual(hash1, hash3)

    def test_create_genesis_block(self):
        blockchain = Blockchain()
        genesis_block = blockchain.chain[0]

        self.assertEqual(genesis_block.index, 0)
        self.assertEqual(genesis_block.previous_hash, "0")
        self.assertEqual(genesis_block.transactions, ["Genesis Block"])
        self.assertEqual(len(blockchain.chain), 1)

    def test_add_block(self):
        blockchain = Blockchain(difficulty=1)
        new_block = Block(1, [{"sender": "Alice", "receiver": "Bob", "amount": 5}])
        blockchain.add_block(new_block)

        self.assertEqual(len(blockchain.chain), 2)
        self.assertEqual(blockchain.get_latest_block().index, 1)

        # Verify block was linked correctly
        genesis_block = blockchain.chain[0]
        added_block = blockchain.chain[1]
        self.assertEqual(added_block.previous_hash, genesis_block.hash)

    def test_is_chain_valid(self):
        blockchain = Blockchain(difficulty=1)
        blockchain.add_block(Block(1, [{"amount": 5}]))
        blockchain.add_block(Block(2, [{"amount": 10}]))

        self.assertTrue(blockchain.is_chain_valid())

    def test_invalid_chain_tampered_data(self):
        blockchain = Blockchain(difficulty=1)
        blockchain.add_block(Block(1, [{"amount": 5}]))
        blockchain.add_block(Block(2, [{"amount": 10}]))

        self.assertTrue(blockchain.is_chain_valid())

        # Tamper with the chain
        blockchain.chain[1].transactions = [{"amount": 500}]

        # The chain should now be invalid because the hash won't match the tampered data
        self.assertFalse(blockchain.is_chain_valid())

        # Even if we recalculate the tampered block's hash...
        blockchain.chain[1].hash = blockchain.chain[1].calculate_hash()

        # The chain should STILL be invalid because the next block's previous_hash won't match
        self.assertFalse(blockchain.is_chain_valid())

if __name__ == '__main__':
    unittest.main()
