from tkinter import Button, IntVar,Tk
from tkinter import Entry
from tkinter.constants import RIGHT, W
root=Tk()
root.geometry("385x235")
root.resizable(0,0)
root.title("calculator")
root.configure(background="black")
a=IntVar
def cal(c):
     a.set(a.get()+c)
def equ():
     ex=a.get()
     a.set(eval(ex))
def clr():
     a.set(" ")
e1=Entry(root,font=("arial",15),justify=RIGHT,textvariable=a)
e1.place(x=5,y=4,width=373,height=50)
#
b7=Button(text="7",font=("arial",15),bg="gray",fg="white",activebackground="green",activeforeground="red")
b7.place(x=5,y=58,width=90,height=40)
b7.configure(command=lambda:cal("7"))
#
b8=Button(text="8",font=("arial",15),bg="gray",fg="white",activebackground="green",activeforeground="red")
b8.place(x=100,y=58,width=90,height=40)
b8.configure(command=lambda:cal("8"))
#
b9=Button(text="9",font=("arial",15),bg="gray",fg="white",activebackground="green",activeforeground="red")
b9.place(x=195,y=58,width=90,height=40)
b9.configure(command=lambda:cal("9"))
#
bp=Button(text="+",font=("arial",15),bg="gray",fg="white",activebackground="green",activeforeground="red")
bp.place(x=290,y=58,width=90,height=40)
bp.configure(command=lambda:cal("+"))
#
b4=Button(text="4",font=("arial",15),bg="gray",fg="white",activebackground="green",activeforeground="red")
b4.place(x=5,y=102,width=90,height=40)
b4.configure(command=lambda:cal("4"))
#
b5=Button(text="5",font=("arial",15),bg="gray",fg="white",activebackground="green",activeforeground="red")
b5.place(x=100,y=102,width=90,height=40)
b5.configure(command=lambda:cal("5"))
#
b6=Button(text="6",font=("arial",15),bg="gray",fg="white",activebackground="green",activeforeground="red")
b6.place(x=195,y=102,width=90,height=40)
b6.configure(command=lambda:cal("6"))
#
bs=Button(text="-",font=("arial",15),bg="gray",fg="white",activebackground="green",activeforeground="red")
bs.place(x=290,y=102,width=90,height=40)
bs.configure(command=lambda:cal("-"))
#
b1=Button(text="1",font=("arial",15),bg="gray",fg="white",activebackground="green",activeforeground="red")
b1.place(x=5,y=145,width=90,height=40)
b1.configure(command=lambda:cal("1"))
#
b2=Button(text="2",font=("arial",15),bg="gray",fg="white",activebackground="green",activeforeground="red")
b2.place(x=100,y=145,width=90,height=40)
b2.configure(command=lambda:cal("2"))
#
b3=Button(text="3",font=("arial",15),bg="gray",fg="white",activebackground="green",activeforeground="red")
b3.place(x=195,y=145,width=90,height=40)
b3.configure(command=lambda:cal("3"))
#
bi=Button(text="x",font=("arial",15),bg="gray",fg="white",activebackground="green",activeforeground="red")
bi.place(x=290,y=145,width=90,height=40)
bi.configure(command=lambda:cal("x"))
#
bc=Button(text="C",font=("arial",15),bg="gray",fg="white",activebackground="green",activeforeground="red")
bc.place(x=5,y=190,width=90,height=40)
bc.configure(command=clr)
#
b0=Button(text="0",font=("arial",15),bg="gray",fg="white",activebackground="green",activeforeground="red")
b0.place(x=100,y=190,width=90,height=40)
b0.configure(command=lambda:cal("0"))
#
be=Button(text="=",font=("arial",15),bg="gray",fg="white",activebackground="green",activeforeground="red")
be.place(x=195,y=190,width=90,height=40)
be.configure(compound=equ)
#
bd=Button(text="÷",font=("arial",15),bg="gray",fg="white",activebackground="green",activeforeground="red")
bd.place(x=290,y=190,width=90,height=40)