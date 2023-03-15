# Selection Sort 

def selectionSort(arr):
    n = len(arr)
    
    for i in range(n-1):
        
        min_index = i 
        min_ele = arr[i]
        
        
        for j in range(i+1, n):
            
            if min_ele > arr[j]:
                
                min_ele = arr[j]
                min_index = j
                
             
        arr[i], arr[min_index] = arr[min_index], arr[i]
         
        

if __name__ == "__main__":
    arr = [int(x) for x in input().split(" ")]
    selectionSort(arr)
    print(arr)
            
            