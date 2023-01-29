import pytest

from puzzles.check_if_the_sentence_is_pangram import check_if_pangram


@pytest.mark.parametrize(
    "sentence, expected",
    [("thequickbrownfoxjumpsoverthelazydog", True), ("leetcode", False)],
)
def test_check_if_pangram(sentence, expected):
    assert check_if_pangram(sentence) == expected
