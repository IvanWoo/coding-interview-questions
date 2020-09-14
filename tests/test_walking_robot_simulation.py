import pytest
from puzzles.walking_robot_simulation import robot_sim


def test_robot_sim():
    assert robot_sim([4, -1, 3], []) == 25
    assert robot_sim([4, -1, 4, -2, 4], [[2, 4]]) == 65
