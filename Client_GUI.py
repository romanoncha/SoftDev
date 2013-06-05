#-*- coding:utf-8 -*-
from Tkinter import *
from socket import *
from client import *
class FormAuthorization:
    def __init__(self):
        self.client=Client()
        self.w = root.winfo_screenwidth()
        self.h = root.winfo_screenheight()
        self.x = 225
        self.y = 130
        root.geometry("%dx%d+%d+%d" % (self.x, self.y, self.w/2-self.x/2, self.h/2-self.y/2))
    
        self.host = StringVar()
        self.port = IntVar()
        
        Label(root, text="host:").place(x=25, y=25)
        Label(root, text="port:").place(x=25, y=50)
        
        self.text1 = Entry(root, textvariable=self.host)
        self.text1.place(x=100, y=25, width = 100)
        
        self.text2 = Entry(root, textvariable=self.port)
        self.text2.place(x=100, y=50, width = 100)
        
        def OnClick(ev):
            self.client.connect(self.host.get(),self.port.get())
            self.login()
        btn1 = Button(root, text='Connect')
        btn1.place(x=25, y=85, width = 175)

        btn1.bind('<Button-1>', OnClick)
    def login(self):
        root1 = Tk()
        self.w = root1.winfo_screenwidth()
        self.h = root1.winfo_screenheight()
        self.x = 225
        self.y = 130
        root1.geometry("%dx%d+%d+%d" % (self.x, self.y, self.w/2-self.x/2, self.h/2-self.y/2))
        self.login = StringVar()
        Label(root1, text="login:").place(x=25, y=25)
        self.text1 = Entry(root1, textvariable=self.login)
        self.text1.place(x=100, y=25, width = 100)
        def OnClick(ev):
            self.client.login(self.login.get())
            
        btn1 = Button(root1, text='Login')
        btn1.place(x=25, y=85, width = 175)

        btn1.bind('<Button-1>', OnClick)
        root1.title("SoftDev Chat")


root = Tk()
root.title("SoftDev Chat")         
Form1 = FormAuthorization()

root.mainloop()



