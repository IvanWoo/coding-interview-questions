import pytest

from puzzles.concatenated_words import find_all_concatenated_words_in_a_dict


@pytest.mark.parametrize(
    "words, expected",
    [
        (
            [
                "cat",
                "cats",
                "catsdogcats",
                "dog",
                "dogcatsdog",
                "hippopotamuses",
                "rat",
                "ratcatdogcat",
            ],
            ["catsdogcats", "dogcatsdog", "ratcatdogcat"],
        ),
        (["cat", "dog", "catdog"], ["catdog"]),
    ],
)
def test_find_all_concatenated_words_in_a_dict(words, expected):
    assert sorted(find_all_concatenated_words_in_a_dict(words)) == sorted(expected)
