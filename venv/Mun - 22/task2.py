n, m = [int(i) for i in input().split()]


def get_anser(x):
    s = x
    while x >= m:
        s += x // m
        x = x % m + x // m
    return s


arr = list(range(n + 1))


def binary_search(n, arr):
    lower_bound = 0
    upper_bound = len(arr) - 1
    while lower_bound <= upper_bound:
        center = (lower_bound + upper_bound) // 2

        if get_anser(arr[center]) == n:
            return center

        elif get_anser(arr[center]) > n:
            upper_bound = center - 1

        elif get_anser(arr[center]) > n:
            lower_bound = center + 1

    return -1


print(arr[binary_search(n, arr)])



