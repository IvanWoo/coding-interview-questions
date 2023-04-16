import pytest

from puzzles.number_of_ways_to_form_a_target_string_given_a_dictionary import num_ways


@pytest.mark.parametrize(
    "words, target, expected",
    [
        (["acca", "bbbb", "caca"], "aba", 6),
        (["abba", "baab"], "bab", 4),
        (["babb", "aaaa"], "aa", 9),
    ],
)
def test_num_ways(words, target, expected):
    assert num_ways(words, target) == expected
