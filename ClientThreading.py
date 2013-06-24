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
<<<<<<< HEAD
        self.messageIn = self.clientSock.recv(1024)
        if self.messageIn.decode() == Command.readyToResive:
            self.SendUserList()
        self.SendMessageList()
=======
        #time.sleep(5)
        self.messageIn = self.clientSock.recv(1024)
        if self.messageIn.decode() == "ready":
            print self.messageIn
            self.SendUserList()
>>>>>>> a6c4615ce1697c7808ab84d4be6ca01fe0c52a5e
        self.Chat()


    def Close(self):
        self.clientSock.close()

    def SendMessageForAll(self, message):

        for client in server.ConnClient:
            if client == self:
                continue
            else:
                client.clientSock.send(message)

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
            message = "NEW USER IN CHAT: " + self.login
            self.SendMessageForAll(message)
            self.AddToMessageList(message)
            break

    def Chat(self):
        while True:
            self.messageIn = self.clientSock.recv(1024)
            self.messageIn.decode()
<<<<<<< HEAD
            self.messageIn = self.FormMessage(self.messageIn)
            print "In Chat"
            self.AddToMessageList(self.messageIn)
            self.SendMessageForAll(self.messageIn)
=======
            print self.messageIn
            now = time.localtime(time.time())
            year, month, day, hour, minute, second, weekday, yearday, daylight = now
            mess="[" +"%02d:%02d:%02d" % (hour, minute, second)+"] "+self.messageIn
             
            for client in server.ConnClient:
                if client == self:
                    continue
                else:
                    client.clientSock.send(mess)
>>>>>>> a6c4615ce1697c7808ab84d4be6ca01fe0c52a5e

    def GetSocket(self):

        return self.clientSock

    def SendUserList(self):
<<<<<<< HEAD

        for client in server.ConnClient:
            for login in server.ClientsLogins:
                client.clientSock.send('@'+login+'\n')

    def FormMessage(self, message):

        now = time.localtime(time.time())
        year, month, day, hour, minute, second, weekday, yearday, daylight = now
        message = "[" +"%02d:%02d:%02d" % (hour, minute, second)+"] "+ message
        return message

    def AddToMessageList(self, message):

        length = len(server.MessageList)
        if length >= server.max_message:
            server.MessageList.delete(0)
        server.MessageList.append(message)
        print "MessageList"
        print server.MessageList

    def SendMessageList(self):

        time.sleep(0.1)
        for message in server.MessageList:
            print "SendMessageList" + message
            self.clientSock.send(message + "\n")



=======
        print "SendUserList"
        for client in server.ConnClient:
            #client.clientSock.send(Command.transferListStart+'\n',10)
            for login in server.ClientsLogins:
                #size = len(login) + 1
                #client.clientSock.send(str(size))
                client.clientSock.send('@'+login+'\n')
            #client.clientSock.send(Command.transferListFinish+'\n',10)
>>>>>>> a6c4615ce1697c7808ab84d4be6ca01fe0c52a5e
