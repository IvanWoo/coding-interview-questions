from collections import deque


def merge(arr1, arr2):
    ans = deque()
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    ans.extend(arr1[i:])
    ans.extend(arr2[j:])
    return list(ans)


def sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = sort(nums[:mid])
    right = sort(nums[mid:])

    return merge(left, right)


def merge_sort(nums):
    n = len(nums)
    copy = nums[:]

    def sort(lo, hi):
        if lo >= hi - 1:
            return
        mid = (lo + hi) >> 1
        sort(lo, mid)
        sort(mid, hi)

        i, j = lo, mid
        while i < j and j < hi:
            if copy[i] < copy[j]:
                i += 1
            else:
                for k in range(j, i, -1):
                    copy[k], copy[k - 1] = copy[k - 1], copy[k]
                i += 1
                j += 1

    sort(0, n)
    return copy
