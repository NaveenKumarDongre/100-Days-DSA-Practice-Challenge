# List sort() in python 
l1 = [5, 10, 15, 1]

# Sorted in a ascending order
l1.sort()
# print(l1)
l2 = [1,5,3,10]

# Sorted in a decending order 
l2.sort(reverse=True)
# print(l2)

# Sorting user defined using key function 
l3 = ["gfg", "ide", "courses"]

def sort_based_on_length(s):
    return len(s) 
l3.sort(key = sort_based_on_length, reverse = True)
# print(l3) 

class Point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
        
    def __str__(self):
        return f"({self.x}, {self.y})"

def myFun(p):
    return p.x 

l = [Point(1,15), Point(10,5), Point(3,8)]
l.sort(key = myFun)

for p in l:
    print(p)

arr = [-11, 23, -4, -10, 100]
arr.sort(key=abs, reverse=True)
print(arr)

t = (10,12,5,1)
print(sorted(t))
  