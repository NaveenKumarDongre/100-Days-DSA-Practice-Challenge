# Problen: Max and Second Max
# Given an array arr[] of size N of positive integers which may have duplicates.
# The task is to find the maximum and second maximum from the array,
# and both of them should be different from each other,
# so If no second max exists, then the second max will be -1.

def largestAndSecondLargest(arr):

    n = len(arr)
    if n < 2:
        return [arr[0], -1]

    m1 = arr[0]
    m2 = -1

    for i in range(1, n):

        if m1 < arr[i]:
            m2 = m1
            m1 = arr[i]

        elif m2 < arr[i] and m1 != arr[i]:
            m2 = arr[i]

    return [m1, m2]


if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    print(largestAndSecondLargest(arr))
