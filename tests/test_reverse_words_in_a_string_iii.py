import pytest
from puzzles.reverse_words_in_a_string_iii import reverse_words


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
        ("God Ding", "doG gniD"),
    ],
)
def test_reverse_words(s, expected):
    assert reverse_words(s) == expected
