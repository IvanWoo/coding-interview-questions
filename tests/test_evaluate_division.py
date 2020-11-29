from puzzles.evaluate_division import calc_equation


def test_calc_equation():
    assert (
        calc_equation(
            equations=[["a", "b"], ["b", "c"]],
            values=[2.0, 3.0],
            queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
        )
        == [6, 0.5, -1, 1, -1]
    )
    assert (
        calc_equation(
            equations=[["a", "b"], ["b", "c"], ["bc", "cd"]],
            values=[1.5, 2.5, 5.0],
            queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
        )
        == [3.75, 0.4, 5.0, 0.2]
    )
    assert (
        calc_equation(
            equations=[["a", "b"]],
            values=[0.5],
            queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
        )
        == [0.5, 2, -1, -1]
    )
