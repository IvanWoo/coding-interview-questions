from puzzles.make_the_string_great import make_good


def test_make_good():
    assert make_good("abBAcC") == ""
    assert make_good("") == ""
    assert make_good("s") == "s"
    assert make_good("LoOkGood") == "LkGood"
