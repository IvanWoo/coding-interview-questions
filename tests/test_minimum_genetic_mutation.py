import pytest

from puzzles.minimum_genetic_mutation import min_mutation


@pytest.mark.parametrize(
    "start, end, bank, expected",
    [
        ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
        ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2),
        ("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"], 3),
        ("AACCGGTT", "AAACGGTA", ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"], 4),
        (
            "AAAAAAAA",
            "AAAAACGG",
            ["AAAAAAGA", "AAAAAGGA", "AAAAACGA", "AAAAACGG", "AAAAAAGG", "AAAAAAGC"],
            3,
        ),
    ],
)
def test_min_mutation(start, end, bank, expected):
    assert min_mutation(start, end, bank) == expected
