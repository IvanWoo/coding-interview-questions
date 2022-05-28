import pytest
from puzzles.encoder import encoder


@pytest.mark.parametrize(
    "row, code_word, expected",
    [
        (["a"], ["1", "2", "3", "4"], ["1"]),
        (["a", "b"], ["1", "2", "3", "4"], ["1", "2"]),
        (["a", "b", "a"], ["1", "2", "3", "4"], ["1", "2", "1"]),
    ],
)
def test_encoder(row, code_word, expected):
    assert encoder(row, code_word) == expected
