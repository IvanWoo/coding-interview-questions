from puzzles.restore_ip_addresses import restore_ip_addresses


def test_restore_ip_addresses():
    assert restore_ip_addresses("25525511135") == ["255.255.11.135", "255.255.111.35"]
    assert restore_ip_addresses("0000") == ["0.0.0.0"]
