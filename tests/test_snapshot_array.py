import pytest

from puzzles.snapshot_array import SnapshotArray
from tests.utils import assert_obj_outs


@pytest.mark.parametrize(
    "ops, vals, outs",
    [
        (
            ["set", "snap", "set", "get"],
            [[0, 5], [], [0, 6], [0, 0]],
            [None, 0, None, 5],
        ),
    ],
)
def test_snapshot_array(ops, vals, outs):
    obj = SnapshotArray(3)
    assert_obj_outs(obj, ops, vals, outs)
