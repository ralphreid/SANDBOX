from string import ascii_lowercase
from string import punctuation


def is_pangram(sentence):
    if not sentence:
        return False
    else:
        alphabet = set(ascii_lowercase)
        sentence = sentence.lower()
        tr = str.maketrans("", "", punctuation)
        sentence = sentence.translate(tr)
        return set(sentence) >= alphabet
