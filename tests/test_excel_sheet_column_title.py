import pytest
from puzzles.excel_sheet_column_title import convert_to_title


def test_convert_to_title():
    assert convert_to_title(1) == "A"
    assert convert_to_title(27) == "AA"
    assert convert_to_title(28) == "AB"
    assert convert_to_title(701) == "ZY"