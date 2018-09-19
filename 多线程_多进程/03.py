import time
import _thread as thread

def loop1(in1):
    print("Start loop 1 at: {}".format(time.ctime()))

    print("我是参数：",in1)

    time.sleep(4)
    print('End loop 1 at:{}'.format(time.ctime()))

def loop2(in1, in2):
    print('Start loop 2 at:{}'.format(time.ctime()))
    print("我是参数1：",in1,'我是参数2:',in2)
    time.sleep(2)
    print("End loop 2 at:{}".format(time.ctime()))

def main():
    print("Start at:",time.ctime())

    thread.start_new_thread(loop1,("王蒙蒙",))

    thread.start_new_thread(loop2,("王大脑袋", '大拿'))

    print("All done at:",time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
