def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
    return "Done"

g = fib(5)
for i in g:
    print(i)