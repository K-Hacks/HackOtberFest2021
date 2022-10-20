def max_sum_subarray(arr):
    start, end = 0, 0
    max_end, max_so_far = 0, 0

    for i in range(len(arr)):
        max_end += arr[i]

        if max_end < 0:
            max_end = 0
            start = i + 1
        elif max_so_far < max_end:
            end = i
            max_so_far = max_end
    return arr[start: end + 1]


def brute_force(arr):
    start, end = 0, 9
    max_sum = float('-inf')

    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if sum(arr[i: j + 1]) > max_sum:
                start, end = i, j
                max_sum = sum(arr[start: end + 1])
    return arr[start: end + 1]


def main():
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(max_sum_subarray(arr))
    print(brute_force(arr))


if __name__ == '__main__':
    main()
