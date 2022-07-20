import pytest
from puzzles.number_of_matching_subsequences import num_matching_subseq


@pytest.mark.parametrize(
    "s, words, expected",
    [
        ("abcde", ["a", "bb", "acd", "ace"], 3),
        ("dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"], 2),
        ("", ["a", "b", "c"], 0),
        ("abc", ["a", "b", "c"], 3),
    ],
)
def test_num_matching_subseq(s: str, words: list[str], expected: int):
    assert num_matching_subseq(s, words) == expected
