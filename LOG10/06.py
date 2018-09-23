import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def fun1():
    print("func1 starting......")
    lock_1.acquire()
    print("func1 acquir1 lock_1")
    time.sleep(2)
    print("func_1 等待lock_2")
    lock_2.acquire()
    print("func_1 acquire lock_2......")

    lock_2.release()
    print("func_1 relesse lock_2")

    lock_1.release()
    print("func1 release lock_1")

    print("func1 done......")


def func_2():
    print("func2 starting......")
    lock_2.acquire()
    print("func2 acquir1 lock_2")
    time.sleep(4)
    print("func_2 等待lock_1")
    lock_1.acquire()
    print("func_2 acquire lock_1......")

    lock_1.release()
    print("func_2 relesse lock_1")

    lock_2.release()
    print("func1 release lock_2")

    print("func1 done......")


if __name__ == '__main__':
    print("主程序启动")
    t1 = threading.Thread(target=fun1, args=())
    t2 = threading.Thread(target=func_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()
