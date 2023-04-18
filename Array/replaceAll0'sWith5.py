# Problem Statement:
# You are given an integer N.
# You need to convert all zeroes of N to 5.
# Input:
# N = 1004
# Output: 1554
# Explanation: There are two zeroes in 1004
# on replacing all zeroes with "5", the new
# number will be "1554".

# Iterative Approach
def convertFive1(n):
    # Code here
    # Using a Stack data structure
    stk = []
    ans = 0

    # Filling the stack from the end digits of the number
    while n:
        stk.append(n % 10)
        n = n // 10
    # Poping element from the stack and simultaneously building answer
    while stk:
        ele = stk.pop()
        if ele == 0:
            ans = (ans*10) + 5
        else:
            ans = (ans*10) + ele
    return ans

# Recursive Approach


def convertFive(n):

    if n == 0:
        return 0

    digit = n % 10
    if digit == 0:
        digit = 5

    return convertFive(n//10)*10 + digit


if __name__ == "__main__":
    n = int(input())
    print(convertFive(n))
