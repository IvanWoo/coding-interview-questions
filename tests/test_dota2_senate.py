import pytest

from puzzles.dota2_senate import predict_party_victory


@pytest.mark.parametrize(
    "senate, expected",
    [
        ("RD", "Radiant"),
        ("RDD", "Dire"),
    ],
)
def test_predict_party_victory(senate, expected):
    assert predict_party_victory(senate) == expected
