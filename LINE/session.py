# -*- coding: utf-8 -*-
from Thrift.transport import THttpClient
from Thrift.protocol import TCompactProtocol
from ThriftService import TalkService, ChannelService, CallService#, SquareService

class LineSession:

    def __init__(self, url, headers, path=''):
        self.host = url + path
        self.headers = headers

    def Talk(self, isopen=True):
        self.transport = THttpClient.THttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)
        
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._talk  = TalkService.Client(self.protocol)
        
        # if isopen:
        #     self.transport.open()

        return self._talk

    def Channel(self, isopen=True):
        self.transport = THttpClient.THttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)

        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._channel  = ChannelService.Client(self.protocol)
        
        # if isopen:
        #     self.transport.open()

        return self._channel

    def Call(self, isopen=True):
        self.transport = THttpClient.THttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)

        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._call  = CallService.Client(self.protocol)
        
        # if isopen:
        #     self.transport.open()

        return self._call

    def Square(self, isopen=True):
        self.transport = THttpClient.THttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)

        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        #self._square  = SquareService.Client(self.protocol)
        
        # if isopen:
        #     self.transport.open()

        #return self._square