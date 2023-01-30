import pytest

from puzzles.lfu_cache import LFUCache
from tests.utils import assert_obj_outs


@pytest.mark.parametrize(
    "capacity, ops, vals, outs",
    [
        (
            2,
            ["put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
            [[1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]],
            [None, None, 1, None, -1, 3, None, -1, 3, 4],
        ),
        (
            0,
            ["put", "get"],
            [[0, 0], [0]],
            [None, -1],
        ),
        (
            2,
            ["get", "put", "get", "put", "put", "get", "get"],
            [[2], [2, 6], [1], [1, 5], [1, 2], [1], [2]],
            [-1, None, -1, None, None, 2, 6],
        ),
    ],
)
def test_lfu_cache(capacity, ops, vals, outs):
    obj = LFUCache(capacity)
    assert_obj_outs(obj, ops, vals, outs)
