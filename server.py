#!/usr/bin/env python
#-*- coding:utf-8 -*-

import threading
from socket import socket, gethostbyname, AF_INET, SOCK_STREAM
import errno
from socket import error
import sys
from Client_Threading import ClientThreading

# GLOBAL
busyportlist = []
freeportlist = []
max_client = 20


ConnClient = []

class Server(object):

    def __init__(self,port):
        '''Base constructor'''
        self.port = port
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.count = 0 

    def Start(self):
        '''Start Server'''
        self.FindFreePort()
        try:
            self.sock.bind(("",self.port))
        except IOError,e:
            print e
            sys.exit("Sorry, error , can't create socket")
        print "Start OK, port = ", self.port
        self.sock.listen(max_client)
        
        while True:
            self.conn, self.adrr = self.sock.accept()
            ConnClient.append(ClientThreading(self.conn,self.adrr,ConnClient))
            ConnClient[self.count].start()
            self.count += 1

            
    def Close(self):
        '''Finish work'''
        for conn in self.ConnClient:
            conn.Close()
        sock.close()

    def FindFreePort(self):
        '''Locks for free port'''
        for i in range(1024,5000):
            result = self.sock.connect_ex(("", i))
            if(result != 0):
                print "Free port ",i
                self.port = i
                break
