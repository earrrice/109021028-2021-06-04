from tkinter import *

def slt():
    lab1.config(text="OAO")

def slt2():
    lab1.config(text="ewe")

window=Tk()
window.title("windo1")
window.geometry("555x555+100+100")
window.config(bg="#6677ff")

lab1=Label(window,text="ewe",width=12,height=3,bg="#555500")
lab1.pack()#打包

btn1=Button(window,text="Text",command=slt)
btn1.pack()
btn2=Button(window,text="Text2",command=slt2)
btn2.pack()

btnexit=Button(window,text="exit",command=window.destroy)
btnexit.pack()

window.mainloop()