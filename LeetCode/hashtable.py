class Array(object):
    def __init__(self, size=30, init=None):
        self.size = size
        self.items = [init]*size
    def __getitem__(self, index):
        return self.items[index]
    def __setitem__(self, index, value):
        self.items[index] = value
    def __len__(self):
        return self.size
    def clear(self):
        for i in range(len(self.size)):
            self.items[i] = init
    def __iter__(self):
        for i in self.items:
            yield i
class Slot(object):
    def __init__(self, value=None, key=None):
        self.key, self.value = key, value
class HashTable(object):
    EMPTY = None
    UNUSED = None
    def __init__(self):
        self._table = Array(20, HashTable.UNUSED)
        self.length = 0
    @property
    def _load_factor(self):
        return self.length / len(self._table)
    def __len__(self):
        return self.length
    def _hash(self, key):
        return abs(hash(key)%len(self._table))
    def _find_key(self, key):
        index = self._hash(key)
        _len = self.length
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:
                index = (index*5 +1) % _len
                continue
            elif self._table[index].key == key:
                return index
            else:
                index = (index *5 + 1) / _len
        return None
    def _slot_can_insert(self, index):
        return (self._table[index] is HashTable.EMPTY or HashTable.UNUSED)
    def _find_slots_for_insert(self, key):
        index = self._hash(key)
        _len = self.length
        while not _slot_can_insert(index):
            index = (index*5 +1)%_len
        return index
    def __contains__(self, key):
        index = _find_key(key)
        return index is not None
    def add(self, key, value):
        if key in self:
            index = self._find_key(key)
            self._table[index].value = value
            return False
        else:
            index = _find_slots_for_insert(key)
            self._table[index] = Slot(value, key)
            self.length += 1
            if self._load_factor() >= 0.8:
                self._rehash()
            return True
    def rehash(self):
        old_table = self._table
        newsize = len(self) * 2
        self._table = Array(newsize, HashTable.UNUSED)
        self.length = 0
        for slot in old_table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                index = self._find_slots_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1
    def get(self, key, default=None):
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value
    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise KeyError()
        value = self._table[index].value
        self._table[index].key = HashTable.EMPTY
        self.length -= 1
        return value
    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot.key