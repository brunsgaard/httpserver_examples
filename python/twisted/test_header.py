from serve import HTTPProtocol
from twisted.web import http



headerdata = """GET / HTTP/1.1
Date     :  27 Aug 76 0932 PDT
From     :  Ken Davis <KDavis@This-Host.This-net>
Subject  :  Re: The Syntax in the RFC
Sender   :  KSecy@Other-Host
Reply-To :  Sam.Irving@Reg.Organization
To       :  George Jones <Group@Some-Reg.An-Org>,
            Al.Neuman@MAD.Publisher
cc       :  Important folk:
              Tom Softwood <Balsa@Tree.Root>,
              "Sam Irving"@Other-Host;,
            Standard Distribution:
              /main/davis/people/standard@Other-Host,
              "<Jones>standard.dist.3"@Tops-20-Host>;
Comment  :  Sam is away on business. He asked me to handle
            his mail for him.  He'll be able to provide  a
            more  accurate  explanation  when  he  returns
            next week.
In-Reply-To: <some.string@DBM.Group>, George's message
X-Special-action:  This is a sample of user-defined field-
 names.  There could also be a field-name
 "Special-action", but its name might later be
 preempted
Message-ID: <4231.629.XYzi-What@Other-Host>

"""

lines = headerdata.splitlines()

class DummyTansport(object):

    def loseConnection(self):
        pass

p = HTTPProtocol()
p.transport = DummyTansport()
for line in lines:
    p.lineReceived(line)
