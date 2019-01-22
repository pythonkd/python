class Node(object):

    def __init__(self, value=None, next=None):
        self.value, self.next = value, next


class LinkedNode(object):

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and self.length >= self.maxsize:
            raise Exception('Full')
        node = Node(value)
        if self.tailnode is None:
            self.root.next = node
        else:
            tailnode = self.tailnode
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def append_left(self, value):
        if self.maxsize is not None and self.length >= self.maxsize:
            raise Exception('Full')
        node = Node(value)
        if self.tailnode is None:
            self.root.next = node
            self.tailnode = node
        else:
            headnode = self.root.next
            self.root.next = node
            node.next = headnode
        self.length += 1

    def __iter__(self):
        for node in self._iter_node():
            yield node.value

    def _iter_node(self):
        curnode = self.root.next
        while curnode:
            yield curnode
            curnode = curnode.next

    def popleft(self):
        if self.tailnode is None:
            return
        headnode = self.root.next
        self.root.next = headnode.next
        value = headnode.value
        if headnode is self.tailnode:
            self.tailnode = None
        del headnode
        self.length -= 1
        return value


class Queue(object):
    def __init__(self, maxlen=None):
        self._items = LinkedNode()

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.popleft()

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item

    def empty(self):
        return len(self._items) == 0


def test():
    q = Queue()
    for i in range(5):
        q.push(i)
    assert list(q) == [i for i in range(5)]
    assert len(q) == 5
    for i in range(5):
        assert q.pop() == i
    assert len(q) == 0


if __name__ == "__main__":
    test()