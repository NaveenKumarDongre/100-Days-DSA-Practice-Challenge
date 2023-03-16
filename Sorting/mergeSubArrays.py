def mergeSubarrays(arr, low, mid, high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]
    
    i = 0
    j = 0
    k = low
    
    while i < len(left) and j < len(right):
        
        if left[i] < right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1 
    
    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    
    while j < len(right):
        arr[k] = right[j]
        k += 1 
        j += 1
        
if __name__ == "__main__":
    
    arr = [int(x) for x in input().split()]
    low = int(input("Low: "))
    high = int(input("High: "))
    mid = int(input("Mid: "))
    
    mergeSubarrays(arr, low, mid, high)
    
    print(arr)
        
    
    