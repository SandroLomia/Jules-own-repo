# Daily Project - 2026-11-11

## Overview

Today's project is a Python utility to translate text to Morse code and Morse code back to text.

## Features

- **Text to Morse Code**: Translates standard alphanumeric characters and common punctuation into Morse code.
- **Morse Code to Text**: Translates valid Morse code back into standard readable text.

## Usage

```python
from morse_code import MorseCodeTranslator

translator = MorseCodeTranslator()

# Text to Morse
morse = translator.text_to_morse("HELLO WORLD")
print(morse)
# Output: .... . .-.. .-.. --- / .-- --- .-. .-.. -..

# Morse to Text
text = translator.morse_to_text(".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
print(text)
# Output: HELLO WORLD
```

## Running Tests

To run the tests for this project, run the following command from the repository root:

```bash
PYTHONPATH=project_2026-11-11 python3 -m unittest project_2026-11-11/test_morse_code.py
```
