import time

def deco(func):
    print("1111")
    def wrapper(a, b):

        startTime = time.time()
        func(a, b)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("->elapsed time:{} ms".format(msecs))
    return wrapper
@deco
def myfunc(a, b):
    print("start myfunc")
    time.sleep(0.6)
    print("result is {}".format(a+b))
    print("end myfunc")
print("myfunc is:",myfunc.__name__)
myfunc(3,5)