from puzzles.satisfiability_of_equality_equations import equations_possible


def test_equations_possible():
    assert equations_possible(["a==b", "b!=a"]) == False
    assert equations_possible(["a==b", "b==a"]) == True
    assert equations_possible(["a==b", "b==c", "a==c"]) == True
    assert equations_possible(["a==b", "b!=c", "c==a"]) == False
    assert equations_possible(["c==c", "b==d", "x!=z"]) == True
