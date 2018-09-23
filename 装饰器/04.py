import time

def deco_1(func):
    print("enter into deco_1")
    print(func)
    def wrapper(*args, **kw):
        print("enter into deco_1_wrapper")
        return func(*args, **kw)
    return wrapper

def deco_2(func):
    print(func)
    print("enter into deco_2")
    def wrapper(*args, **kw):
        print("enter into deco_2_wrapper")
        return func(*args, **kw)
    return wrapper

@deco_1
@deco_2
def addfunc(a,b):
    print("result is ",(a + b))

addfunc(2,3)