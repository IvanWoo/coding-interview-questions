import pytest
from dacite import from_dict

from puzzles.construct_quad_tree import Node, construct


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [[0, 1], [1, 0]],
            {
                "val": False,
                "isLeaf": False,
                "topLeft": {
                    "val": False,
                    "isLeaf": True,
                    "topLeft": None,
                    "topRight": None,
                    "bottomLeft": None,
                    "bottomRight": None,
                },
                "topRight": {
                    "val": True,
                    "isLeaf": True,
                    "topLeft": None,
                    "topRight": None,
                    "bottomLeft": None,
                    "bottomRight": None,
                },
                "bottomLeft": {
                    "val": True,
                    "isLeaf": True,
                    "topLeft": None,
                    "topRight": None,
                    "bottomLeft": None,
                    "bottomRight": None,
                },
                "bottomRight": {
                    "val": False,
                    "isLeaf": True,
                    "topLeft": None,
                    "topRight": None,
                    "bottomLeft": None,
                    "bottomRight": None,
                },
            },
        ),
        (
            [
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0],
            ],
            {
                "val": True,
                "isLeaf": False,
                "topLeft": {
                    "val": True,
                    "isLeaf": True,
                    "topLeft": None,
                    "topRight": None,
                    "bottomLeft": None,
                    "bottomRight": None,
                },
                "topRight": {
                    "val": False,
                    "isLeaf": False,
                    "topLeft": {
                        "val": False,
                        "isLeaf": True,
                        "topLeft": None,
                        "topRight": None,
                        "bottomLeft": None,
                        "bottomRight": None,
                    },
                    "topRight": {
                        "val": False,
                        "isLeaf": True,
                        "topLeft": None,
                        "topRight": None,
                        "bottomLeft": None,
                        "bottomRight": None,
                    },
                    "bottomLeft": {
                        "val": True,
                        "isLeaf": True,
                        "topLeft": None,
                        "topRight": None,
                        "bottomLeft": None,
                        "bottomRight": None,
                    },
                    "bottomRight": {
                        "val": True,
                        "isLeaf": True,
                        "topLeft": None,
                        "topRight": None,
                        "bottomLeft": None,
                        "bottomRight": None,
                    },
                },
                "bottomLeft": {
                    "val": True,
                    "isLeaf": True,
                    "topLeft": None,
                    "topRight": None,
                    "bottomLeft": None,
                    "bottomRight": None,
                },
                "bottomRight": {
                    "val": False,
                    "isLeaf": True,
                    "topLeft": None,
                    "topRight": None,
                    "bottomLeft": None,
                    "bottomRight": None,
                },
            },
        ),
    ],
)
def test_construct(grid, expected):
    assert construct(grid) == from_dict(data_class=Node, data=expected)
