from tkinter import *
from math import *
window = Tk()
window.geometry("465x475")
window.resizable(False,False)
window.title("Calculator")
window.configure(bg="#202020")
oblicz = ""

def liczba(x):
    global oblicz
    oblicz = oblicz + str(x)
    rownanie.set(oblicz)

def wyliczenie():
    try:
        global oblicz 
        suma = str(eval(oblicz))
        rownanie.set(suma)
        oblicz =""
    except:
        rownanie.set("error")
        oblicz = ""

def wyczysc():
    global oblicz
    oblicz = ""
    rownanie.set("")

def back():
    global oblicz
    oblicz = oblicz[:-1]
    rownanie.set(oblicz)

def pierw():
    global oblicz
    t = rownanie.get()
    t=int(t)
    rownanie.set(sqrt(t))
    oblicz = ""

def potega():
    global oblicz
    oblicz = oblicz + str("**")
    rownanie.set(oblicz)


rownanie = StringVar()


pokaz = Entry(window,width=16,font=("segoe",40),bg="#202020",fg="#f1f1f1",textvariable=rownanie).grid(row=0,column=1, columnspan=4)

btn0 = Button(window,text="0",font=(20),fg="#f1f1f1",bg="#3b3b3b",command=lambda: liczba(0),height=2,width=8).grid(row=6,column=2)                   #0
btn1 = Button(window,text="1",font=(20),fg="#f1f1f1",bg="#3b3b3b",command=lambda: liczba(1),height=2,width=8).grid(row=5,column=1)                   #1
btn2 = Button(window,text="2",font=(20),fg="#f1f1f1",bg="#3b3b3b",command=lambda: liczba(2),height=2,width=8).grid(row=5,column=2)                   #2
btn3 = Button(window,text="3",font=(20),fg="#f1f1f1",bg="#3b3b3b",command=lambda: liczba(3),height=2,width=8).grid(row=5,column=3)                   #3
btn4 = Button(window,text="4",font=(20),fg="#f1f1f1",bg="#3b3b3b",command=lambda: liczba(4),height=2,width=8).grid(row=4,column=1)                   #4
btn5 = Button(window,text="5",font=(20),fg="#f1f1f1",bg="#3b3b3b",command=lambda: liczba(5),height=2,width=8).grid(row=4,column=2)                   #5
btn6 = Button(window,text="6",font=(20),fg="#f1f1f1",bg="#3b3b3b",command=lambda: liczba(6),height=2,width=8).grid(row=4,column=3)                   #6
btn7 = Button(window,text="7",font=(20),fg="#f1f1f1",bg="#3b3b3b",command=lambda: liczba(7),height=2,width=8).grid(row=3,column=1)                   #7
btn8 = Button(window,text="8",font=(20),fg="#f1f1f1",bg="#3b3b3b",command=lambda: liczba(8),height=2,width=8).grid(row=3,column=2)                   #8
btn9 = Button(window,text="9",font=(20),fg="#f1f1f1",bg="#3b3b3b",command=lambda: liczba(9),height=2,width=8).grid(row=3,column=3)                   #9
btnd = Button(window,text="+",font=(20),fg="#f1f1f1",bg="#323232",command=lambda: liczba("+"),height=5,width=8).grid(row=5,column=4,rowspan=2)       #+
btno = Button(window,text="-",font=(20),fg="#f1f1f1",bg="#323232",command=lambda: liczba("-"),height=2,width=8).grid(row=4,column=4)                 #-
btnm = Button(window,text="*",font=(20),fg="#f1f1f1",bg="#323232",command=lambda: liczba("*"),height=2,width=8).grid(row=3,column=4)                 #*
btndz = Button(window,text="/",font=(20),fg="#f1f1f1",bg="#323232",command=lambda: liczba("/"),height=2,width=8).grid(row=2,column=4)                #/
btneq = Button(window,text="=",font=(20),fg="#f1f1f1",bg="#323232",command=lambda: wyliczenie(),height=2,width=8).grid(row=6,column=3)               #=
btnp = Button(window,text=",",font=(20),fg="#f1f1f1",bg="#323232",command=lambda: liczba("."),height=2,width=8).grid(row=6,column=1)                 #,
btnc = Button(window,text="C",font=(20),fg="#f1f1f1",bg="#323232",command=lambda: wyczysc(),height=2,width=8).grid(row=1,column=3)                   #C
btnback = Button(window,text="⌫",font=(20),fg="#f1f1f1",bg="#323232",command=lambda: back(),height=2,width=8).grid(row=1,column=4)                  #backspace
btnpier = Button(window,text="√",font=(20),fg="#f1f1f1",bg="#323232",command=lambda:pierw() ,height=2,width=8).grid(row=2,column=3)                  #√
btnpot = Button(window,text="**",font=(20),fg="#f1f1f1",bg="#323232",command=lambda:potega() ,height=2,width=8).grid(row=2,column=2)                 #**
btnln = Button(window,text="(",font=(20),fg="#f1f1f1",bg="#323232",command=lambda: liczba("("),height=2,width=8).grid(row=1,column=1)                #(
btnpn = Button(window,text=")",font=(20),fg="#f1f1f1",bg="#323232",command=lambda: liczba(")"),height=2,width=8).grid(row=1,column=2)                #)
btnpi = Button(window,text="π",font=(20),fg="#f1f1f1",bg="#323232",command=lambda: liczba("(3.14)"),height=2,width=8).grid(row=2,column=1)           #π

window.mainloop()