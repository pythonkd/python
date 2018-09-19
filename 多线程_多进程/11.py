import multiprocessing
from time import ctime,sleep
def clock(interval):
    while True:
        print("The time is %s" % ctime())
        sleep(interval)
if __name__ == "__main__":
    p = multiprocessing.Process(target=clock, args=(5,))
    p.start()
    p.join()