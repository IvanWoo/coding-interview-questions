import pytest

from puzzles.trie import Trie
from tests.utils import assert_obj_outs


@pytest.mark.parametrize(
    "ops, vals, outs",
    [
        (
            ["insert", "search", "search", "startsWith", "insert", "search"],
            [["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            [None, True, False, True, None, True],
        ),
    ],
)
def test_trie(ops, vals, outs):
    obj = Trie()
    assert_obj_outs(obj, ops, vals, outs)
