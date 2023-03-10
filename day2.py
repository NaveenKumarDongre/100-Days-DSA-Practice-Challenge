#Searching Concepts 

def binarySeach(arr, x):
    left = 0
    right = len(arr) - 1 
    
    
    while(left <= right):
        
        m = left + (right - left) // 2
        
        if arr[m] == x:
            return m 
        elif arr[m] > x:
            right = m - 1 
        else:
            left = m + 1 
            
    return -1 


def recursiveBinarySearch(arr,x,l,r):
    
    if l > r:
        return -1 
    mid = l + (r - l) // 2
    
    if arr[mid] == x:
        return mid 
    elif arr[mid] > x:
        return recursiveBinarySearch(arr, x, l, mid-1)
    else:
        return recursiveBinarySearch(arr, x, mid+1, r)
    
    
    
# Find the index of the first Occurrence 
# This is best approach with better time complexity
def indexOfFirstOccurrence(arr, x):
    n = len(arr)

    l = 0
    r = n - 1
    
    while l <= r:
        
        m = (l+r)//2 
        
        if arr[m] == x:
            if arr[m-1] != x or m == 0:
                return m
            else:
                r = m - 1
        elif arr[m] > x:
            r = m - 1 
        else:
            l = m + 1 
    return -1 
            
        
if __name__ == "__main__":
    arr = [int(x) for x in input("Enter the elements: ").split(" ")]
    x = int(input("Enter the element to search: "))
    # print(binarySeach(arr, x))
    # print(recursiveBinarySearch(arr, x, 0, len(arr) - 1))
    print(indexOfFirstOccurrence(arr, x))