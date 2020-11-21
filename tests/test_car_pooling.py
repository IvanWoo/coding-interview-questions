from puzzles.car_pooling import car_pooling


def test_car_pooling():
    assert car_pooling([[2, 1, 5], [3, 3, 7]], 5) == True
    assert car_pooling([[2, 1, 5], [3, 3, 7]], 4) == False
    assert car_pooling([[2, 1, 5], [3, 5, 7]], 3) == True
    assert car_pooling([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11) == True
