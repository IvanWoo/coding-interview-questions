# question: https://www.youtube.com/watch?v=5o-kdjv7FD0&t=127s


# recursive
def num_ways(n):
    if n == 0 or n == 1:
        return 1
    else:
        return num_ways(n - 2) + num_ways(n - 1)


# dynamic programming
def num_ways_bottom_up(n):
    nums = {0: 1, 1: 1}
    if n <= 1:
        return nums[n]
    for i in range(2, n + 1):
        nums[i] = nums[i - 1] + nums[i - 2]
    return nums[n]


# space optimized dynamic programming
def num_ways_bottom_up_less_space(n):
    a = 1
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b


def num_ways_x(n, x):
    if n == 0:
        return 1
    total = 0
    for step in x:
        if n - step >= 0:
            total += num_ways_x(n - step, x)
    return total


def num_ways_x_bottom_up(n, x):
    if n == 0:
        return 1
    nums = {0: 1}
    for i in range(1, n + 1):
        total = 0
        for step in x:
            if i - step >= 0:
                total += num_ways_x_bottom_up(i - step, x)
        nums[i] = total
    return nums[n]


print(num_ways(2))
print(num_ways(4))

print(num_ways_bottom_up(37))
print(num_ways_bottom_up_less_space(37))

print("expect to be 2: ", num_ways_x(2, [1, 2]))
print("expect to be 5: ", num_ways_x(4, [1, 2]))

print(num_ways_x_bottom_up(10, [1, 3, 5]))
print(num_ways_x_bottom_up(20, [1, 3, 5]))
