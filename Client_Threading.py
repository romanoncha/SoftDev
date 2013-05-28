#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
import threading
from Server import *


class ClientThreading(threading.Thread):
    def __init__(self, clientSock, addr, ConnClient ):
        
        self.clientSock = clientSock
        self.addr = addr
        threading.Thread.__init__(self)
        self.ConnClient = ConnClient[:]
    def run (self):
        while True:
            self.data = self.clientSock.recv(1024)
            for client in self.ConnClient:
                if client == self:
                    continue
                else:
                    client.clientSock.send(self.data)
            
    def Close(self):
        self.clientSock.close()
        