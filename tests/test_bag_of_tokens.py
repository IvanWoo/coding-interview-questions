import pytest
from puzzles.bag_of_tokens import bag_of_tokens_score


@pytest.mark.parametrize(
    "tokens, power, expected",
    [
        ([100], 90, 0),
        ([100, 200], 150, 1),
        ([100, 200, 300, 400], 200, 2),
        ([58, 91], 50, 0),
        ([], 85, 0),
    ],
)
def test_bag_of_tokens_score(tokens, power, expected):
    assert bag_of_tokens_score(tokens, power) == expected
