#Merge Two Sorted Lists 
"""
I/P: a = [10,15,20]
     b = [5, 6,  30]
     
O/P: res = [5, 6, 10, 15, 20, 30]

"""

def mergeTwoSortedLists(a1, a2):
    
    n1 = len(a1)
    n2 = len(a2)
    res = [0]*(n1+n2)
    i, j, k  = 0, 0, 0
   
    while( i < n1 and j < n2):
        
        if(a1[i] < a2[j]):
            
            res[k] = a1[i]
            k = k + 1
            i = i + 1 
        else:
            
            res[k] = a2[j]
            k = k + 1 
            j = j + 1 
            
    while (i < n1):
        
        res[k] = a1[i]
        k = k + 1 
        i = i + 1
        
    while (j < n2):
        
        res[k] = a2[j]
        k = k + 1 
        j = j + 1
        
    return res 

if __name__ == "__main__":
    a1 = [int(x) for x in input().split()]
    a2 = [int(x) for x in input().split()]
    
    res = mergeTwoSortedLists(a1, a2)
    
    print(res)
    
    
    
    