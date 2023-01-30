from puzzles.longest_word_in_dictionary_through_deleting import find_longest_word


def test_find_longest_word():
    assert (
        find_longest_word(s="abpcplea", d=["ale", "apple", "monkey", "plea"]) == "apple"
    )
    assert find_longest_word(s="abpcplea", d=["a", "b", "c"]) == "a"
    assert (
        find_longest_word(
            "aewfafwafjlwajflwajflwafj",
            ["apple", "ewaf", "awefawfwaf", "awef", "awefe", "ewafeffewafewf"],
        )
        == "ewaf"
    )
