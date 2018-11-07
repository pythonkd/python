import collections
class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]
    def __contains__(self, key):
        return str(key) in self.date
    def __setitem__(self, key, item):
        print('setitem',item)
        self.data[str(key)] = item