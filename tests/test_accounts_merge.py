from puzzles.accounts_merge import accounts_merge


def test_accounts_merge():
    assert sorted(
        accounts_merge(
            [
                ["John", "johnsmith@mail.com", "john00@mail.com"],
                ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["Mary", "mary@mail.com"],
            ]
        )
    ) == sorted(
        [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["Mary", "mary@mail.com"],
        ]
    )
