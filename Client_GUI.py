#-*- coding:utf-8 -*-
'''
Created on 25 05 2013

@author: roma
'''
from Tkinter import *

class FormAuthorization:
    def __init__(self):
        self.w = root.winfo_screenwidth()
        self.h = root.winfo_screenheight()
        self.x = 225
        self.y = 130
        
        #place window into center of the screen
        root.geometry("%dx%d+%d+%d" % (self.x, self.y, self.w/2-self.x/2, self.h/2-self.y/2))
        
        self.login = StringVar()
        self.password = StringVar()
        
        Label(root, text="Login:").place(x=25, y=25)
        Label(root, text="Password:").place(x=25, y=50)
        
        self.text1 = Entry(root, textvariable=self.login)
        self.text1.place(x=100, y=25, width = 100)
        
        self.text2 = Entry(root, textvariable=self.password)
        self.text2.place(x=100, y=50, width = 100)
        
        def OnClick(ev):
            '''
            Отправляем логин и пароль на сервер...
            '''
            #таким образом получаем значения текстовых полей
            print self.text1.get()
            print self.text2.get()
        
        btn1 = Button(root, text='Authorization')
        btn1.place(x=25, y=85, width = 175)

        btn1.bind('<Button-1>', OnClick)

        

root = Tk()
root.title("SoftDev Chat")

Form1 = FormAuthorization()

root.mainloop()



