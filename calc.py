#!/usr/bin/env python3
from tkinter import *

win = Tk()
win.geometry("320x325")
win.resizable(0,0)
win.title("Calc with converters")

def bt_click(item):
    global flag
    global expression
    if item in range(0,10) or str(item) in "+-*/":
        expression =expression + str(item)
        input_text.set(expression)
        flag= False
    else:
        expression= "error value"
        input_text.set(expression)
        expression=""
        flag= False
def bt_clear():
    global expression
    expression = ""
    input_text.set(expression)
    flag= False

def bt_equal():
    try:
        global expression 
        global flag  # flaga odpowiadająca za pózniejsze warunki ( czy było kliknięte)
        flag = True
        result = str(eval(expression))
        input_text.set(result)
    except:
        input_text.set("error expression")
        expression = ""
        flag= False
def change(option):
    global expression
    global flag # flaga od kliknięcia równania
    try:
        if option == 2: # opcja binarna
            res = [i for i in expression if i in "/*+-"]  # wyszukanie czy sa znaki arytmetyczne i zapis do listy (W ODPOWIEDNEJ KOLEJNOSCI)
            if res and not flag:    # warunek czy były operacje oraz czy kyło kliknięte znak równości
                xd='' # string do przechowania binarnego przedstawienia liczb z znakami
                nexpress=expression.replace('+',' ').replace('/',' ').replace('-',' ').replace('*',' ').split(' ') # 1. krok usuwanie znaków arytmetycznych poprzez zastąpienie spacją i zrobienie listy
                nbin=[str(bin(int(nexpress[i]))) for i in range(len(nexpress))] # 2. krok rzutowanie binarnej konwersji na string aby ładnie pakować do listy
                word=[nbin[i]+res[i] for i in range(len(res))] # 3. łączenie listy binarnych stringów i znaków arytmetycznej w kolejności odpowiadającej realnym operacjim
                xd=[word[i] for i in range(len(word))] # 4. łączenie elementów w jedną listę
                xd.append(nbin[-1]) # 5. dodanie ostatniej liczby do listy
                input_text.set(xd) # wypisanie listy w kalkulatorze
            else:
                input_text.set(bin(int(eval((expression))))) # w razie kliknięcia równania -> wypisuje binarną wersje wyniku 
        if option ==1:
            res = [i for i in expression if i in "/*+-"]
            if res and not flag:
                xd=''
                nexpress=expression.replace('+',' ').replace('/',' ').replace('-',' ').replace('*',' ').split(' ')
                nbin=[str(float(int(nexpress[i]))) for i in range(len(nexpress))] # tutaj tylko zmiana bin() na float() zasada taka sama
                word=[nbin[i]+res[i] for i in range(len(res))]
                xd=[word[i] for i in range(len(word))]
                xd.append(nbin[-1])
                input_text.set(xd)
            else:
                input_text.set(int(eval(expression)))
    except:
        input_text.set("None type to convert")
expression = ""
flag= False
input_text = StringVar()
input_frame = Frame(win, highlightbackground="black",highlightcolor="black",highlightthickness=2)
input_frame.pack(side=TOP)
input_field=Entry(input_frame,font=('arial',18,'bold'),textvariable=input_text,width=50,bg='#eee',bd=0,justify=LEFT)
input_field.grid(row=0,column=0,columnspan=4)
input_field.pack()


btns_frame = Frame(win)
btns_frame.pack(side=TOP)

binary = Radiobutton(btns_frame,text = "DEC",value="1",command=lambda:change(1)).grid(row=0,column=0,padx=1,pady=1,columnspan=2)
decimal =Radiobutton(btns_frame,text = "BIN",value="2",command=lambda:change(2)).grid(row=0,column=2,padx=1,pady=1,columnspan=2)

one = Button(btns_frame,text="1",fg="black",width=6,height=3,bd=0,bg='#fff',cursor="hand2",command=lambda:bt_click(1)).grid(row=1,column=0,padx=1,pady=1)
two = Button(btns_frame,text="2",fg="black",width=6,height=3,bd=0,bg='#fff',cursor="hand2",command=lambda:bt_click(2)).grid(row=1,column=1,padx=1,pady=1)
tree= Button(btns_frame,text="3",fg="black",width=6,height=3,bd=0,bg='#fff',cursor="hand2",command=lambda:bt_click(3)).grid(row=1,column=2,padx=1,pady=1)
add = Button(btns_frame,text="+",fg="black",width=6,height=3,bd=0,bg='#fff',cursor="hand2",command=lambda:bt_click("+")).grid(row=1,column=3,padx=1,pady=1)

four = Button(btns_frame,text="4",fg="black",width=6,height=3,bd=0,bg='#fff',cursor="hand2",command=lambda:bt_click(4)).grid(row=2,column=0,padx=1,pady=1)
five = Button(btns_frame,text="5",fg="black",width=6,height=3,bd=0,bg='#fff',cursor="hand2",command=lambda:bt_click(5)).grid(row=2,column=1,padx=1,pady=1)
six = Button(btns_frame,text="6",fg="black",width=6,height=3,bd=0,bg='#fff',cursor="hand2",command=lambda:bt_click(6)).grid(row=2,column=2,padx=1,pady=1)
munis= Button(btns_frame,text="-",fg="black",width=6,height=3,bd=0,bg='#fff',cursor="hand2",command=lambda:bt_click("-")).grid(row=2,column=3,padx=1,pady=1)

seven = Button(btns_frame,text="7",fg="black",width=6,height=3,bd=0,bg='#fff',cursor="hand2",command=lambda:bt_click(7)).grid(row=3,column=0,padx=1,pady=1)
eight = Button(btns_frame,text="8",fg="black",width=6,height=3,bd=0,bg='#fff',cursor="hand2",command=lambda:bt_click(8)).grid(row=3,column=1,padx=1,pady=1)
nine = Button(btns_frame,text="9",fg="black",width=6,height=3,bd=0,bg='#fff',cursor="hand2",command=lambda:bt_click(9)).grid(row=3,column=2,padx=1,pady=1)
mul = Button(btns_frame,text="*",fg="black",width=6,height=3,bd=0,bg='#fff',cursor="hand2",command=lambda:bt_click("*")).grid(row=3,column=3,padx=1,pady=1)

zero = Button(btns_frame,text="0",fg="black",width=6,height=3,bd=0,bg='#fff',cursor="hand2",command=lambda:bt_click(0)).grid(row=4,column=0,padx=1,pady=1)
clear = Button(btns_frame,text="C",fg="black",width=6,height=3,bd=0,bg='#bbb',cursor="hand2",command=lambda:bt_clear()).grid(row=4,column=2,padx=1,pady=1)
eq = Button(btns_frame,text="=",fg="black",width=6,height=3,bd=0,bg='#fff',cursor="hand2",command=lambda:bt_equal()).grid(row=4,column=1,padx=1,pady=1)
div99 = Button(btns_frame,text="/",fg="black",width=6,height=3,bd=0,bg='#fff',cursor="hand2",command=lambda:bt_click("/")).grid(row=4,column=3,padx=1,pady=1)

win.mainloop()