#Square Root 
"""
    I/P: X = 4
    O/P: 2
    
    I/P: X = 14
    O/P: 3
    
    I/P: X = 25
    O/P: 5
"""

# Niave approach 
def squareRoot(num):
    i = 1
    res = 0
    while True:
        if (i*i) >  num:
            break
        res = i  
        i = i + 1
    return res
    # return int(pow(num, 0.5))
    
    
# Efficient approach using binary search 
# Time complexity O(logn)
def efficentSquareRoot(num):
    res = 0 
    l = 1 
    r = num 
    while l <= r:
        m = l + (r-l)//2 
        sq = (m*m)
        if sq == num:
            return m 
        elif sq > num:
            r = m - 1
        else:
            res = m 
            l = m + 1 
    return res 
        

if __name__ == "__main__":
    num = int(input())
    print(squareRoot(num))
    print(efficentSquareRoot(num))