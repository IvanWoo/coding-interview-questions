import pytest
from puzzles.stamping_the_sequence import moves_to_stamp, overwrite


@pytest.mark.parametrize(
    "stamp, target",
    [
        ("abc", "ababc"),
        ("abca", "aabcaca"),
        ("k", "kkkkkkkkkkkkkkk"),
    ],
)
def test_moves_to_stamp(stamp: str, target: str):
    steps = moves_to_stamp(stamp, target)
    ans = "?" * len(target)
    for i in steps:
        ans = overwrite(ans, i, stamp)
    assert ans == target
