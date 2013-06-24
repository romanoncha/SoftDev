'''
Client classes
@author: ivan
'''
import socket
from threading import Thread
from Command import *
from re import compile, findall
import time

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

    def GetReceivedData(self):
        self.data = self.Socket.recv(1024)
        
        reg = compile("[@][\w]+")
        logs = reg.findall(self.data)
        print logs
        if logs==[]:
            return self.data
        else:
            return logs
        
    def FormMessage(self,message):
        now = time.localtime(time.time())
        year, month, day, hour, minute, second, weekday, yearday, daylight = now
        message ="[" +"%02d:%02d:%02d" % (hour, minute, second)+"] " + message
        return message