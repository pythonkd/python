import threading
import time

class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()#一定不要忘记写  为了使用父类的__init__
        self.arg=arg

    # 必须重写run函数，润函数代表的是真正执行的函数
    def run(self):
        time.sleep(2)
        print("The args for this class is {}".format(self.arg))

for i in range(5):
    t=MyThread(i)
    t.start()
    t.join()

print("Main thread is done!!!")