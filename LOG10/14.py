import multiprocessing
from time import ctime

def consumer(input_q):
    print("Into consumer:", ctime())
    while True:
        item = input_q.get()
        print("pull",item,"out of q")
        input_q.task_done()
    print("Out of consumer:", ctime())

def producer(sequence, output_q):
    print("Into producer",ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item, "into q")
    print("Out of producer:",ctime())

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    cons_p = multiprocessing.Process(target=consumer,target=(q,))
    cons_p.daemon = True
    cons_p.start()

    sequence = [1,2,3,4]
    producer(sequence, q)
    q.join()