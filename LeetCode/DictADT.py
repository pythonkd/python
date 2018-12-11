class Array(object):
    def __init__(self, size=32, init=None):
        self.size = size
        self.items = [init] * size
    def clear(self, value=None):
        for i in range(len(self)):
            self.items[i] = value
    def __len__(self):
        return self.size
    def __getitem__(self, index):
        return self.items[index]
    def __setitem__(self, index, value):
        self.items[index] = value
    def __iter__(self):
        for item in self.items:
            yield item
class Slot(object):
    def __init__(self, key=None, value=None):
        self.key, self.value = key, value
class HashTable(object):
    UNUSED = None
    EMPTY = Slot()
    def __init__(self):
        self._table = Array(8, init=HashTable.UNUSED)
        self.length = 0
    def __len__(self):
        return self.length
    def _hash(self, key):
        return abs(hash(key)) % len(self._table)
    @property
    def load_factor(self):
        return self.length / len(self._table)
    def find_key(self, key):
        index = self._hash(key)
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is not HashTable.EMPTY and self._table[index].key == key:
                return index
            index = (index*5+1)%len(self._table)
        return None
    def find_key_to_insert(self, key):
        index = self._hash(key)
        while self._table[index] not in (HashTable.UNUSED, HashTable.EMPTY):
            index = (index*5+1) % len(self._table)
        return index
    def add(self, key, value):
        if self.find_key(key):
            self._table[index].value = value
        else:
            index = self.find_key_to_insert(key)
            slot = Slot(key, value)
            self._table[index] = slot
        self.length += 1
        if self.load_factor >= 0.8:
            self._rehash_table()
    def _rehash_table(self):
        old_table = self._table
        newsize = len(self._table) * 2
        self._table = Array(newsize, HashTable.UNUSED)
        for i in old_table:
            if i not in (HashTable.UNUSED, HashTable.EMPTY):
                index = self.find_key_to_insert(i.key)
                self._table[index] = i
    def remove(self, key):
        index = self.find_key(key)
        if index is not None:
            self._table[index] = HashTable.EMPTY
            self.length -= 1
        else:
            raise KeyError('Not Found')
    def __iter__(self):
        for item in self._table:
            if item not in (HashTable.UNUSED, HashTable.EMPTY):
                yield (item.key, item.value)
    def __contains__(self, key):
        if self.find_key(key):
            return True
        return False
    def get(self, key, default=None):
        index = self.find_key(key)
        if  index is not None:
            return self._table[index].value
        return default
class DictADT(HashTable):
    def __setitem__(self, key, value):
        self.add(key, value)
    def __getitem__(self, key):
        return self.get(key)
    def items(self):
        for item in self:
            yield item
    def keys(self):
        for item in self:
            yield item[0]
    def values(self):
        for item in self:
            yield item[1]
def test():
    import random
    a = DictADT()
    a.add('a', 1)
    assert len(a) == 1
    assert a['a'] == 1
    a.remove('a')
    assert len(a) == 0
    l = list(range(30))
    random.shuffle(l)
    for i in l:
        a[i] = i
        assert a[i] == i
    assert len(a) == 30
    assert sorted(a.values()) == sorted(l)
    print('Successful')
if __name__ == "__main__":
    test()