#!/usr/bin/env python
#-*- coding:utf-8 -*-
import threading
import server
import Command
import time

class ClientThreading(threading.Thread):
    def __init__(self, clientSock, addr):

        self.clientSock = clientSock
        self.addr = addr
        threading.Thread.__init__(self)

    def run (self):

        self.Autorization()
        #time.sleep(5)
        self.messageIn = self.clientSock.recv(1024)
        if self.messageIn.decode() == "ready":
            print self.messageIn
            self.SendUserList()
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
            break

    def Chat(self):
        while True:
            self.messageIn = self.clientSock.recv(1024)
            self.messageIn.decode()
            print self.messageIn
            now = time.localtime(time.time())
            year, month, day, hour, minute, second, weekday, yearday, daylight = now
            mess="[" +"%02d:%02d:%02d" % (hour, minute, second)+"] "+self.messageIn
             
            for client in server.ConnClient:
                if client == self:
                    continue
                else:
                    client.clientSock.send(mess)

    def GetSocket(self):
        return self.clientSock

    def SendUserList(self):
        print "SendUserList"
        for client in server.ConnClient:
            #client.clientSock.send(Command.transferListStart+'\n',10)
            for login in server.ClientsLogins:
                #size = len(login) + 1
                #client.clientSock.send(str(size))
                client.clientSock.send('@'+login+'\n')
            #client.clientSock.send(Command.transferListFinish+'\n',10)
