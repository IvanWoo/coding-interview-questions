import pytest

from puzzles.similar_string_groups import num_similar_groups


@pytest.mark.parametrize(
    "strs, expected",
    [
        (["tars", "rats", "arts", "star"], 2),
        (["omv", "ovm"], 1),
    ],
)
def test_num_similar_groups(strs, expected):
    assert num_similar_groups(strs) == expected
