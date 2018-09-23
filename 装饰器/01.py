from functools import wraps
import time
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kw):
        '''decorator'''
        print("Calling {} is time:{}".format(func.__name__,time.ctime()))
        return func(*args, **kw)
    return wrapper
@my_decorator
def a():
    '''dectoring'''
    print("my name is A")

if __name__ == '__main__':
    a()
    print(a.__name__,a.__doc__)