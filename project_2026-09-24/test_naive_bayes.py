import unittest
from naive_bayes import NaiveBayesClassifier

class TestNaiveBayesClassifier(unittest.TestCase):
    def setUp(self):
        self.classifier = NaiveBayesClassifier()
        self.docs = [
            "I love this sandwich.",
            "This is an amazing place!",
            "I feel very good about these beers.",
            "This is my best work.",
            "What an awesome view",
            "I do not like this restaurant",
            "I am tired of this stuff.",
            "I can't deal with this",
            "He is my sworn enemy!",
            "My boss is horrible."
        ]
        self.labels = [
            "Positive", "Positive", "Positive", "Positive", "Positive",
            "Negative", "Negative", "Negative", "Negative", "Negative"
        ]

    def test_train_updates_counts(self):
        self.classifier.train(self.docs, self.labels)

        self.assertIn("Positive", self.classifier.classes)
        self.assertIn("Negative", self.classifier.classes)
        self.assertEqual(self.classifier.total_docs, 10)
        self.assertEqual(self.classifier.class_counts["Positive"], 5)
        self.assertEqual(self.classifier.class_counts["Negative"], 5)

        # Test vocabulary building
        self.assertIn("love", self.classifier.vocab)
        self.assertIn("sandwich", self.classifier.vocab)
        self.assertIn("horrible", self.classifier.vocab)

    def test_predict_correct_class(self):
        self.classifier.train(self.docs, self.labels)

        positive_pred = self.classifier.predict("I feel very good, this is awesome!")
        self.assertEqual(positive_pred, "Positive")

        negative_pred = self.classifier.predict("I am tired and my boss is horrible")
        self.assertEqual(negative_pred, "Negative")

    def test_predict_unseen_words(self):
        self.classifier.train(self.docs, self.labels)

        # This test ensures Laplace smoothing is working (no log(0) errors)
        pred = self.classifier.predict("A completely unseen alien word xyzzy")
        # Should just return some class without throwing an error
        self.assertIn(pred, ["Positive", "Negative"])

    def test_mismatched_train_data(self):
        with self.assertRaises(ValueError):
            self.classifier.train(["Doc 1", "Doc 2"], ["Label 1"])

    def test_predict_before_train(self):
        with self.assertRaises(RuntimeError):
            self.classifier.predict("Hello world")

if __name__ == '__main__':
    unittest.main()
