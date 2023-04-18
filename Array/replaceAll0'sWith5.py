# Problem Statement:
# You are given an integer N. 
# You need to convert all zeroes of N to 5.
# Input:
# N = 1004
# Output: 1554
# Explanation: There are two zeroes in 1004
# on replacing all zeroes with "5", the new
# number will be "1554".

def convertFive(n):
    # Code here
    # Using a Stack data structure 
    stk = []
    ans = 0
    
    # Filling the stack from the end digits of the number
    while n:
        stk.append(n%10)
        n = n // 10 
    # Poping element from the stack and simultaneously building answer
    while stk:
        ele = stk.pop()
        if ele == 0:
            ans = (ans*10) + 5
        else:
            ans = (ans*10) + ele 
    return ans 

if __name__ == "__main__":
    n = int(input())
    print(convertFive(n))