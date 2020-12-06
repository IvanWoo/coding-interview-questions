from puzzles.word_ladder_ii import find_ladders


def test_find_ladders():
    assert sorted(
        find_ladders(
            beginWord="hit",
            endWord="cog",
            wordList=["hot", "dot", "dog", "lot", "log", "cog"],
        )
    ) == sorted(
        [
            ["hit", "hot", "dot", "dog", "cog"],
            ["hit", "hot", "lot", "log", "cog"],
        ]
    )
    assert (
        find_ladders(
            beginWord="hit",
            endWord="cog",
            wordList=["hot", "dot", "dog", "lot", "log"],
        )
        == []
    )
