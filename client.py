'''
Created on 25 05 2013

@author: roma
'''
from Tkinter import *

def GetLogin(ev):
    print text1.get()
    print text2.get()

root = Tk()
root.title("SoftDev Team Chat")

w = root.winfo_screenwidth()
h = root.winfo_screenheight(
x = 225
y = 150

#place window into center of the screen
root.geometry("%dx%d+%d+%d" % (x, y, w/2-x/2, h/2-y/2))


Label(root, text="Hi bratyuni!").place(x=25, y=15)
Label(root, text="Login:").place(x=25, y=50)
Label(root, text="Password:").place(x=25, y=75)

login = StringVar()
password = StringVar()

text1 = Entry(root, textvariable=login)
text1.place(x=100, y=50, width = 100)

text2 = Entry(root, textvariable=password)
text2.place(x=100, y=75, width = 100)

btn1 = Button(root, text='Show login')#.place(x=25, y=100)
btn1.place(x=25, y=105)

btn1.bind('<Button-1>', GetLogin)


root.mainloop()

#*********************************************************

