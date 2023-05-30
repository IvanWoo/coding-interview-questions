import pytest

from puzzles.design_hashset import MyHashSet
from tests.utils import assert_obj_outs


@pytest.mark.parametrize(
    "ops, vals, outs",
    [
        (
            [
                "add",
                "add",
                "contains",
                "contains",
                "add",
                "contains",
                "remove",
                "contains",
            ],
            [[1], [2], [1], [3], [2], [2], [2], [2]],
            [None, None, True, False, None, True, None, False],
        ),
    ],
)
def test_word_dictionary(ops, vals, outs):
    obj = MyHashSet()
    assert_obj_outs(obj, ops, vals, outs)
