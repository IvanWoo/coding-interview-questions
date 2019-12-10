import pytest

from puzzles.flood_fill import flood_fill


def test_flood_fill_0():
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    assert flood_fill(image, sr, sc, newColor) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]


def test_flood_fill_1():
    image = [[0, 0, 0], [0, 1, 1]]
    sr = 1
    sc = 1
    newColor = 1
    assert flood_fill(image, sr, sc, newColor) == [[0, 0, 0], [0, 1, 1]]

