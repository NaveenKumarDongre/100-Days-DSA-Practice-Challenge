#Implement an algorithm to determine if a string has all
#unique characters. What if cannot use additional data structure

def isUniqueNiave(string):
    n = len(string)
    for i in range(n):
        if string[i] in string[i+1:n]:
            return False 
    else:
        return True
    
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
    
    
def isUnique(string):
    hashMap = dict()
    for ele in string:
        hashMap[ele] = hashMap.get(ele, 0) + 1 
    
    for key in hashMap:
        if hashMap[key] > 1:
            return False 
    return True 


def betterIsUnique(string):
    
    arr = [0]*128 
    
    for ele in string:
        # print(ord(ele))
        if arr[ord(ele)] == 1:
            # print(arr.count(1))
            return False 
        elif arr[ord(ele)] == 0:
            arr[ord(ele)] = 1
 
    # print(arr.count(1), len(arr))
    return True 
    
    

    
     

if __name__ == "__main__":
    
    string = input("Enter the string: ")
    print( "Have Unique characters" if isUnique(string) else "Don't have Unique characters")
    print( "Have Unique characters" if isUniqueNiave(string) else "Don't have Unique characters")
    print( "Have Unique characters" if betterIsUnique(string) else "Don't have Unique characters")