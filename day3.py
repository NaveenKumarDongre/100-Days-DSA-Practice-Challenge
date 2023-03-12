#Find the index of the last occurence of element
#In a sorted array or list 
def findFirstIndex(arr, x):
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

def findLastIndex(arr,x):
    n = len(arr)
    l = 0 
    r = n - 1 
    
    while(l <= r):
        
        m = l + (r-l)//2 
        if arr[m] == x:
            if m == n - 1 or arr[m+1] != x: 
                return m 
            else:
                l = m + 1 
        elif arr[m] > x:
            r = m - 1
        else:
            l = m + 1 
    return -1 


# Count Occurrence in a Sorted array 

def naive_count_occurence(arr, x):
    count = 0
    for ele in arr:
        if ele == x:
            count+=1
    return count 

def better_count_occurence(arr,x):
    fi = findFirstIndex(arr, x)
    if fi == -1:
        return 0
    return findLastIndex(arr, x) - fi + 1
    
    


if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    x = int(input())
    # print(findFirstIndex(arr, x))
    # print(findLastIndex(arr, x))
    print(better_count_occurence(arr, x))
    # print(naive_count_occurence(arr, x))