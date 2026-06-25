import unittest
from entropy_analyzer import PasswordAnalyzer

class TestPasswordAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = PasswordAnalyzer()

    def test_empty_password(self):
        result = self.analyzer.analyze("")
        self.assertEqual(result["entropy"], 0.0)
        self.assertEqual(result["estimated_pool_size"], 0)
        self.assertEqual(result["strength"], "Very Weak")

    def test_only_lowercase(self):
        # Pool size = 26. Log2(26) ~= 4.7
        # 10 chars -> entropy ~= 47
        result = self.analyzer.analyze("helloworld")
        self.assertEqual(result["estimated_pool_size"], 26)
        self.assertTrue(46 < result["entropy"] < 48)

    def test_mixed_case_and_numbers(self):
        # Pool size = 26 + 26 + 10 = 62. Log2(62) ~= 5.95
        # 10 chars -> entropy ~= 59.5
        result = self.analyzer.analyze("HelloWorld1")
        self.assertEqual(result["estimated_pool_size"], 62)
        self.assertTrue(59 < result["entropy"] < 66)

    def test_very_strong_password(self):
        result = self.analyzer.analyze("A1!b2@C3#d4$E5%f6^g7&H8*i9(J0)")
        self.assertEqual(result["strength"], "Very Strong")

    def test_very_weak_password(self):
        result = self.analyzer.analyze("abc")
        self.assertEqual(result["strength"], "Very Weak")

if __name__ == '__main__':
    unittest.main()
