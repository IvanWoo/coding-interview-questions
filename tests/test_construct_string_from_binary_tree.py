import pytest
from puzzles.utils import make_tree
from puzzles.construct_string_from_binary_tree import tree2str


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([1, 2, 3, 4]), "1(2(4))(3)"),
        (make_tree([1, 2, 3, None, 4]), "1(2()(4))(3)"),
    ],
)
def test_tree2str(root, expected):
    assert tree2str(root) == expected
