# -*- coding: utf-8 -*-
class Array(object):

    def __init__(self, size=16, init=None):
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
        for i in len(self):
            self._items[i] = init


class Slot(object):

    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable(object):
    UNUSED = None
    EMPTY = Slot(None, None)

    def __init__(self):
        self._table = Array(8, HashTable.UNUSED)
        self.length = 0

    def __len__(self):
        return self.length

    @property
    def _loadfactor(self):
        return self.length / float(len(self._table))

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def slot_can_insert(self, index):
        return self._table[index] is HashTable.UNUSED or self._table[index] is HashTable.EMPTY

    def find_slot_for_insert(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while not self.slot_can_insert(index):
            index = (index * 5 + 1) % _len
        return index

    def find_key(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is not HashTable.EMPTY and self._table[index].key == key:
                return index
            index = (index * 5 + 1) % _len
        return None

    def __contains__(self, key):
        return self.find_key(key) is not None

    def add(self, key, value):
        if key in self:
            index = self.find_key(key)
            self._table[index].value = value
            return False
        else:
            index = self.find_slot_for_insert(key)
            self._table[index] = Slot(key, value)
            self.length += 1
            if self._loadfactor >= 0.8:
                self._rehash()
            return True

    def _rehash(self):
        old_table = self._table
        new_size = len(self._table) * 2
        self._table = Array(new_size, HashTable.UNUSED)
        self.length = 0
        for slot in old_table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                key = slot.key
                index = self.find_slot_for_insert(key)
                self._table[index] = slot
                self.length += 1

    def get(self, key, default=None):
        index = self.find_key(key)
        if index is not None:
            return self._table[index].value
        else:
            return default

    def remove(self, key):
        index = self.find_key(key)
        if index is None:
            raise KeyError()
        value = self._table[index].value
        self._table[index] = HashTable.EMPTY
        self.length -= 1
        return value

    def __iter__(self):
        for slot in self._table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                yield slot.key


class Dict(HashTable):
    def _iter_slot(self):
        for slot in self._table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                yield slot

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
       if key not in self:
           raise KeyError()
       else:
           return self.get(key)

    def items(self):
        for slot in self._iter_slot():
            yield(slot.key, slot.value)

    def keys(self):
        for slot in self._iter_slot():
            yield slot.key

    def values(self):
        for slot in self._iter_slot():
            yield slot.value

def test_dict():
    d = Dict()
    d['a'] = 0
    d['b'] = 1
    d['c'] = 2
    assert d['a'] == 0
    assert sorted(list(d.keys())) == ['a', 'b', 'c']
    assert sorted(list(d.values())) == [0,1,2]

if __name__ == "__main__":
    test_dict()
