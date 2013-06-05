'''
Client classes
@author: ivan
'''
import socket
from threading import Thread

class ClientInfo:
    def __init__(self):
        self.userName=""
        self.passWord=""


class Client:    
    def __init__(self):
        'Client init'
        self.Socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.data=""
        self.messageText=""
       
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
      
    def StartReceive(self): 
        print "StartReceive "
        while True:
            self.data=self.Socket.recv(1024)
            if self.data:
                print "Server Message: "+self.data