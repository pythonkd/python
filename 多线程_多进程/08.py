import time
import threading

def loop1():
    print("Start loop 1 at: {}".format(time.ctime()))

    time.sleep(4)
    print('End loop 1 at:{}'.format(time.ctime()))

def loop2():
    print('Start loop 2 at:{}'.format(time.ctime()))

    time.sleep(2)
    print("End loop 2 at:{}".format(time.ctime()))


def loop3():
    print('Start loop 3 at:{}'.format(time.ctime()))
    time.sleep(5)
    print("End loop 3 at:{}".format(time.ctime()))

def main():
    print("Start at:", time.ctime())

    t1 = threading.Thread(target=loop1, args=())
    t1.setName('Thr_1')
    t1.start()

    t2 = threading.Thread(target=loop2, args=())
    t2.setName('Thr_2')
    t2.start()

    t3 = threading.Thread(target=loop3, args=())
    t3.setName('Thr_3')
    t3.start()

    time.sleep(3)

    for thr in threading.enumerate():
        print("正在运行的线程名字是：",thr.getName())

    print("正在运行的线程数量为：{}".format(threading.activeCount()))

    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)
