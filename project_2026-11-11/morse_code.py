class MorseCodeTranslator:
    """A class to translate text to Morse code and vice versa."""

    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-',
        ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
        '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
        ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
        '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
        '@': '.--.-.'
    }

    # Create the reverse dictionary for decoding
    REVERSE_MORSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

    def text_to_morse(self, text: str) -> str:
        """
        Translates normal text to Morse code.
        Words are separated by " / " and letters are separated by a space.
        Unsupported characters are ignored.
        """
        if not text:
            return ""

        words = text.strip().upper().split()
        morse_words = []

        for word in words:
            morse_chars = []
            for char in word:
                if char in self.MORSE_CODE_DICT:
                    morse_chars.append(self.MORSE_CODE_DICT[char])
            if morse_chars:
                morse_words.append(' '.join(morse_chars))

        return ' / '.join(morse_words)

    def morse_to_text(self, morse_code: str) -> str:
        """
        Translates Morse code back to text.
        Expects words to be separated by " / " and letters by a space.
        """
        if not morse_code:
            return ""

        morse_words = morse_code.strip().split(' / ')
        text_words = []

        for morse_word in morse_words:
            text_chars = []
            for char in morse_word.split():
                if char in self.REVERSE_MORSE_DICT:
                    text_chars.append(self.REVERSE_MORSE_DICT[char])
                else:
                    text_chars.append('?') # Add placeholder for unknown morse
            if text_chars:
                text_words.append(''.join(text_chars))

        return ' '.join(text_words)
