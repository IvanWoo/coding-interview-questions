from puzzles.find_k_closest_elements import find_closest_elements


def test_find_closest_elements():
    assert find_closest_elements(arr=[1, 2, 3, 4, 5], k=4, x=3) == [1, 2, 3, 4]
    assert find_closest_elements(arr=[1, 2, 3, 4, 5], k=4, x=-1) == [1, 2, 3, 4]
    assert find_closest_elements([1, 1, 1, 10, 10, 10], 1, 9) == [10]
