import pytest
from puzzles.orderly_queue import orderly_queue


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("cba", 1, "acb"),
        ("baaca", 3, "aaabc"),
        ("v", 1, "v"),
        ("gn", 2, "gn"),
        ("kuh", 1, "hku"),
        ("xmvzi", 2, "imvxz"),
    ],
)
def test_orderly_queue(s, k, expected):
    assert orderly_queue(s, k) == expected
