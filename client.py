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

class Types:
    connecting=123456;
    canSendMessage=1234567;
    disconnected=12345678;

class Client ():
    def __init__(self):
        'Client init'
        self.Socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.data=""
        self.enableRecive=False
        self.sendMessage=True
        self.messageText=""
        self.state=Types()
        self.ClientInf=ClientInfo()


    def Connect(self,ip,port):
        'connect to ip and port, where ip string and port integer'
        self.state=Types.connecting
        self.Socket.connect((ip,port))
        print "Connect"

    def ConnectWithName(self,name,ip,port):
        'connect to ip and port, where ip string and port integer'
        self.state=Types.connecting
        self.Socket.connect((ip,port))
        print "Connect"

    def Disconnect(self):
        'connect to ip and port'
        self.state=Types.disconnected
        self.Socket.close()
        print "Disconnect"

    def Send(self,message):
        'send message to server'
        #if self.state==Types.canSendMessage:
        self.Socket.send(message)
        print "Send"
    def SendLogginWithRepeating(self):
        'send message to server'
        while True:
            #print (self.ClientInf.userName)
            self.Socket.send(self.ClientInf.userName)
            if self.state==Types.canSendMessage:
                break

    def SendLoggin(self):
        'send message to server'
        self.Socket.send(self.ClientInf.userName)


    def Autorization(self):

        self.SendLoggin()
        self.servCommand = self.Socket.recv(1024)
        self.servCommand.decode()
        print self.servCommand
        return self.servCommand

    def StartReceive(self):
        print "StartReceive "
        while True:
            if self.state==Types.connecting:
                print "Types.connecting"
                #Thread(target=self.SendLogginWithRepeating).start()
                self.data=self.Socket.recv(1024)
                print 'DATA '+self.data
                if not self.data:
                    self.state=Types.connecting
                else:
                    self.state=Types.canSendMessage
            if self.state==Types.canSendMessage:
                print "Types.canSendMessage"
                self.data=self.Socket.recv(1024)
                self.messageText+=self.data
                if self.data:
                    print "Server Message: "+self.messageText
            if self.state==Types.disconnected:
                break

    def GetServerCommand(self):
        self.servCommand = self.Socket.recv(1024)
        self.servCommand.decode()
        print self.servCommand+'\n'
        return self.servCommand

    def GetReceivedData(self):
        self.data = self.Socket.recv(1024)
        self.data.decode()
        return self.data