
#-*- coding:utf-8 -*-
from socket import *

class Client(object):
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
    def connect(self, host, port):
        self.sock.connect((host, port))
    def send(self,mess):
        self.sock.send(mess)
        if mess == "exit_":
            self.sock.close()
    def receive(self):
        while True:
            result = self.sock.recv(1024)
            print result
            