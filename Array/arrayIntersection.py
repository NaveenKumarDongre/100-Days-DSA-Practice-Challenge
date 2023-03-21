#Array intersection 

def arrayIntersection(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
   
    for ele in arr1:
        if ele in arr2:
            print(ele, end=" ")
    print()
    
    
def arrayIntersectionBetter(arr1, arr2):
    n1 = len(arr1) 
    n2 = len(arr2)
    
    arr1.sort()
    arr2.sort()
    
    i , j  = 0, 0 
    while i < n1 and j < n2:
        if arr1[i] == arr2[j]:
            print(arr1[i], end=" ")
            i += 1
            j += 1 
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
    print()
            
            
def arrayIntersectionBest(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    
    hashMap = dict()
    for ele in arr1:
        hashMap[ele] = hashMap.get(ele, 0) + 1 
    
    for ele in arr2:
        if ele in hashMap:
            print(ele, end = " ") 
            hashMap[ele] -= 1
            if hashMap[ele] == 0:
                hashMap.pop(ele)
    print()
            
        

if __name__ == "__main__":
    arr1 = [int(x) for x in input().split(" ")]
    arr2 = [int(x) for x in input().split(" ")]
    
    arrayIntersection(arr1, arr2)
    arrayIntersectionBetter(arr1, arr2)
    arrayIntersectionBest(arr1, arr2)