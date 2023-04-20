# Problem Statement:
# You are given an array A, of N elements.
# Find minimum index based distance between two elements of the array, x and y such that (x!=y).

def minDist(arr, n, x, y):
    if x == y:
        return -1
    id_x = -1
    id_y = -1
    mini = pow(10, 5) + 1
    for i in range(n):
        if arr[i] == x:
            id_x = i
        if arr[i] == y:
            id_y = i
        if id_x != -1 and id_y != -1:
            if abs(id_x - id_y) < mini:
                mini = abs(id_x - id_y)
    if id_x == -1 or id_y == -1:
        return -1

    return mini


if __name__ == "__main__":

    n = int(input())
    arr = [int(x) for x in input().split()]
    x = int(input())
    y = int(input())

    print(minDist(arr, n, x, y))
