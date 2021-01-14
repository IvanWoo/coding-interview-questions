from puzzles.valid_square import valid_square


def test_valid_square():
    assert valid_square(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 1]) == True
    assert valid_square(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 12]) == False
    assert valid_square(p1=[1, 0], p2=[-1, 0], p3=[0, 1], p4=[0, -1]) == True
    assert valid_square([0, 1], [1, 1], [1, 1], [1, 0]) == False
