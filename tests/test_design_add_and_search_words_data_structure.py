import pytest

from puzzles.design_add_and_search_words_data_structure import WordDictionary
from tests.utils import assert_obj_outs


@pytest.mark.parametrize(
    "ops, vals, outs",
    [
        (
            ["addWord", "addWord", "addWord", "search", "search", "search", "search"],
            [["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
            [None, None, None, False, True, True, True],
        ),
        (
            ["addWord", "addWord", "addWord", "addWord", "search"],
            [["at"], ["and"], ["an"], ["add"], ["a"]],
            [None, None, None, None, False],
        ),
    ],
)
def test_word_dictionary(ops, vals, outs):
    obj = WordDictionary()
    assert_obj_outs(obj, ops, vals, outs)
