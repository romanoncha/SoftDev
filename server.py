#!/usr/bin/env python
#-*- coding:utf-8 -*-

import threading
from socket import socket, gethostbyname, AF_INET, SOCK_STREAM
import errno
from socket import error
import sys

# GLOBAL
busyportlist = []
freeportlist = []
max_client = 20


ConnClient = []
ClientsLogins = []

class Server(object):

    def __init__(self,port):
        '''Base constructor'''
        self.port = port
        self.sock = socket.socket(AF_INET, SOCK_STREAM)
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
            ConnClient.append(ClientThreading(self.conn,self.adrr))
            ConnClient[self.count].start()
            self.count += 1


    def Close(self):
        '''Finish work'''
        for conn in ConnClient:
            conn.Close()
        self.sock.close()

    def FindFreePort(self):
        '''Locks for free port'''
        for i in range(1024,5000):
            result = self.sock.connect_ex(("", i))
            if(result != 0):
                print "Free port ",i
                self.port = i
                break

import socket
import threading
from Server import *

#Client_Threading CLASS
class ClientThreading(threading.Thread):
    def __init__(self, clientSock, addr):

        self.clientSock = clientSock
        self.addr = addr
        threading.Thread.__init__(self)
    def run (self):
        self.Autorization()
        while True:
            self.data = self.clientSock.recv(1024)
            for client in ConnClient:
                if client == self:
                    continue
                else:
                    mess = self.login + ": " + self.data
                    client.clientSock.send(mess)

    def Close(self):
        self.clientSock.close()
    def Autorization(self):
        self.clientSock.send("Hello user, first you must login\n")
        while True:
            self.login = self.clientSock.recv(1024)
            if self.login in ClientsLogins:
                self.clientSock.send("Sorry, this login is already used, try again\n")
                continue
            elif len(ClientsLogins) >= max_client:
                self.clientSock.send("Sorry, server is overload. Try later\n")
                continue

            self.clientSock.send("Welcome to our chat "+self.login+"\n")
            ClientsLogins.append(self.login)
            break
