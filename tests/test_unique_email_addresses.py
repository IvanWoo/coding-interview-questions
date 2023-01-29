import pytest

from puzzles.unique_email_addresses import num_unique_emails


@pytest.mark.parametrize(
    "emails, expected",
    [
        (
            [
                "test.email+alex@leetcode.com",
                "test.e.mail+bob.cathy@leetcode.com",
                "testemail+david@lee.tcode.com",
            ],
            2,
        ),
        (["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"], 3),
    ],
)
def test_num_unique_emails(emails, expected):
    assert num_unique_emails(emails) == expected
