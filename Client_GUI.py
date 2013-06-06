#-*- coding:utf-8 -*-
from Tkinter import *
from client import *
from threading import Thread


class FormAuthorization:
    def __init__(self):
        self.client=Client()
        menu = Menu(root)
        root.config(menu=menu)
        menu.add_command(label="Connect", command=self.connect )
        menu.add_command(label="Login", command=self.login)

        self.w = root.winfo_screenwidth()
        self.h = root.winfo_screenheight()
        self.x = 650
        self.y = 400
        root.geometry("%dx%d+%d+%d" % (self.x, self.y, self.w/2-self.x/2, self.h/2-self.y/2))
        text1=Text(root,height=17,width=60,font='Arial 12',wrap=WORD)
        text1.config(state='disabled')
        text1.pack(side='left')
        listbox1=Listbox(root,height=20,width=20,selectmode=EXTENDED)
        listbox1.pack(side='right')
        self.message=StringVar(root)
        message=Entry(root,textvariable=self.message)
        message.place(x=1, y=370, width = 480)
        def onClick(ev):
            ##################
            self.receiver.Send(message.get())
            self.text1=self.receiver.messageText
            ###################
            text1.insert(END, message.get()+'\n')
            message.delete('0', END)
        sendb = Button(root, text='Send')
        sendb.place(x=482, y=366, width = 64)
        sendb.bind('<Button-1>', onClick) 
        
        ###########################
        self.receiver=Client()
        
    def connect(self):
        son1=Tk()
        self.w = son1.winfo_screenwidth()
        self.h = son1.winfo_screenheight()
        self.x = 225
        self.y = 130
        son1.geometry("%dx%d+%d+%d" % (self.x, self.y, self.w/2-self.x/2, self.h/2-self.y/2))
        self.host = StringVar(son1)
        self.port = IntVar(son1)
        
        Label(son1, text="host:").place(x=25, y=25)
        Label(son1, text="port:").place(x=25, y=50)
        
        self.text1 = Entry(son1, textvariable=self.host)
        self.text1.place(x=100, y=25, width = 100)
        
        self.text2 = Entry(son1, textvariable=self.port)
        self.text2.place(x=100, y=50, width = 100)
        def onClick(ev):
            #self.client.connect(self.host.get(),self.port.get())
            ##############
            self.receiver.Connect("127.0.0.1", 1024)
            Thread(target=self.receiver.StartReceive).start()
            ################
            self.login()
            son1.withdraw()
        btn1 = Button(son1, text='Connect')
        btn1.place(x=25, y=85, width = 175)
        btn1.bind('<Button-1>', onClick) 
        son1.title("SoftDev Chat")
         
    def login(self):
        son2=Tk()
        self.w = son2.winfo_screenwidth()
        self.h = son2.winfo_screenheight()
        self.x = 225
        self.y = 130
        son2.geometry("%dx%d+%d+%d" % (self.x, self.y, self.w/2-self.x/2, self.h/2-self.y/2))
        self.login = StringVar(son2)
        Label(son2, text="login:").place(x=25, y=25)
        self.text1 = Entry(son2, textvariable=self.login)
        self.text1.place(x=100, y=25, width = 100)
        def onClick(ev):
            #self.client.send(self.login.get())
            self.receiver.ClientInf.Set("FIRST USER", "")
            self.receiver.SendLoggin()
            son2.withdraw()
        btn1 = Button(son2, text='Login')
        btn1.place(x=25, y=85, width = 175)

        btn1.bind('<Button-1>', onClick)
        son2.title("SoftDev Chat")


root = Tk()
root.title("SoftDev Chat")         
Form1 = FormAuthorization()

root.mainloop()





