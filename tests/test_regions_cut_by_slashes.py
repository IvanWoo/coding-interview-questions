from puzzles.regions_cut_by_slashes import regions_by_slashes


def test_regions_by_slashes():
    assert regions_by_slashes([" /", "/ "]) == 2
    assert regions_by_slashes([" /", "  "]) == 1
    assert regions_by_slashes(["\\/", "/\\"]) == 4
    assert regions_by_slashes(["/\\", "\\/"]) == 5
    assert regions_by_slashes(["//", "/ "]) == 3
