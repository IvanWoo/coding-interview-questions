from puzzles.expression_add_operators import add_operators


def test_add_operators():
    assert sorted(add_operators(num="123", target=6)) == sorted(["1+2+3", "1*2*3"])
    assert sorted(add_operators(num="232", target=8)) == sorted(["2*3+2", "2+3*2"])
    assert sorted(add_operators(num="105", target=5)) == sorted(["1*0+5", "10-5"])
    assert sorted(add_operators(num="00", target=0)) == sorted(["0+0", "0-0", "0*0"])
    assert sorted(add_operators(num="3456237490", target=9191)) == sorted([])
