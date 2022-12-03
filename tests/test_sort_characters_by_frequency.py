import pytest
from puzzles.sort_characters_by_frequency import frequency_sort


@pytest.mark.parametrize(
    "s, expected",
    [
        ("tree", ["eert", "eetr"]),
        ("cccaaa", ["aaaccc", "cccaaa"]),
        ("Aabb", ["bbAa", "bbaA"]),
    ],
)
def test_frequency_sort(s, expected):
    assert frequency_sort(s) in expected
