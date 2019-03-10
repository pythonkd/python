class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, sequence):
        node = self.root
        for item in sequence:
            if item in node.keys():
                node = node[item]
            else:
                node[item] = {}
                node = node[item]
        node['end'] = True

    def search(self, word):
        node = self.root
        for w in word:
            if w not in node.keys():
                return False
            else:
                node = node[w]
        mark = node.get('end')
        return mark is not None

    def startsWith(self, prefix):
        curnode = self.root
        for w in prefix:
            if w not in curnode.keys():
                return False
            curnode = curnode[w]
        return True
if __name__ == '__main__':
    t = Trie()
    t.insert('apple')
    assert not t.search('app')
    assert t.search('apple')
    t.insert('app')
    assert t.search('app')
    assert t.startsWith('app')