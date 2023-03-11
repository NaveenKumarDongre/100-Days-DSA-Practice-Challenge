# 1.In Python , every member is accessible everywhere
class Test:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    def fun(self):
        print("Hi")
        
# t = Test(10,20)
# print(t.x)
# print(t.y)
# t.fun()


#2. When we use unaderscore before a varialbe name,
# we suggest not to use it outside class  
class Test1:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def _fun(self):
        print("Hi")
        
# t = Test1(10, 20)
# print(t.x)
# print(t.y)
# t._fun()

# When we use two underscore before a member name
# it becomes private 

class Test2: 
    def __init__(self,x,y):
        self.__x = x 
        self.y = y 
    def __fun(self):
        print("Hi")
t = Test2(10, 20)
# print(t.__x) Error --> no Attribute
# But can acces by 
print(t._Test2__x)
print(t.y)