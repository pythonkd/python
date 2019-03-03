import threading, time

class SayHi(threading.Thread):
    def __init__(self,name):
        super(SayHi, self).__init__()
        self.name = name

    def run(self):
        time.sleep(2)
        print("{} say hello".format(self.name))

if __name__ == '__main__':
    t = SayHi("lili")
    t.start()
    print("主线程")