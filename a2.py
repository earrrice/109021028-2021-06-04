from tkinter import *
import random

n=int(0)

def slt():
    global n
    n=random.randrange(10)
    lab1.config(text=n) 


window=Tk()
window.title("windo1")
window.geometry("555x555+100+100")
window.config(bg="#6677ff")

lab1=Label(window,text=n,width=12,height=8,bg="#555500")
lab1.pack()#打包

btn1=Button(window,text="generate",command=slt)
btn1.pack()

btnexit=Button(window,text="exit",command=window.destroy)
btnexit.pack()

window.mainloop()