from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineReceiver
#from twisted.python import log
from models import Request

# No persistent connections
# No pipeline
# Only serve text data for now

class HTTPProtocol(LineReceiver):

    request = None
    _cheader = ''

    def lineReceived(self, line):

        if not self.request:
            parts = line.split()
            if len(parts) == 3:
                self.request = Request(*parts)
            else:
                self.badRequest()
                return

        elif line == '':
            if self._cheader:
                self.headerReceived(self._cheader)
            self.emptyLineReceived()
        elif line[0] in ' \t':
            self._cheader += '\n' + line
        elif ':' in line:
            if self._cheader:
                self.headerReceived(self._cheader)
            self._cheader = line

    def headerReceived(self, rawheader):
        try:
            # move this to HeaderClass, also keep raw data,
            # just for good measures
            key, value = rawheader.split(":", 1)
            key = (key.strip()).lower()
            value = ' '.join((s.strip() for s in value.splitlines()))
            self.request.headers[key] = value
        except:
            self.badRequest()

    def emptyLineReceived(self):
        print(self.request)
        from pprint import pprint
        pprint(self.request.headers.items())
        self.transport.loseConnection()

    def badRequest(self):
        self.transport.write(b'HTTP/1.1 400 Bad Request\n\r\n\r')
        self.transport.loseConnection()


class HTTPFactory(ServerFactory):
    protocol = HTTPProtocol


if __name__ == "__main__":
    from twisted.internet import reactor
    # import sys
    # log.startLogging(sys.stdout)
    reactor.listenTCP(8080, HTTPFactory())
    reactor.run()

# EXAMPLE that works with persistent connections
#        if line == b'':
#            self.transport.write('HTTP/1.1 200 OK\n')
#            self.transport.write('Content-Length: 42\n')
#            self.transport.write('Content-Type: text/plain\n\r\n\r')
#            self.transport.write('abcdefghijklmnoprstuvwxyz1234567890abcdef')
#            #self.transport.loseConnection()
#            print('hej')
#        return
