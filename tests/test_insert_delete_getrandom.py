import random

import pytest

from puzzles.insert_delete_getrandom import RandomizedSet
from tests.utils import assert_obj_outs


@pytest.mark.parametrize(
    "ops, vals, outs",
    [
        (
            [
                "insert",
                "remove",
                "insert",
                "getRandom",
                "remove",
                "insert",
                "getRandom",
            ],
            [[1], [2], [2], [], [1], [2], []],
            [True, False, True, 2, True, False, 2],
        )
    ],
)
def test_randomized_set(ops, vals, outs):
    obj = RandomizedSet()
    # need to fix the random seed to have consistent testing results
    random.seed(11)
    assert_obj_outs(obj, ops, vals, outs)
