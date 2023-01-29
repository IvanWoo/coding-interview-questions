import pytest

from puzzles.group_anagrams import group_anagrams
from puzzles.utils import deep_sort


@pytest.mark.parametrize(
    "strs, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        (["a", "b", "c"], [["a"], ["b"], ["c"]]),
        (["a", "b", "c", "d"], [["a"], ["b"], ["c"], ["d"]]),
    ],
)
def test_group_anagrams(strs, expected):
    assert deep_sort(group_anagrams(strs)) == deep_sort(expected)
