def dec_fun(f):
    def inner_fun(n):
        print("Welcome")
        f(n)
    return inner_fun 


@ dec_fun
def fun(name):
    print(name)
    
# fun = dec_fun(fun)
fun("Raj")