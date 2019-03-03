def average():
    total = 0.0
    count = 0
    pivot = 0
    while True:
        total += yield pivot
        count += 1
        pivot = total / count

if __name__ == '__main__':
    t = average()
    next(t)
    print(t.send(10))
    print(t.send(20))
    print(t.send(30))
