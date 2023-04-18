# Problem Statement:
# Given an array of distinct elements.
# Find the third largest element in it.
# Suppose you have A[] = {1, 2, 3, 4, 5, 6, 7},
# its output will be 5 because it is the 3 largest element in the array A.

# Example 1:

# Input:
# N = 5
# A[] = {2,4,1,3,5}
# Output: 3

def thirdLargest(a, n):
    # code here
    if n < 3:
        return -1
    # a.sort()
    # return a[n-3]
    m1 = a[0]
    m2 = -1
    m3 = -2
    for i in range(1, n):
        if m1 < a[i]:
            m3 = m2
            m2 = m1
            m1 = a[i]
        elif m2 < a[i]:
            m3 = m2
            m2 = a[i]
        elif m3 < a[i]:
            m3 = a[i]
    return m3


if __name__ == "__main__":
    n = int(input())
    a = [int(x) for x in input().split(" ")]

    print(thirdLargest(a, n))
