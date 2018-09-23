import time

def deco(arg = True):
    if arg:
        def _deco(func):
            def wrapper(*args, **kw):
                startTime = time.time()
                func(*args, **kw)
                endTime = time.time()
                msecs = (endTime - startTime)*1000
                print("->elapsed time:{} ms".format(msecs))
            return wrapper
    else :
        def _deco(func):
            return func
    return _deco

@deco(False)
def myfunc():
    print("start myfunc")
    time.sleep(0.6)
    print("end myfunc")

@deco(True)
def addfunc(a, b):
    print("start addfunc")
    time.sleep(0.6)
    print("result is {}".format(a+b))
    print("end addfunc")

if __name__ == '__main__':
    myfunc()
    addfunc(3,6)