from structures import CaseInsensitiveDict


class HeaderDict(CaseInsensitiveDict):
    pass


class Request(object):

    def __init__(self, command, path, version):
        self.command = command
        self.version = version
        self.path = path
        self.headers = HeaderDict()

    def __repr__(self):
        args = self.command, self.path, self.version
        return '<Request({},{},{})>'.format(*args)
