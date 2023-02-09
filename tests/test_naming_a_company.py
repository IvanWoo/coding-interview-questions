import pytest

from puzzles.naming_a_company import distinct_names


@pytest.mark.parametrize(
    "ideas, expected",
    [
        (["coffee", "donuts", "time", "toffee"], 6),
        (["lack", "back"], 0),
    ],
)
def test_distinct_names(ideas, expected):
    assert distinct_names(ideas) == expected
