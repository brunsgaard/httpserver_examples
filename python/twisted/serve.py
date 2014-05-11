from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineReceiver
#from twisted.python import log
from models import Request


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
            self._header += '\n' + line
        elif ':' in line:
            if self._cheader:
                self.headerReceived(self._cheader)
            self._cheader = line

    def headerReceived(self, rawheader):
        try:
            key, value = rawheader.split(":", 1)
            self.request.headers[key] = value
        except:
            self.badRequest()

    def emptyLineReceived(self):
        print('emptyLineReceived')
        print(self.request)
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

#        if line == b'':
#            self.transport.write('HTTP/1.1 200 OK\n')
#            self.transport.write('Content-Length: 42\n')
#            self.transport.write('Content-Type: text/plain\n\r\n\r')
#            self.transport.write('abcdefghijklmnoprstuvwxyz1234567890abcdef')
#            #self.transport.loseConnection()
#            print('hej')
#        return
