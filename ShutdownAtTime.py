#!/usr/bin/python
#_*_coding:utf-8_*_
import Tkinter
import sys
import os
tk=Tkinter.Tk()
tk.title('Auto Shutdown')
tk.geometry('350x150')


At=Tkinter.Label(tk,text='At:',font=('Arial',14),width=10,height=10)
At.place(x=20,y=-50,anchor='nw')

H=Tkinter.Entry(tk,width=5)
H.place(x=90,y=55,anchor='nw')

h=Tkinter.Label(tk,text='H',font=('Arial',14),width=3,height=10)
h.place(x=120,y=-50,anchor='nw')

M=Tkinter.Entry(tk,width=5)
M.place(x=150,y=55,anchor='nw')

m=Tkinter.Label(tk,text='M',font=('Arial',14),width=3,height=10)
m.place(x=180,y=-50,anchor='nw')

def Set():
    Hour=int(H.get())
    Min=int(M.get())
    if 0<=Hour<=23 and 0<=Min<=59:
        os.popen('at '+H.get()+':'+M.get()+' shutdown -s')
        btn['text']='Remove'
        hint['text']='Success! the system will shutdown at today '+H.get()+':'+M.get()+'.'
    else:
         hint['text']=='Please Input Correct Time !!!'
def Remove():
    os.popen('at /delete /yes')
    btn['text']='Set'
    hint['text']='Success! already removed~'
def SelectFun():
    if btn['text']=='Set':
        Set()
    else:
        Remove()

btn=Tkinter.Button(tk,text='Set',width=7,height=2,command=SelectFun)
btn.place(x=220,y=45,anchor='nw')



hint=Tkinter.Label(tk,text='Please Input Time Of You Want To Shutdown',font=('Arial',11),width=50)
hint.place(x=-30,y=100,anchor='nw')
tk.mainloop()
