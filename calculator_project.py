from tkinter import *
from tkinter.ttk import *
window=Tk()

window.title("Calculator")
window.minsize(160,150)
window.maxsize(160,150)
e=Entry(window,width=26)
e.place(x=0,y=0)

ops=['+','-','*','/','.']

e.insert(END, 0)

def insert_number(number):
    x=e.get()
    if len(x)==1 and x=='0':  
        e.delete(0, END)  
    e.insert(END, number)

one=Button(window,text="1",width=5,command=lambda: insert_number(1))
one.place(x=0,y=25)

two=Button(window,text="2",width=5,command=lambda: insert_number(2))
two.place(x=40,y=25)

three=Button(window,text="3",width=5,command=lambda: insert_number(3))
three.place(x=80,y=25)

four=Button(window,text="4",width=5,command=lambda: insert_number(4))
four.place(x=0,y=50)

five=Button(window,text="5",width=5,command=lambda: insert_number(5))
five.place(x=40,y=50)

six=Button(window,text="6",width=5,command=lambda: insert_number(6))
six.place(x=80,y=50)

seven=Button(window,text="7",width=5,command=lambda: insert_number(7))
seven.place(x=0,y=75)

eight=Button(window,text="8",width=5,command=lambda: insert_number(8))
eight.place(x=40,y=75)

nine=Button(window,text="9",width=5,command=lambda: insert_number(9))
nine.place(x=80,y=75)

zero=Button(window,text="0",width=8,command=lambda: insert_number(0))
zero.place(x=0,y=100)

def dot():
    a=e.get()
    if a[-1] not in ops:
        e.insert(END, '.')

decimal=Button(window,text=".",width=8,command=dot)
decimal.place(x=60,y=100)

def clear_last():
    a=e.get()
    e.delete(len(a)-1)
clear=Button(window,text="<-",width=8,command=clear_last)
clear.place(x=0,y=125)

def clear_all():
    e.delete(0, END)
    e.insert(END,0)
clear_all=Button(window,text="C",width=8,command=clear_all)
clear_all.place(x=60,y=125)

def insert_operator(operator):
    y=e.get()
    if y[-1]  in ops:
        e.delete(len(y)-1)
        
    e.insert(END, operator)
    

add=Button(window,text="+",width=5,command=lambda: insert_operator("+"))
add.place(x=120,y=25)

sub=Button(window,text="-",width=5,command=lambda: insert_operator("-"))
sub.place(x=120,y=50)

mul=Button(window,text="*",width=5,command=lambda: insert_operator("*"))
mul.place(x=120,y=75)

div=Button(window,text="/",width=5,command=lambda: insert_operator("/"))
div.place(x=120,y=100)

def calc():
    try:
        result=eval(e.get())
        e.delete(0, END)
        e.insert(END, result)
    except Exception as error:
        e.delete(0, END)
        e.insert(END, "Error")
equ=Button(window,text="=",width=5,command=calc)
equ.place(x=120,y=125)
    
window.mainloop()