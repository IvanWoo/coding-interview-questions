import pytest

from puzzles.two_sum import two_sum


@pytest.mark.parametrize(
    "numbers, target, expected",
    [
        ([1, 2, 7, 11, 15], 9, [1, 2]),
        ([1], 2, [0, 0]),
    ],
)
def test_two_sum(numbers: list[int], target: int, expected: list[int]) -> None:
    assert two_sum(numbers, target) == expected
