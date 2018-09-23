from functools import wraps

def coroutine(func):
    @wraps(func)
    def primer(*args, **kw):
        gen = func(*args, **kw)
        next(gen)
        return gen
    return primer

@coroutine
def simple_coro(a):
    print(a)
    a = yield
    print(a+a)
s = simple_coro(12)
try:
    s.send(3)
except StopIteration as exc:
    print(exc.value)
