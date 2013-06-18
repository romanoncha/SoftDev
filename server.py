#!/usr/bin/env python
#-*- coding:utf-8 -*-

#с импортами думаю ничего сложного
import threading
from socket import socket, gethostbyname, AF_INET, SOCK_STREAM, error
import errno 
import sys
from ServerConsoleThread import *
from ClientThreading import *

# GLOBAL, тут глобальные переменные
global max_client
max_client = 20
global ConnClient
ConnClient = []
global ClientsLogins
ClientsLogins = []

class Server(object):

    def __init__(self,port):
        '''Base constructor'''
        self.port = port
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.count = 0

    def Start(self):
        '''Start Server'''
        self.port=1024#self.FindFreePort()
        try:
            self.sock.bind(("",self.port))
        except IOError,e:
            print e
            sys.exit("Sorry, error , can't create socket")
        print "Start OK, port = ", self.port
        self.sock.listen(max_client)

        self.consoleThread = ServerConsoleThread(self.sock)
        self.consoleThread.start()

        while True:
            self.conn, self.adrr = self.sock.accept()
            ConnClient.append(ClientThreading(self.conn,self.adrr))
            ConnClient[self.count].start()
            self.count += 1


    def Close(self):
        '''Finish work'''
        for conn in ConnClient:
            conn.Close()
        self.sock.close()
        sys.exit()

    def FindFreePort(self):
        '''Locks for free port'''
        for i in range(1024,5000):
            result = self.sock.connect_ex(("", i))
            if(result != 0):
                print "Free port ",i
                self.port = i