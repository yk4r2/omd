import doctest


LETTER_TO_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": " ",
}

MORSE_TO_LETTER = {morse: letter for letter, morse in LETTER_TO_MORSE.items()}


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе
    >>> encode(message='SOS')
    '... --- ...'
    >>> encode(message='SOS SOS SOS') # doctest: +ELLIPSIS
    '... --- ... ... ... --- ...'
    >>> encode(message='S O S') # doctest: +NORMALIZE_WHITESPACE
    '...  ---  ...'
    >>> encode(message=1)
    Traceback (most recent call last):
    TypeError: 'int' object is not iterable
    """

    encoded_signs = [LETTER_TO_MORSE[letter] for letter in message]
    return " ".join(encoded_signs)


if __name__ == "__main__":
    doctest.testmod()
