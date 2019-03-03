import time, threading
def loop1():
    print("loop1 start{}".format(time.ctime()))
    time.sleep(4)
    print("loop1 end {}".format(time.ctime()))
def loop2():
    print("loop2 start{}".format(time.ctime()))
    time.sleep(2)
    print("loop2 end {}".format(time.ctime()))

def main():
    start = time.time()
    print("**"*10)
    t1 = threading.Thread(target=loop1, args=())
    t1.setDaemon(True)
    t1.start()
    t2 = threading.Thread(target=loop2, args=())
    t2.start()
    # t1.join()
    # t2.join()
    end = time.time()
    print("程序共用了{}".format(end - start))
main()