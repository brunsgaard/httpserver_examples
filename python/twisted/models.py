from collections import MutableMapping


class HeaderDict(MutableMapping):

    def __init__(self, data=None, **kwargs):
        self._store = dict()
        if data is None:
            data = {}
        self.update(data, **kwargs)

    def __setitem__(self, key, value):
        key = key.lower().strip()
        value = ' '.join((s.strip() for s in value.split()))
        if key in self._store:
            self._store[key].append(value)
        else:
            self._store[key] = [value]

    def __getitem__(self, key):
        key = key.lower().strip()
        return ', '.join(self._store[key])

    def __delitem__(self, key):
        del self._store[key.lower().strip()]

    def __iter__(self):
        return iter(self._store)

    def __len__(self):
        return len(self._store)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, dict(self.items()))


class Request(object):

    def __init__(self, command, path, version):
        self.command = command
        self.version = version
        self.path = path
        self.headers = HeaderDict()

    def __repr__(self):
        args = self.command, self.path, self.version
        return '<Request({},{},{})>'.format(*args)
