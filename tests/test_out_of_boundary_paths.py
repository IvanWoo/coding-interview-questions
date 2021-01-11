from puzzles.out_of_boundary_paths import find_paths


def test_find_paths():
    assert find_paths(m=2, n=2, N=2, i=0, j=0) == 6
    assert find_paths(m=1, n=3, N=3, i=0, j=1) == 12
    assert find_paths(m=2, n=1, N=2, i=0, j=0) == 6
