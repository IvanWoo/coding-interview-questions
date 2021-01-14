from puzzles.top_k_frequent_words import top_k_frequent


def test_top_k_frequent():
    assert top_k_frequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == [
        "i",
        "love",
    ]
    assert top_k_frequent(["i", "love", "leetcode", "i", "love", "coding"], 3) == [
        "i",
        "love",
        "coding",
    ]
    assert top_k_frequent(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4
    ) == ["the", "is", "sunny", "day"]
