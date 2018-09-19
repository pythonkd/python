import multiprocessing
import time
class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        super().__init__()
        self.interval = interval
    def run(self):
        while True:
            print("The time is %s" % time.ctime())
            time.sleep(self.interval)
if __name__ == "__main__":
    p = ClockProcess(3)
    p.start()
    p.join()