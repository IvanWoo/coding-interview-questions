import pytest

from puzzles.construct_target_array_with_multiple_sums import is_possible


@pytest.mark.parametrize(
    "target, expected",
    [
        ([9, 3, 5], True),
        ([17, 3, 5], True),
        ([1, 1, 1, 2], False),
        ([2], False),
        ([8, 5], True),
        ([1, 1000000000], True),
        ([2, 900000002], False),
    ],
)
def test_is_possible(target, expected):
    assert is_possible(target) == expected
