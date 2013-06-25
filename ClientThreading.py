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
        self.stop_event = threading.Event()

    def run (self):

        self.Autorization()
        self.messageIn = self.clientSock.recv(1024)
        if self.messageIn.decode() == Command.readyToResive:
            self.SendUserList()
        self.SendMessageList()
        self.Chat()
        self.SendUserList()
        self.Close()


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

        while not self.stop_event.isSet():
            self.messageIn = self.clientSock.recv(1024)
            self.messageIn.decode()
            if self.messageIn in server.ClientsLogins:
                self.log=self.messageIn
                self.index = server.ClientsLogins.index(self.messageIn)
                server.ConnClient[self.index].GetSocket().send(Command.clientDestroy)
                server.ConnClient[self.index].GetSocket().send(Command.readyToStop)
                self.messageIn = self.clientSock.recv(1024)
                if self.messageIn == Command.readyToStop:
                    server.ConnClient[self.index].Close()
                    del server.ConnClient[self.index]
                    server.ClientsLogins.remove(self.log)
                    self.messageIn = self.FormMessage("USER "+self.log+" DISCONNECT")
                    self.AddToMessageList(self.messageIn)
                    self.SendMessageForAll(self.messageIn)
                    server.count-=1
                    self.stop_event.set()
            else:
                self.messageIn = self.FormMessage(self.messageIn)
                print "In Chat"
                self.AddToMessageList(self.messageIn)
                self.SendMessageForAll(self.messageIn)

    def GetSocket(self):

        return self.clientSock

    def SendUserList(self):

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
            buf=server.MessageList[0]
            server.MessageList.remove(buf)
        server.MessageList.append(message)
        print "MessageList"

    def SendMessageList(self):

        time.sleep(0.1)
        for message in server.MessageList:
            self.clientSock.send(message + "\n")



