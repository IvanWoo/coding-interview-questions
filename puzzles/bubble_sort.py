def bubble_sort(arr):
    n = len(arr)
    while True:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    bubble_sort([5, 1, 1, 2, 0, 0])