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