'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''
import time
import _thread as thread
def loop1():
    print('Start loop 1 at :{}'.format(time.ctime()))
    time.sleep(4)
    print('End loop 1 at :{}'.format(time.ctime()))

def loop2():
    print('Start loop 2 at {}'.format(time.ctime()))
    time.sleep(2)
    print('End loop 2 at :{}'.format(time.ctime()))

def main():
    print("Start at:{}".format(time.ctime()))
    thread.start_new(loop1,())
    thread.start_new(loop2,())
    print("All done at:{}".format(time.ctime()))

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)