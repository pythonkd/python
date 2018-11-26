class Array:
    def __init__(self, size=32):
        self._size = size
        self._items = [None]*32
    def __getitem__(self, index):
        return self._items[index]
    def __setitem__(self, index, value):
        self._items[index] = value
    def __len__(self):
        return self._size
    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value
    def __iter__(self):
        for i in self._items:
            yield i
class FullError(Exception):
    pass
class ArrayQueue:
    '''定长的队列，当队列满了之后再添加元素，会覆盖掉第一个添加的一个元素,从头开始添加。'''
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0
    def push(self, value):
        if len(self.array) > self.maxsize:
            raise FullError('The queue is full')
        self.array[self.head%self.maxsize] = value
        self.head += 1
    def pop(self):
        value = self.array[self.tail%self.maxsize]
        self.tail += 1
        return value
    def __len__(self):
        return self.head - self.tail
def test_array_queue():
    size = 5
    q = ArrayQueue(size)
    for i in range(size):
        q.push(i)
    assert len(q) == size
    assert q.pop() == 0
    assert q.pop() == 1
    q.push(5)
    assert len(q) == 4
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.pop() == 5
    assert len(q) == 0
    print('Test Successful')
if __name__ == "__main__":
    test_array_queue()