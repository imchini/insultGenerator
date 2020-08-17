import meanMachine
from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Get Insulted!")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
ttk.Button(root, text=meanMachine.insult).grid()
root.mainloop()

