import pytest
import numpy as np
from puzzles.max_vacation_days import (
    max_vacation_days,
    max_vacation_days_dp,
    get_inputs,
)


def test_max_vacation_days_0():
    inputs = get_inputs(
        [[0, 1, 1], [1, 0, 1], [1, 1, 0]], [[1, 3, 1], [6, 0, 3], [3, 3, 3]]
    )
    assert max_vacation_days(**inputs) == 12


def test_max_vacation_days_1():
    inputs = get_inputs(
        [[0, 1, 1], [1, 0, 1], [1, 1, 0]], [[7, 0, 0], [0, 7, 0], [0, 0, 7]]
    )
    assert max_vacation_days(**inputs) == 21


def test_max_vacation_days_stay_in_0():
    inputs = get_inputs(
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [7, 7, 7], [7, 7, 7]]
    )
    assert max_vacation_days(**inputs) == 3


def test_max_vacation_days_random():
    for i in range(3):
        inputs = get_inputs(
            np.random.randint(2, size=(7, 7)).tolist(),
            np.random.randint(8, size=(7, 7)).tolist(),
        )
        assert max_vacation_days(**inputs) == max_vacation_days_dp(**inputs)
