
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
        while True:
            self.data = self.sock.recv(1024)
            print self.data
