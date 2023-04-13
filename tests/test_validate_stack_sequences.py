import pytest

from puzzles.validate_stack_sequences import validate_stack_sequences


@pytest.mark.parametrize(
    "pushed, popped, expected",
    [
        ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
        ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
        ([2, 1, 0], [1, 2, 0], True),
    ],
)
def test_validate_stack_sequences(pushed, popped, expected):
    assert validate_stack_sequences(pushed, popped) == expected
