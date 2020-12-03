from puzzles.sequential_digits import sequential_digits


def test_sequential_digits():
    assert sequential_digits(100, 300) == [123, 234]
    assert sequential_digits(123, 234) == [123, 234]
    assert sequential_digits(1000, 13000) == [1234, 2345, 3456, 4567, 5678, 6789, 12345]
