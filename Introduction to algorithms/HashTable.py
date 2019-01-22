class Array(object):

    def __init__(self, size=32, init=None):
        self.size = size
        self._items = [init] * size

    def __len__(self):
        return self.size

    def __setitem__(self, index, value):
        self._items[index] = value

    def __getitem__(self, index):
        return self._items[index]

    def __iter__(self):
        for item in self._items:
            yield item

    def clear(self, init=None):
        for i in range(len(self)):
            self._items[i] = init


class Slot(object):
    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable(object):
    UNUSED = None
    EMPTY = Slot(None, None)

    def __init__(self):
        self._table = Array(16, HashTable.UNUSED)
        self.length = 0

    def __len__(self):
        return self.length

    @property
    def _load_factor(self):
        return self.length / float(len(self._table))

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def slot_can_insert(self, index):
        return self._table[index] is HashTable.UNUSED or self._table[index] is HashTable.EMPTY

    def find_key(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is not HashTable.EMPTY and self._table[index].key == key:
                return index
            index = (index * 5 + 1) % _len
        return None

    def find_slot_to_insert(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while not self.slot_can_insert(index):
            index = ((index * 5) + 1) % _len
        return index

    def __contains__(self):
        return self.find_key(key) is not None

    def add(self, key, value):
        index = self.find_key(key)
        if index is not None:
            self._table[index].value = value
            return False
        else:
            index = self.find_slot_to_insert(key)
            self._table[index] = Slot(key, value)
            self.length += 1
            if self._load_factor >= 0.8:
                self._rehash()
            return True

    def _rehash(self):
        old_table = self._table
        newsize = len(self._table)
        self._table = Array(newsize, HashTable.UNUSED)
        self.length = 0
        for slot in old_table:
            if slot is not HashTable.UNUSED or slot is not HashTable.EMPTY:
                index = self.find_slot_to_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def remove(self, key):
        index = self.find_key(key)
        if index is None:
            raise KeyError()
        else:
            value = self._table[index].value
            self._table[index] = HashTable.EMPTY
            self.length -= 1
            return value

    def get(self, key, default=None):
        index = self.find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value

    def __iter__(self):
        for slot in self._table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                yield slot.key


def test_Hash_Table():
    h = HashTable()
    h.add('a', 1)
    h.add('b', 2)
    h.add('c', 3)
    assert len(h) == 3
    assert h.get('b') == 2
    h.add('b', -1)
    assert len(h) == 3
    assert h.get('b') == -1
    assert h.remove('b') == -1
    assert len(h) == 2


if __name__ == "__main__":
    test_Hash_Table()