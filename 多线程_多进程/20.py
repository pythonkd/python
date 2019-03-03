import threading
Sum = 0
loopsum = 1000000
def add():
    global Sum, loopsum
    for i in range(loopsum):
        Sum += 1

def minu():
    global Sum , loopsum
    for i in range(loopsum):
        Sum -= 1
if __name__ == "__main__":
    print('start sum={}'.format(Sum))
    t1 = threading.Thread(target=add, args=())
    t2 = threading.Thread(target=minu, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(Sum)