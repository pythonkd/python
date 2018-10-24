def add_b():
    global b
    b = 42
    def do_global():
        global b
        b += 10
        print(b)
    do_global()
    print(b)
add_b()
print(b)