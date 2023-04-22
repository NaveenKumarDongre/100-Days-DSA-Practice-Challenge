# Problem Statement:
# Given an unsorted array arr[] of size N. Rotate the array to the left
# (counter-clockwise direction) by D steps, where D is a positive integer.
"""
Example 1:

Input:
N = 5, D = 2
arr[] = {1,2,3,4,5}
Output: 3 4 5 1 2
Explanation: 1 2 3 4 5  when rotated
by 2 elements, it becomes 3 4 5 1 2.
"""


def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def rotateArr(A, D, N):
    # Your code here
    D = D % N
    reverse(A, 0, D-1)
    reverse(A, D, N-1)
    reverse(A, 0, N-1)


if __name__ == "__main__":
    A = [int(x) for x in input().split(" ")]
    D = int(input())
    N = len(A)
    rotateArr(A, D, N)
    print(f"Array after the rotation by {D} steps")
    print(A)
