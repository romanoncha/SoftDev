'''
Client classes
@author: ivan
'''
import socket
from threading import Thread
from Command import *

class ClientInfo:
    def __init__(self):
        self.userName=""
        self.passWord=""
    def Set(self,name,pas):
        self.userName=name
        self.passWord=pas

class Client ():
    def __init__(self):
        'Client init'
        self.Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.data = ""
        self.messageText = ""
        self.ClientInf = ClientInfo()


    def Connect(self,ip,port):
        'connect to ip and port, where ip string and port integer'
        self.Socket.connect((ip,port))
        print "Connect"

    def Disconnect(self):
        'connect to ip and port'
        self.Socket.close()
        print "Disconnect"

    def Send(self,message):
        'send message to server'
        #if self.state==Types.canSendMessage:
        self.Socket.send(message)
        print "Send"


    def SendLoggin(self):
        'send message to server'
        self.Socket.send(self.ClientInf.userName)


    def Autorization(self):

        self.SendLoggin()
        self.servCommand = self.Socket.recv(1024)
        self.servCommand.decode()
        return self.servCommand

    def StartReceive(self):
        print "StartReceive "
        while True:
            self.data=self.Socket.recv(1024)
            print 'DATA '+self.data
                

    def GetServerCommand(self):
        self.servCommand = self.Socket.recv(1024)
        self.servCommand.decode()
        print self.servCommand+'\n'
        return self.servCommand

    def GetReceivedData(self):
        self.data = self.Socket.recv(1024)
        self.data.decode()
        return self.data