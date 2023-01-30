import pytest

from puzzles.maximum_product_of_splitted_binary_tree import max_product
from puzzles.utils import make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([1, 2, 3, 4, 5, 6]), 110),
        (make_tree([1, None, 2, 3, 4, None, None, 5, 6]), 90),
    ],
)
def test_max_product(root, expected):
    assert max_product(root) == expected
