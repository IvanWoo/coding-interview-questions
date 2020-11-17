from puzzles.validate_stack_sequences import validate_stack_sequences


def test_validate_stack_sequences():
    assert validate_stack_sequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]) == True
    assert validate_stack_sequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) == False
    assert validate_stack_sequences([2, 1, 0], [1, 2, 0]) == True
