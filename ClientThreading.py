#!/usr/bin/env python
#-*- coding:utf-8 -*-
import threading
import server

class ClientThreading(threading.Thread):
    def __init__(self, clientSock, addr):

        self.clientSock = clientSock
        self.addr = addr
        threading.Thread.__init__(self)
    def run (self):
        self.Autorization()
        while True:
            self.data = self.clientSock.recv(1024)
            for client in server.ConnClient:
                if client == self:
                    continue
                else:
                    mess = self.login + ": " + self.data
                    client.clientSock.send(mess)

    def Close(self):
        self.clientSock.close()
    def Autorization(self):
        #print len(ConnClient)
        #print "Hello user, first you must login\n"
        #self.clientSock.send("Hello user, first you must login\n")
        while True:
            self.login = self.clientSock.recv(16)
            if self.login in server.ClientsLogins:
                #self.clientSock.send("Sorry, this login is already used, try again\n")
                print("Sorry, this login is already used, try again\n")
                continue
            elif len(server.ClientsLogins) >= server.max_client:
                print "Sorry, server is overload. Try later\n"
                #self.clientSock.send("Sorry, server is overload. Try later\n")
                continue

            
            #print "Welcome to our chat "+self.login+"\n"
            self.clientSock.send(self.login)
            server.ClientsLogins.append(self.login)
            self.clientSock.send("Welcome to our chat "+self.login+"\n")
            break