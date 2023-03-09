

# All Divisors of a Number 

# n = 15
# 1 2 5 15
import math

def allDivisors(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i, end=" ")
    print()
    
def betterAllDivisor(n):
    r = math.floor(pow(n, 0.5))
    for i in range(1,r+1):
        if n % i == 0:
            print(i, end=" ")
            # if(i != n//i):
            print(n//i, end=" ")
    print()
    
def removeDuplicates(arr):
    
    n = len(arr)
    j = 0
    for i in range(1,n):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    return j+1
        
    
if __name__ == "__main__":
    arr = [int(x) for x in input().split(" ")]
    n = removeDuplicates(arr)
    print(n)
    for i in range(n):
        print(arr[i], end=" ")
    print()
    # n = int(input("Enter the number: "))
    # allDivisors(n)
    # betterAllDivisor(n)
    # print(math.floor(pow(4, 0.5)))