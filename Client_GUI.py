#-*- coding:utf-8 -*-
from Tkinter import *
from client import *
from threading import Thread
import tkMessageBox
import Command
import sys
from re import compile, findall

class FormAuthorization:
    def __init__(self):
        self.client=Client()
        menu = Menu(root)
        root.config(menu=menu)
        menu.add_command(label="Connect", command=self.connect )

        self.w = root.winfo_screenwidth()
        self.h = root.winfo_screenheight()
        self.x = 615
        self.y = 385
        root.geometry("%dx%d+%d+%d" % (self.x, self.y, self.w/2-self.x/2, self.h/2-self.y/2))

        self.richTextBox1 = Text(root, height=20, width=60, font='Arial 10',wrap=WORD)
        self.richTextBox1.config(state='normal')
        self.richTextBox1.place(x=15, y=15, width=450)

        self.listbox1 = Listbox(root, height=20, width=20, selectmode=EXTENDED)
        self.listbox1.place(x=475, y=15)

        self.message=StringVar(root)
        textOfMessage=Entry(root,textvariable=self.message)
        textOfMessage.place(x=15, y=350, width = 450)

        def onClick(ev):
            #send message
            if '' == self.message.get():
                tkMessageBox.showwarning("Empty string!", "Enter the text of message, please!")
                return
            self.client.Send(self.message.get())
            self.richTextBox1.insert(END, self.message.get()+'\n')
            #self.richTextBox1.insert(END, self.client.GetReceivedData()+'\n')
            textOfMessage.delete('0', END)

        sendb = Button(root, text='Send')
        sendb.place(x=475, y=347, width = 125, height = 25)
        sendb.bind('<Button-1>', onClick)

        ###########################

    def connect(self):
        son1=Tk()
        self.w = son1.winfo_screenwidth()
        self.h = son1.winfo_screenheight()
        self.x = 175
        self.y = 130
        son1.geometry("%dx%d+%d+%d" % (self.x, self.y, self.w/2-self.x/2, self.h/2-self.y/2))

        self.host = StringVar(son1)
        self.port = IntVar(son1)
        self.host.set("127.0.0.1")
        self.port.set(1024)

        Label(son1, text="Host:").place(x=25, y=25)
        Label(son1, text="Port:").place(x=25, y=50)

        self.text1 = Entry(son1, textvariable=self.host)
        self.text1.place(x=75, y=25, width = 75)

        self.text2 = Entry(son1, textvariable=self.port)
        self.text2.place(x=75, y=50, width = 75)

        def onClick(ev):
            #make connection
            try:
                self.client.Connect(self.host.get(), self.port.get())
                #Thread(target=self.client.StartReceive).start()
            except IOError,e:
                tkMessageBox.showerror("Connection Error!",
                                       "Failed to establish connection to the server ("+self.host.get()+":"+str(self.port.get())+")!\nTry again, please!")
                son1.withdraw()
                return
            self.loginDlg()
            son1.withdraw()

        btn1 = Button(son1, text='Connect')
        btn1.place(x=25, y=85, width = 125)
        btn1.bind('<Button-1>', onClick)
        son1.title("SoftDev Connect")

    def getListOfClients(self):
        self.command = self.client.GetServerCommand()

        reg = compile("[\w@]+")
        logs = reg.findall(self.command)

        for log in logs:
            if (log == Command.transferListStart):
                continue
            elif (log == Command.transferListFinish):
                break
            else:
                if (log == self.login.get()):
                    self.listbox1.insert(END, log+" (You)")
                    continue
            self.listbox1.insert(END, log)


    def loginDlg(self):
        son2=Tk()
        self.w = son2.winfo_screenwidth()
        self.h = son2.winfo_screenheight()
        self.x = 175
        self.y = 105
        son2.geometry("%dx%d+%d+%d" % (self.x, self.y, self.w/2-self.x/2, self.h/2-self.y/2))

        self.login = StringVar(son2)
        Label(son2, text="Login:").place(x=25, y=25)
        self.text1 = Entry(son2, textvariable=self.login)
        self.text1.place(x=75, y=25, width = 75)

        def onClick(ev):
            self.client.ClientInf.Set(self.login.get(), "")

            self.command = self.client.Autorization()

            if self.command == Command.loginExist:
                tkMessageBox.showerror("Wrong login","This login is already exist. Try again")
                son2.withdraw()
                self.loginDlg()
            if self.command == Command.serverOverload:
                tkMessageBox.showerror("Server is overload","Server is overload. Try later")
                sys.exit(0)
            if self.command == Command.welcome:
                tkMessageBox.showinfo("Welcome","Welcome to our chat " + self.client.ClientInf.userName)
                self.getListOfClients()
                son2.withdraw()


        btn1 = Button(son2, text='Login')
        btn1.place(x=25, y=60, width = 125)

        btn1.bind('<Button-1>', onClick)
        son2.title("SoftDev Login")


root = Tk()
root.title("SoftDev Chat")
Form1 = FormAuthorization()

root.mainloop()





