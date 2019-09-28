import tkinter
from tkinter import *

top=tkinter.Tk()
def hello():
    text=Text(top)
    text.insert(INSERT,"Hello this is my first Aplication ")
    text.insert(END,"Thanks fo waching my tutorial, if you have any proble just reach out to my")
    text.pack()

B=tkinter.Button(top,text="Mi primer boton GUI",command=hello)
B.pack()
top.mainloop()