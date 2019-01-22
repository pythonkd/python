class Node(object):
    def __init__(self, value=None, next=None, previous=None):
        self.value, self.next, self.previous = value, next, previous


class CircularDoubleLinkedNode(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
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
        if self.maxsize is not None and self.value >= self.maxsize:
            raise Exception('Full')
        node = Node(value)
        tailnode = self.tailnode()
        tailnode.next = node
        node.next = self.root
        node.previous = tailnode
        self.length += 1
        self.root.previous = node

    def appendleft(self, value):
        if self.maxsize is not None and self.value >= self.maxsize:
            raise Exception('Full')
        node = Node(value)
        headnode = self.headnode()
        self.root.next = node
        node.next = headnode
        headnode.previous = node
        node.previous = self.root
        self.length += 1

    def pop(self):
        if self.root.next is self.root:
            return
        tailnode = self.tailnode()
        prevnode = tailnode.previous
        prevnode.next = self.root
        self.root.previous = prevnode
        value = tailnode.value
        del tailnode
        self.length -= 1
        return value

    def popleft(self):
        if self.root.next is self.root:
            return
        headnode = self.headnode()
        self.root.next = headnode.next
        headnode.next.previous = self.root
        value = headnode.value
        del headnode
        self.length -= 1
        return value

    def __iter__(self):
        for node in self._iter_node():
            yield node.value

    def _iter_node(self):
        curnode = self.root.next
        while curnode is not self.root:
            yield curnode
            curnode = curnode.next

    def remove(self, node):
        if self.root.next is self.root:
            raise Exception('remove empty CircularDoubleLinkedNode')
        prevnode = node.previous
        nextnode = node.next
        prevnode.next = nextnode
        nextnode.previous = prevnode
        del node
        self.length -= 1

    def reverse_node(self):
        curnode = self.root.previous
        while curnode is not self.root:
            yield curnode
            curnode = curnode.previous


class Stack(object):
    def __init__(self):
        self._items = CircularDoubleLinkedNode()

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0


def test_Stack():
    s = Stack()
    for i in range(10):
        s.push(i)
    assert len(s) == 10
    assert s.pop() == 9
    assert s.pop() == 8
    assert len(s) == 8


if __name__ == "__main__":
    test_Stack()