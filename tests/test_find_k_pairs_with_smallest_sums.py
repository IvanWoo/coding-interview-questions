from puzzles.find_k_pairs_with_smallest_sums import k_smallest_pairs


def test_k_smallest_pairs():
    assert k_smallest_pairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3) == [
        [1, 2],
        [1, 4],
        [1, 6],
    ]
    assert k_smallest_pairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2) == [[1, 1], [1, 1]]
    assert k_smallest_pairs(nums1=[], nums2=[1, 2, 3], k=2) == []
    assert k_smallest_pairs(nums1=[], nums2=[], k=2) == []
    assert k_smallest_pairs(nums1=[1, 2], nums2=[3], k=3) == [[1, 3], [2, 3]]
    assert sorted(k_smallest_pairs([1, 1, 2], [1, 2, 3], 10)) == sorted(
        [
            [1, 1],
            [1, 1],
            [2, 1],
            [1, 2],
            [1, 2],
            [2, 2],
            [1, 3],
            [1, 3],
            [2, 3],
        ]
    )
