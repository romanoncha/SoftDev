#!/usr/bin/env python
#-*- coding:utf-8 -*-
import threading
import server
import Command

class ClientThreading(threading.Thread):
    def __init__(self, clientSock, addr):

        self.clientSock = clientSock
        self.addr = addr
        threading.Thread.__init__(self)

    def run (self):

        self.Autorization()
        self.Chat()


    def Close(self):

        self.clientSock.close()

    def Autorization(self):

        while True:
            self.messageIn = self.clientSock.recv(1024)
            self.messageIn.decode()
            self.login = self.messageIn

            if self.login in server.ClientsLogins:
                self.clientSock.send(Command.loginExist)
                continue
            elif len(server.ClientsLogins) >= server.max_client:
                self.clientSock.send(Command.serverOverload)
                continue
            self.clientSock.send(Command.welcome)
            server.ClientsLogins.append(self.login)

            self.clientSock.send(Command.transferListStart+'\n')
            for login in server.ClientsLogins:
                self.clientSock.send(login+'\n')

            self.clientSock.send(Command.transferListFinish+'\n')

            break

    def Chat(self):

        while True:
            self.messageIn = self.clientSock.recv(1024)
            self.messageIn.decode()
            for client in server.ConnClient:
                if client == self:
                    continue
                else:
                    client.clientSock.send(self.messageIn)

    def GetSocket(self):
        return self.clientSock