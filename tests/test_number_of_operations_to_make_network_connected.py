from puzzles.number_of_operations_to_make_network_connected import make_connected


def test_make_connected():
    assert make_connected(n=4, connections=[[0, 1], [0, 2], [1, 2]]) == 1
    assert make_connected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2]]) == -1
    assert make_connected(n=5, connections=[[0, 1], [0, 2], [3, 4], [2, 3]]) == 0
    assert (
        make_connected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]) == 2
    )
