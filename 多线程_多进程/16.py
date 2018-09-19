import multiprocessing
from time import ctime

def consumer(input_q):
    print("Into consumer:",ctime())
    while True:
        item = input_q.get()
        print("pull",item,"out of q")
        input_q.task_done()

def producer(sequence,output_q):
    print("Into producer:",ctime())
    for item in sequence:
        output_q.put(item)
        print("put",item,"into q")
    print("out of producer:",ctime())

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    cons_p1 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p1.start()

    cons_p2 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p2.start()

    sequence = [1,2,3,4]
    producer(sequence, q)

    q.put(None) #取出之后就会停止该子进程，不会再取出第二次
    q.put(None)

    cons_p1.join()
    cons_p2.join()