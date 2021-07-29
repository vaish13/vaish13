import random

from tkinter import *
import pyperclip
from functools import partial




top = Tk()
top.configure(background = '#99ddff')
top.title("Password Generator")
top.geometry("900x700")


img=PhotoImage(file='password.png')
imgLabel=Label(image=img)
btn=Button(top,image=img,borderwidth=0).place(x=5,y=5)



def generate(upr, lwr, nbr, sbl):    
    upper=""
    lower=""
    numbers=""
    symbols=""
    
    if upr.get()==1:
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if lwr.get()==1:
        lower = "abcdefghijklmnopqrstuvwxyz"

    if nbr.get()==1:
        numbers = "01234567890123456789"


    if sbl.get()==1:
        symbols = "!@#$%&*()./_"  

    bigString = lower + upper + numbers + symbols
    
    length = 16
    password="".join(random.sample(bigString, length))
    pass_str.set(password)

upr = IntVar()
lwr = IntVar()
nbr = IntVar()
sbl = IntVar()

def copytoclipboard():
    random_password=pass_str.get()
    pyperclip.copy(random_password)

    
pass_str=StringVar()


c1 = Checkbutton(top, text="Upper", variable=upr, onvalue=1, offvalue=0,bg="#b3b3cc",fg="#330d00",font="arial 8 bold").place(x=350, y=50)

c2 = Checkbutton(top, text="Lower", variable=lwr, onvalue=1, offvalue=0,bg="#b3b3cc",fg="#330d00",font="arial 8 bold").place(x=350, y=150)

c3 = Checkbutton(top, text="Numbers", variable=nbr, onvalue=1, offvalue=0,bg="#b3b3cc",fg="#330d00",font="arial 8 bold").place(x=350, y=250)

c4 = Checkbutton(top, text="Symbols", variable=sbl, onvalue=1, offvalue=0,bg="#b3b3cc",fg="#330d00",font="arial 8 bold").place(x=350, y=350)


generate = partial(generate, upr, lwr, nbr, sbl)
b = Button(top, text="Generate Password",bg="#660000",fg="white",font="arial 8 bold",command=generate).place(x=350, y=400)
entry=Entry(top,textvariable=pass_str,font="arial 8 bold").place(x=350,y=450)


b1=Button(top, text="Copy To Clipboard",bg="#660000",fg="white",font="arial 8 bold",command=copytoclipboard).place(x=350,y=500)
entry=Entry(top)


top.mainloop()

