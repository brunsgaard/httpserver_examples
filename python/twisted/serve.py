from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineReceiver
from twisted.python import log


class HTTPProtocol(LineReceiver):

    #delimiter = b'\n'  # defaults to b'\r\n'
    is_first_line = True

    def lineReceived(self, line):

        if line == b'':
            self.transport.write('HTTP/1.1 200 OK\n')
            self.transport.write('Content-Length: 42\n')
            self.transport.write('Content-Type: text/plain\n\r\n\r')
            self.transport.write('abcdefghijklmnoprstuvwxyz1234567890abcdef')
            #self.transport.loseConnection()
            print('hej')
        return

#        if self.is_first_line:
#            parts = line.split()
#            if len(parts) != 3:
#                self.transport.write('HTTP/1.1 400 Bad Request\n\r\n\r')
#                self.transport.loseConnection()
#                return
#
#            command, request, version = parts
#            self._command = command
#            self._path = request
#            self._version = version
#            self.is_first_line = False
#            self.sendLine(line)
#        elif line == b'':
#            print('done')
#            self.transport.loseConnection()
#        else:
#            self.sendLine('H: ' + line)

        #self.transport.loseConnection()




class HTTPFactory(ServerFactory):
    protocol = HTTPProtocol

if __name__ == "__main__":
    from twisted.internet import reactor
    import sys
    #log.startLogging(sys.stdout)
    reactor.listenTCP(8080, HTTPFactory())
    reactor.run()
