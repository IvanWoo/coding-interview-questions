from puzzles.strange_printer import strange_printer


def test_strange_printer():
    assert strange_printer("aaabbb") == 2
    assert strange_printer("aba") == 2
