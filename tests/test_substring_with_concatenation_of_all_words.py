from puzzles.substring_with_concatenation_of_all_words import find_substring


def test_find_substring():
    assert find_substring(
        "wordgoodgoodgoodbestword", ["word", "good", "best", "good"]
    ) == [8]
    assert find_substring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]
    assert (
        find_substring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"])
        == []
    )
    assert find_substring("barfoofoobarthefoobarman", ["bar", "foo", "the"]) == [
        6,
        9,
        12,
    ]
