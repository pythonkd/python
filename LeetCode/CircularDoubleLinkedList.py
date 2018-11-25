class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoubleLinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        if self.maxsize is not None and self.length >= self.maxsize:
            raise Exception('full')
        node = Node(value)
        tailnode = self.root.prev or self.root

        node.prev = tailnode
        node.next = self.root
        tailnode.next = node
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and self.length >= self.maxsize:
            raise Exception('full')
        node = Node(value)
        if self.root.next is self.root:
            self.root.next = node
            node.next = self.root
            self.root.prev = node
            node.prev = self.root
        else:
            headnode = self.root.next
            node.next = headnode
            node.prev = self.root
            headnode.prev = node
            self.root.next = node
        self.length += 1

    def remove(self, node):
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next == self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        if self.root.prev == self.root:
            return
        else:
            curnode = self.root.prev
            while curnode.prev is not self.root:
                yield curnode
                curnode = curnode.prev
            yield curnode


def test():
    dll = CircularDoubleLinkedList()
    assert len(dll) == 0
    for i in range(5):
        dll.append(i)
    assert len(dll) == 5
    assert list(dll) == [0, 1, 2, 3, 4]
    assert [node.value for node in dll.iter_node()] == [0, 1, 2, 3, 4]
    assert [node.value for node in dll.iter_node_reverse()] == [4, 3, 2, 1, 0]
    assert dll.headnode().value == 0
    dll.remove(dll.headnode())
    assert len(dll) == 4
    assert dll.headnode().value == 1
    assert [i for i in dll] == [1, 2, 3, 4]
    dll.appendleft(0)
    assert [i for i in dll] == [0, 1, 2, 3, 4]
    print('success')


if __name__ == '__main__':
    test()