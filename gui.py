import meanMachine
from tkinter import *
from tkinter import ttk
import random

def genInsult():
  label.configure(text= ("you "+meanMachine.list1[random.randint(0,18)]+", "+meanMachine.list2[random.randint(0,18)]+", "+meanMachine.list3[random.randint(0,26)]+"!"))

def showText():
  print(genInsult())

root=Tk()
root.title("Get Insulted!")
root.geometry("800x400")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
ttk.Button(root,text="Generate Insult",
                command=genInsult).grid()
label = ttk.Label(root)
label.grid(column = 0, row = 0, pady = 2)
ttk.Button(root,
                text="Quit",
                command=root.destroy).grid()

"""ttk.Button(root, text=insult).grid()"""

root.mainloop()