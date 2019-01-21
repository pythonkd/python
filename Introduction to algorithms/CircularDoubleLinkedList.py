class Node(object):

    def __init__(self, value=None, next=None, previous=None):
        self.value, self.next, self.previous = value, next, previous

    def __str__(self):
        return '<Node: value:{}, next:{}, previous:{}>'.format(self.value, self.next, self.previous)

    __repr__ = __str__


class Circular_Double_LinkedList(object):

    def __init__(self, maxsize=None):
        self.root = Node()
        self.maxsize = maxsize
        self.root.next = self.root
        self.root.previous = self.root
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.previous

    def append(self, value):
        if self.maxsize is not None and self.length >= self.maxsize:
            raise Exception('Full')
        node = Node(value)
        tailnode = self.tailnode()
        tailnode.next = node
        node.next = self.root
        node.previous = tailnode
        self.root.previous = node
        self.length += 1

    def append_left(self, value):
        if self.maxsize is not None and self.length >= self.maxsize:
            raise Exception('Full')
        node = Node(value)
        headnode = self.headnode()
        self.root.next = node
        node.next = headnode
        node.previous = self.root
        headnode.previous = node
        self.length += 1

    def __iter__(self):
        for node in self._iter_node():
            yield node.value

    def _iter_node(self):
        curnode = self.headnode()
        while curnode is not self.root:
            yield curnode
            curnode = curnode.next

    def remove(self, node):
        if node is self.root:
            return
        prevnode = node.previous
        prevnode.next = node.next
        node.next.previous = prevnode
        value = node.value
        del node
        self.length -= 1
        return value

    def reverse_node(self):
        curnode = self.tailnode()
        while curnode is not self.root:
            yield curnode
            curnode = curnode.previous

    def pop(self):
        if self.root.next is self.root:
            return
        tailnode = self.tailnode()
        prevnode = tailnode.previous
        nextnode = tailnode.next
        prevnode.next = nextnode
        nextnode.previous = prevnode
        value = tailnode.value
        del tailnode
        self.length -= 1
        return value

    def popleft(self):
        if self.root.next is self.root:
            return
        headnode = self.headnode()
        prevnode = headnode.previous
        nextnode = headnode.next
        prevnode.next = nextnode
        nextnode.previous = prevnode
        value = headnode.value
        self.length -= 1
        del headnode
        return value


def test():
    dll = Circular_Double_LinkedList()
    for i in range(10):
        dll.append(i)
    assert len(dll) == 10
    assert list(dll) == [i for i in range(10)]
    dll.append_left(-1)
    assert list(dll) == [-1] + [i for i in range(10)]
    assert len(dll) == 11
    assert dll.pop() == 9
    assert dll.popleft() == -1
    assert len(dll) == 9


if __name__ == "__main__":
    test()