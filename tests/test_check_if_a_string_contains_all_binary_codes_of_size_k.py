import pytest
from puzzles.check_if_a_string_contains_all_binary_codes_of_size_k import has_all_codes


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("00110110", 2, True),
        ("0110", 1, True),
        ("0110", 2, False),
        ("00110", 2, True),
    ],
)
def test_has_all_codes(s: str, k: int, expected: bool):
    assert has_all_codes(s, k) == expected
