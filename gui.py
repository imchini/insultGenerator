import meanMachine
from tkinter import *
from tkinter import ttk
import random

insult=("you "+meanMachine.list1[random.randint(0,18)]+", "+meanMachine.list2[random.randint(0,18)]+", "+meanMachine.list3[random.randint(0,26)]+"!")

def showText():
  insult

root=Tk()
root.title("Get Insulted!")
root.geometry("400x400")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
ttk.Button(root,text="Generate Insult",
                command=showText).grid()
ttk.Button(root,
                text="Quit",
                command=root.destroy).grid()

"""ttk.Button(root, text=insult).grid()"""

root.mainloop()