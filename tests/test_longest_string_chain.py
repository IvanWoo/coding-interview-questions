import pytest
from puzzles.longest_string_chain import longest_str_chain


@pytest.mark.parametrize(
    "words, expected",
    [
        (["a", "b", "ba", "bca", "bda", "bdca"], 4),
        (["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], 5),
        (["abcd", "dbqca"], 1),
    ],
)
def test_longest_str_chain(words, expected):
    assert longest_str_chain(words) == expected
