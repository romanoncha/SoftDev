
#-*- coding:utf-8 -*-
from socket import *

class Client(object):
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
    def connect(self, host, port):
        self.sock.connect((host, port))
    def login(self,login):
        self.sock.send(login)
    def receive(self):
        msg = ''
        while True:
            chunk = self.sock.recv(1024)
            if chunk == '':
                raise RuntimeError("socket connection broken")
            msg = msg + chunk
        print msg