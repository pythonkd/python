import threading
sum = 0
loopsum = 100000

lock = threading.Lock()

def myadd():
    global sum, loopsum

    for i in range(1,loopsum):
        lock.acquire()
        sum += 1
        lock.release()

def myMinu():
    global sum, loopsum
    for i in range(1, loopsum):
        lock.acquire()
        sum -= 1
        lock.release()

if __name__ == '__main__':
    print("Starting ......{}".format(sum ))
    t1 = threading.Thread(target=myadd(), args=())
    t2 = threading.Thread(target=myMinu(), args=())
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done .....{}".format(sum))