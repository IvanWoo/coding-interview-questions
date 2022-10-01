import pytest
from puzzles.decode_ways import num_decodings


@pytest.mark.parametrize(
    "s, expected",
    [
        ("12", 2),
        ("226", 3),
        ("06", 0),
        ("222", 3),
    ],
)
def test_num_decodings(s, expected):
    assert num_decodings(s) == expected
