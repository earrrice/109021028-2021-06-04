from tkinter import *
import random

n=int(0)

def slt():
    l1,l2,l3,l4,l5,l6 = random.sample(range(1, 42), 6)
    lab1.config(text=l1) 
    lab2.config(text=l2)
    lab3.config(text=l3)
    lab4.config(text=l4)
    lab5.config(text=l5)
    lab6.config(text=l6)


window=Tk()
window.title("windo1")
window.geometry("555x555+100+100")
window.config(bg="#6677ff")

lab1=Label(window,text=n,width=12,height=3,bg="#555500")
lab1.pack()#打包
lab2=Label(window,text=n,width=12,height=3,bg="#555500")
lab2.pack()
lab3=Label(window,text=n,width=12,height=3,bg="#555500")
lab3.pack()
lab4=Label(window,text=n,width=12,height=3,bg="#555500")
lab4.pack()
lab5=Label(window,text=n,width=12,height=3,bg="#555500")
lab5.pack()
lab6=Label(window,text=n,width=12,height=3,bg="#555500")
lab6.pack()

btn1=Button(window,text="generate",command=slt)
btn1.pack()

btnexit=Button(window,text="exit",command=window.destroy)
btnexit.pack()

window.mainloop()