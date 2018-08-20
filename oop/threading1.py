import time ,threading

def loop():
    print('thread {} is running...'.format(threading.current_thread().name))
    n=0
    while n<5:
        n =n+1
        print('thread {} >>> {}'.format(threading.current_thread().name,n))
        time.sleep(1)
    print('thread {} ended.'.format(threading.current_thread().name))

print('thread {} is running...'.format(threading.current_thread().name))
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread {} ended.'.format(threading.current_thread().name))