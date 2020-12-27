from puzzles.ones_and_zeroes import find_max_form


def test_find_max_form():
    assert find_max_form(strs=["10", "0001", "111001", "1", "0"], m=5, n=3) == 4
    assert find_max_form(strs=["10", "0", "1"], m=1, n=1) == 2
    assert (
        find_max_form(
            strs=[
                "0",
                "1101",
                "01",
                "00111",
                "1",
                "10010",
                "0",
                "0",
                "00",
                "1",
                "11",
                "0011",
            ],
            m=63,
            n=36,
        )
        == 12
    )
