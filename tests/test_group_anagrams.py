import unittest
import pytest
from puzzles.group_anagrams import group_anagrams


def test_group_anagrams():
    case = unittest.TestCase()
    results = sorted(
        group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), key=len
    )
    exprected_results = sorted(
        [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]], key=len
    )
    for k, v in enumerate(results):
        case.assertCountEqual(v, exprected_results[k])

