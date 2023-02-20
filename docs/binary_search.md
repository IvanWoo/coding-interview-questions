# binary search

template

```py
lo, hi = 0, n - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] < target:
        lo = mid + 1
    elif nums[mid] > target:
        hi = mid - 1
    elif nums[mid] == target:
        # change the behavior based on the requirements
        ...
# check the boundary
```
