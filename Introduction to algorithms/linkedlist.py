class Node(object):

    def __init__(self, value=None, Next=None):
        self.value, self.next = value, Next

    def __str__(self):
        return "<Node: value:{}, next:{} >".format(self.value, self.next)

    __repr__ = __str__


class LinkedList(object):

    def __init__(self, maxsize=None):
        self.root = Node()
        self.tailnode = None
        self.maxsize = maxsize
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

    def appendleft(self, value):
        if self.maxsize is not None and self.length >= self.maxsize:
            raise Exception('Full')
        node = Node(value)
        if self.tailnode is None:
            self.root.next = node
            self.tailnode = node
        headnode = self.root.next
        node.next = headnode
        self.root.next = node
        self.length += 1

    def __iter__(self):
        for node in self._iter_node():
            yield node.value

    def _iter_node(self):
        curnode = self.root.next
        while curnode is not self.tailnode:  # 从第一个节点开始遍历
            yield curnode
            curnode = curnode.next  # 移动到下一个节点
        if curnode is not None:
            yield curnode

    def find(self, value):
        index = 0
        for node in self._iter_node():
            if node.value == value:
                return index
            index += 1
        return -1

    def remove(self, value):
        prevnode = self.root
        for curnode in self._iter_node():
            if curnode.value == value:
                prevnode.next = curnode.next
                self.length -= 1
                if curnode is self.tailnode:
                    self.tailnode = prevnode
                del curnode
                return 1
            prevnode = curnode
        return -1

    def popleft(self):
        if self.root.next is None:
            raise Exception('The LinkedList is Empty')
        headnode = self.root.next
        self.root.next = headnode.next
        value = headnode.value
        if headnode is self.tailnode:
            self.tailnode = None
        self.length -= 1
        del headnode
        return value

    def clear(self):
        for node in self._iter_node():
            del node
        self.length = 0
        self.root.next = None
        self.tailnode = None

    def reverse(self):
        curnode = self.root.next
        self.tailnode = curnode
        prevnode = None

        while curnode:
            nextnode = curnode.next
            curnode.next = prevnode

            if nextnode is None:
                self.root.next = curnode

            prevnode = curnode
            curnode = nextnode


def test_linked_list():
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)

    assert len(ll) == 4
    assert ll.find(2) == 2
    assert ll.find(-1) == -1

    assert ll.remove(0) == 1
    assert ll.remove(10) == -1
    assert ll.remove(2) == 1
    assert len(ll) == 2
    assert list(ll) == [1, 3]
    assert ll.find(0) == -1

    ll.appendleft(0)
    assert list(ll) == [0, 1, 3]
    assert len(ll) == 3

    headvalue = ll.popleft()
    assert headvalue == 0
    assert len(ll) == 2
    assert list(ll) == [1, 3]

    assert ll.popleft() == 1
    assert list(ll) == [3]
    ll.popleft()
    assert len(ll) == 0
    assert ll.tailnode is None

    ll.clear()
    assert len(ll) == 0
    assert list(ll) == []


def test_linked_list_remove():
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.remove(7)
    print(list(ll))


def test_linked_list_reverse():
    ll = LinkedList()
    n = 10
    for i in range(n):
        ll.append(i)
    # print(list(ll))
    ll.reverse()
    #     print(list(ll))
    assert list(ll) == list(reversed(range(n)))


def test_linked_list_append():
    ll = LinkedList()
    ll.appendleft(1)
    ll.append(2)
    assert list(ll) == [1, 2]


if __name__ == '__main__':
    test_linked_list()
    test_linked_list_append()
    test_linked_list_reverse()