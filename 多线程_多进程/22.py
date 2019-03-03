import multiprocessing
import time

class Clockprocess(multiprocessing.Process):

    def __init__(self, interval):
        self.interval = interval
        super(Clockprocess, self).__init__()

    def run(self):
        while True:
            print("The time is {}".format(time.ctime()))
            time.sleep(self.interval)

if __name__ == '__main__':
    p = Clockprocess(5)
    p.start()