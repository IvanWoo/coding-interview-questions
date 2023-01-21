import pytest
from puzzles.restore_ip_addresses import restore_ip_addresses


@pytest.mark.parametrize(
    "s, expected",
    (
        ("25525511135", ["255.255.11.135", "255.255.111.35"]),
        ("0000", ["0.0.0.0"]),
    ),
)
def test_restore_ip_addresses(s, expected):
    assert restore_ip_addresses(s) == expected
