# Daily Project - 2026-09-24: Naive Bayes Text Classifier

## Overview

This project implements a Multinomial Naive Bayes text classifier from scratch, utilizing only the Python standard library. It serves as an exercise in fundamental machine learning algorithms and handling raw text data.

## Architecture

The project consists of the following components:

*   **`naive_bayes.py`**: Contains the `NaiveBayesClassifier` class.
    *   **Tokenizer (`_tokenize`)**: A simple regular expression based tokenizer that converts text to lowercase and extracts words.
    *   **Training (`train`)**: Calculates the prior probabilities for each class and the conditional probabilities for each word given a class, utilizing `collections.defaultdict` for efficient counting.
    *   **Prediction (`predict`)**: Uses Bayes' theorem to calculate the log probability of a document belonging to each class, and returns the class with the highest probability. It uses `math.log` to prevent numerical underflow and implements Add-1 (Laplace) smoothing to handle unseen words.
*   **`test_naive_bayes.py`**: A comprehensive unit test suite using the `unittest` module to verify the classifier's functionality, including training logic, accurate prediction, Laplace smoothing, and edge cases (like missing training data).

## How to Run

1.  **Navigate to the project directory:**
    ```bash
    cd project_2026-09-24
    ```

2.  **Run the unit tests:**
    ```bash
    PYTHONPATH=. python3 -m unittest test_naive_bayes.py
    ```

## Example Usage

```python
from naive_bayes import NaiveBayesClassifier

classifier = NaiveBayesClassifier()

documents = [
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

labels = [
    "Positive", "Positive", "Positive", "Positive", "Positive",
    "Negative", "Negative", "Negative", "Negative", "Negative"
]

classifier.train(documents, labels)

prediction = classifier.predict("I feel very good, this is awesome!")
print(f"Prediction: {prediction}") # Output: Positive
```