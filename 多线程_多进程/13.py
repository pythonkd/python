from multiprocessing import Process,current_process
import os
def info(title):
    print(title)
    print("module name: ",__name__)
    print("父进程ID",os.getppid())
    print("子进程ID",os.getpid(),current_process().name)

def f(name):
    info("function f")
    print('hello',name)

if __name__ == '__main__':
    info("main line")
    p = Process(target=f, args=("bob",),name="subProcess1")
    p.start()
    p.join()