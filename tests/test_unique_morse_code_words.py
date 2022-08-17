import pytest
from puzzles.unique_morse_code_words import unique_morse_representations


@pytest.mark.parametrize(
    "words, expected",
    [
        (["gin", "zen", "gig", "msg"], 2),
        (["a"], 1),
    ],
)
def test_unique_morse_representations(words: list[str], expected: int):
    assert unique_morse_representations(words) == expected
