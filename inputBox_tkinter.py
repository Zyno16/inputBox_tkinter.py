from tkinter import *
from tkinter import ttk
from tools import *
form =Tk()
form.geometry("700x500")
tkcenter(form)
def test():
    name=inbox("Enter your name ?")
    print("hello " + name)

ttk.Button(form,text="Text Input Box",command=test ).pack(pady =10)
fontall(form,"None 30")



form.mainloop()
