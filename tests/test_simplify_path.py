import pytest

from puzzles.simplify_path import simplify_path


@pytest.mark.parametrize(
    "path, expected",
    [
        ("/home/", "/home"),
        ("/../", "/"),
        ("/home//foo/", "/home/foo"),
    ],
)
def test_simplify_path(path, expected):
    assert simplify_path(path) == expected
