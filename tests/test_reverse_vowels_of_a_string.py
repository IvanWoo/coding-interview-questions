import pytest
from puzzles.reverse_vowels_of_a_string import reverse_vowels


def test_reverse_vowels():
    assert reverse_vowels("Sore was I ere I saw Eros.") == "SorE was I ere I saw eros."
    assert reverse_vowels("aA") == "Aa"