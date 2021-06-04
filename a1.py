from tkinter import *

n=int(0)

def slt():
    global n
    n+=1
    lab1.config(text=n) 

def slt2():
    global n
    n-=1
    lab1.config(text=n)

window=Tk()
window.title("windo1")
window.geometry("555x555+100+100")
window.config(bg="#6677ff")

lab1=Label(window,text=n,width=12,height=3,bg="#555500")
lab1.pack()#打包

btn1=Button(window,text="add",command=slt,bg="#00AA00")
btn1.pack()
btn2=Button(window,text="sub",command=slt2)
btn2.pack()

btnexit=Button(window,text="exit",command=window.destroy)
btnexit.pack()

window.mainloop()