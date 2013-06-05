
#-*- coding:utf-8 -*-
from socket import *

class Client(object):
    def __init__(self):
        print "afr"
        self.sock = socket(AF_INET, SOCK_STREAM)

    def connect(self, host, port):
        
        self.sock.connect((host, port))
    def login(self,login):
        self.sock.send("fd")