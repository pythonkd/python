class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None
class LinkedNode(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.length = 0
        self.tailnode = None
    def __len__(self):
        return self.length
    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('full')
        node = Node(value)
        if self.root.next is None:
            self.tailnode = node
            self.root.next = self.tailnode
        else:
            curnode = self.tailnode
            curnode.next = node
            self.tailnode = node
        self.length += 1
    def append_left(self, value):
        node = Node(value)
        headnode = self.root.next
        self.root.next = node
        node.next = headnode
        self.length += 1
    def iter_node(self):
        curnode = self.root.next
        while curnode:
            yield curnode
            curnode = curnode.next
    def __iter__(self):
        for node in self.iter_node():
            yield node.value
    def remove(self, value):
        prevnode = self.root
        while prevnode:
            curnode = prevnode.next
            if (curnode is not None) and (curnode.value == value):
                prevnode.next = curnode.next
                self.length -= 1
                return 1
            prevnode = prevnode.next
        return -1
    def popleft(self):
        headnode = self.root.next
        if headnode is None:
            raise Exception('pop from empty LinkedList')
        val = headnode.value
        self.root.next = headnode.next
        self.length -= 1
        del headnode
        return val
    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0
    def find(self, value):
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1
class Queue(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_linked_list = LinkedNode()
    def __len__(self):
        return len(self._item_linked_list)
    def push(self,value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('full')
        return self._item_linked_list.append(value)
    def pop(self):
        if len(self) == 0:
            raise Exception('queue empty')
        return self._item_linked_list.popleft()
def test_queue():
    q = Queue()
    for i in range(3):
        q.push(i)
    assert q.pop() == 0
    assert q.pop() == 1
    assert q.pop() == 2
    assert len(q) == 0
    print("successful")
if __name__ == "__main__":
    test_queue()