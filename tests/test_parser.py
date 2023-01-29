import pytest

from puzzles.parser import parser


def test_parser():
    assert parser("3[abc]4[ab]c") == "abcabcabcababababc"
    assert parser("10[a]") == "aaaaaaaaaa"
    assert parser("2[3[a]b]") == "aaabaaab"
    assert parser("0[abc]") == ""
    assert parser("1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[xx]]]]]]]]]]]]]]]]]]]]") == "xx"
    assert parser("a[]b") == "ab"
