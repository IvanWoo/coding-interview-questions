import pytest

from puzzles.design_browser_history import BrowserHistory
from tests.utils import assert_obj_outs


@pytest.mark.parametrize(
    "ops, vals, outs",
    [
        (
            [
                "visit",
                "visit",
                "visit",
                "back",
                "back",
                "forward",
                "visit",
                "forward",
                "back",
                "back",
            ],
            [
                ["google.com"],
                ["facebook.com"],
                ["youtube.com"],
                [1],
                [1],
                [1],
                ["linkedin.com"],
                [2],
                [2],
                [7],
            ],
            [
                None,
                None,
                None,
                "facebook.com",
                "google.com",
                "facebook.com",
                None,
                "linkedin.com",
                "google.com",
                "leetcode.com",
            ],
        ),
    ],
)
def test_browser_history(ops, vals, outs):
    obj = BrowserHistory("leetcode.com")
    assert_obj_outs(obj, ops, vals, outs)
