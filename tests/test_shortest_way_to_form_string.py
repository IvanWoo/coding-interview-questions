import pytest
from puzzles.shortest_way_to_form_string import shortest_way_to_form_string


def test_shortest_way_to_form_string():
    assert shortest_way_to_form_string(source="abc", target="abcbc") == 2
    assert shortest_way_to_form_string(source="abc", target="acdbc") == -1
    assert shortest_way_to_form_string(source="xyz", target="xzyxz") == 3

