# insertion sort 

def insertion_sort(arr):
    n = len(arr) 
    
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while(j >= 0 and key < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1 
        arr[j+1] = key 

if __name__ == "__main__":
    arr = [int(x) for x in input().split(" ")]
    insertion_sort(arr)
    print(arr)
        