import math
from collections import defaultdict
import re

class NaiveBayesClassifier:
    """
    A Naive Bayes text classifier utilizing only the Python standard library.
    Implements Multinomial Naive Bayes suitable for text classification.
    """

    def __init__(self):
        self.classes = []
        self.class_word_counts = defaultdict(lambda: defaultdict(int))
        self.class_counts = defaultdict(int)
        self.vocab = set()
        self.total_docs = 0

    def _tokenize(self, text):
        """Simple tokenizer to lowercase and extract words."""
        text = str(text).lower()
        # Find all sequences of alphanumeric characters
        return re.findall(r'\b\w+\b', text)

    def train(self, documents, labels):
        """
        Trains the Naive Bayes classifier.

        Args:
            documents (list of str): The training text documents.
            labels (list of str): The corresponding labels for the documents.
        """
        if len(documents) != len(labels):
            raise ValueError("Number of documents must match number of labels.")

        for text, label in zip(documents, labels):
            if label not in self.classes:
                self.classes.append(label)

            self.class_counts[label] += 1
            self.total_docs += 1

            words = self._tokenize(text)
            for word in words:
                self.class_word_counts[label][word] += 1
                self.vocab.add(word)

    def predict(self, text):
        """
        Predicts the class of the given text.

        Args:
            text (str): The text to classify.

        Returns:
            str: The predicted class label.
        """
        if not self.classes:
            raise RuntimeError("Model has not been trained yet.")

        words = self._tokenize(text)

        best_class = None
        max_log_prob = -float('inf')

        vocab_size = len(self.vocab)

        for c in self.classes:
            # P(c)
            prob_c = self.class_counts[c] / self.total_docs
            log_prob = math.log(prob_c)

            # Total words in class c
            total_words_in_c = sum(self.class_word_counts[c].values())

            for word in words:
                # Add-1 Laplace smoothing for P(w|c)
                word_count_in_c = self.class_word_counts[c].get(word, 0)
                prob_w_given_c = (word_count_in_c + 1) / (total_words_in_c + vocab_size)
                log_prob += math.log(prob_w_given_c)

            if log_prob > max_log_prob:
                max_log_prob = log_prob
                best_class = c

        return best_class
