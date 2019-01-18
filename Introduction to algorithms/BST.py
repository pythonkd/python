BST_node_date = [
    {'key': 60, 'left': 12, 'right': 90, 'is_root': True},
    {'key': 12, 'left': 4, 'right': 41, 'is_root': False},
    {'key': 90, 'left': 71, 'right': 100, 'is_root': False},
    {'key': 4, 'left': 1, 'right': None, 'is_root': False},
    {'key': 41, 'left': 29, 'right': None, 'is_root': False},
    {'key': 71, 'left': None, 'right': 84, 'is_root': False},
    {'key': 100, 'left': None, 'right': None, 'is_root': False},
    {'key': 1, 'left': None, 'right': None, 'is_root': False},
    {'key': 29, 'left': 23, 'right': 37, 'is_root': False},
    {'key': 84, 'left': None, 'right': None, 'is_root': False},
    {'key': 23, 'left': None, 'right': None, 'is_root': False},
    {'key': 37, 'left': None, 'right': None, 'is_root': False}
]


class BST_node(object):
    def __init__(self, key, value, left=None, right=None):
        self.key, self.value, self.left, self.right = key, value, left, right


class BST(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, BST_node_date):
        cls.size = 0
        node_dict = {}
        for node_data in BST_node_date:
            key = node_data['key']
            node_dict[key] = BST_node(key, value=key)

        for node_data in BST_node_date:
            key = node_data['key']
            node = node_dict[key]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
            cls.size += 1
        return cls(root)

    def _bst_search(self, subtree, key):
        if subtree is None:
            return None
        elif subtree.key > key:
            return self._bst_search(subtree.left, key)
        elif subtree.key < key:
            return self._bst_search(subtree.right, key)
        else:
            return subtree

    def __contains__(self, key):
        return self._bst_search(self.root, key) is not None

    def get(self, key, default=None):
        node = self._bst_search(self.root, key)
        if node is None:
            return default
        else:
            return node.value

    def _bst_min_node(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bst_min_node(subtree.left)

    def bst_min(self):
        node = self._bst_min_node(self.root)
        return node.value if node else None

    def _bst_max_node(self, subtree):
        if subtree is None:
            return None
        elif subtree.right is None:
            return subtree
        else:
            return self._bst_max_node(subtree.right)

    def bst_max(self):
        node = self._bst_max_node(self.root)
        return node.value if node else None

    def _bst_insert(self, subtree, key, value):
        if subtree is None:
            subtree = BST_node(key, value)
        elif subtree.key > key:
            subtree.left = self._bst_insert(subtree.left, key, value)
        elif subtree.key < key:
            subtree.right = self._bst_insert(subtree.right, key, value)
        return subtree

    def add(self, key, value):
        node = self._bst_search(self.root, key)
        if node is not None:
            node.value = value
            return False
        else:
            self.root = self._bst_insert(self.root, key, value)
            self.size += 1
            return True

    def _bst_remove(self, subtree, key):
        if subtree is None:
            return None
        elif subtree.key < key:
            subtree.right = self._bst_remove(subtree.right, key)
            return subtree
        elif subtree.key > key:
            subtree.left = self._bst_remove(subtree.left, key)
            return subtree
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:
                successor_node = self._bst_min_node(subtree.right)
                subtree.key, subtree.value = successor_node.key, successor_node.value
                subtree.right = self._bst_remove(subtree.right, successor_node.key)
                return subtree

    def remove(self, key):
        assert key in self
        self.size -= 1
        return self._bst_remove(self.root, key)

    def preorder_traversal(self, subtree):
        if subtree is not None:
            self.preorder_traversal(subtree.left)
            print(subtree.key, subtree.value)
            self.preorder_traversal(subtree.right)

    def reverse(self, subtree):
        if subtree is not None:
            subtree.left, subtree.right = subtree.right, subtree.left
            self.reverse(subtree.left)
            self.reverse(subtree.right)


# bst = BST.build_from(BST_node_date)
# bst.add(120, 120)
# bst.add(0, 0)
# bst.add(3,3)
# bst.preorder_traversal(bst.root)
# bst.remove(3)
# bst.remove(90)
# bst.remove(60)
# bst.remove(0)
# bst.preorder_traversal(bst.root)
def test_bst_tree():
    bst = BST.build_from(BST_node_date)
    for node_dict in BST_node_date:
        key = node_dict['key']
        assert bst.get(key) == key
    assert bst.size == len(BST_node_date)
    assert bst.get(-1) is None  # 单例的 None 我们用 is 来比较

    assert bst.bst_min() == 1

    bst.add(0, 0)
    assert bst.bst_min() == 0

    bst.remove(12)
    assert bst.get(12) is None

    bst.remove(1)
    assert bst.get(1) is None

    bst.remove(29)
    assert bst.get(29) is None


if __name__ == "__main__":
    test_bst_tree()