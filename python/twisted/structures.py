from collections import MutableMapping


class CaseInsensitiveDict(MutableMapping):

    def __init__(self, data=None, **kwargs):
        self._store = dict()
        if data is None:
            data = {}
        self.update(data, **kwargs)

    def __setitem__(self, key, value):
        self._store[key.lower()] = (key, value)

    def __getitem__(self, key):
        return self._store[key.lower()][1]

    def __delitem__(self, key):
        del self._store[key.lower()]

    def __iter__(self):
        return (k for k, _ in self._store.values())

    def __len__(self):
        return len(self._store)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, dict(self.items()))
