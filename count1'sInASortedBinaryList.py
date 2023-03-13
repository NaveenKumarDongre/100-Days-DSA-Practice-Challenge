#Count 1's in a Sorted Binary List
"""
I/P: l = [0,0,0,1,1,1,1]
O/P: 4

I/P: l = [1,1,1,1,1]
O/P: 5 

I/P: l = [0,0,0]
O/P: 0
"""

# Naive approach 
def countOnesInASortedBinaryList(arr):
    n = len(arr) 
    for i in range(n):
        if(arr[i] == 1):
            return (n-i)
    return 0

# Efficient approach 
def efficientCountOnes(arr):
    n = len(arr)
    l = 0
    r = n - 1 
    while l <= r:
        m = l + (r-l)//2 
        if arr[m] < 1:
            l = m + 1
        else:
            if m == 0:
                return n
            elif arr[m-1] == 1:
                r = m - 1
            else:
                return n - m
    return 0
            
        
if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    print(f"Number of one's in the array: {countOnesInASortedBinaryList(arr)}")
    print(f"Number of one's in the array: {efficientCountOnes(arr)}")