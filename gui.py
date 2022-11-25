from tkinter import *
from tkinter import ttk
from mininet.net import Mininet

def addSW():
    i=7
    sconfig = {"dpid": "%016x" % (i + 1)}
    net.addSwitch("s%d" % (i + 1), **sconfig)
net=Mininet()
root = Tk() #finestra
root.title("Test")
root.geometry("250x250")#definizione grandezza finestra

mainframe = ttk.Frame(root, padding="3 3 12 12") #simile ad un div
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe,text="ciao").grid(column=2,row=1, sticky=W)
ttk.Button(mainframe,text="aggiungi host",command=addSW()).grid(column=2, row= 2,sticky=W)
root.mainloop()

