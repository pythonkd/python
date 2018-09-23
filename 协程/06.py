from functools import wraps

def deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        next(a)
        return a
    return wrapper

@deco
def averager():
    # 使用协程求平均值
    total = 0.0
    count = 0
    average = None
    while True:

        term = yield average
        if term == Ellipsis:
            break
        total += term
        count += 1
        average = total/count
a = averager()
print(a.send(10))
print(a.send(20))
print(a.send(30))
print(a.send(Ellipsis))#哨符值

