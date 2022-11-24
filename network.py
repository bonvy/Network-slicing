#!/usr/bin/python3
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from tkinter import *
from tkinter import ttk



def createNet(net):


    

    info( '*** Adding controller\n' )
    controller = RemoteController("c1", ip="127.0.0.1", port=6633)
    net.addController(controller)


    host_config = dict(inNamespace=True)
    switch_config = dict(bw=20)

     #create switch nodes
    for i in range(6):
        sconfig = {"dpid": "%016x" % (i + 1)}
        net.addSwitch("s%d" % (i + 1), **sconfig)

     #create host nodes
    for i in range(9):
        net.addHost("h%d" % (i + 1), **host_config)

    #network core links
    net.addLink("s1","s2", **switch_config)
    net.addLink("s1","s3", **switch_config)
    net.addLink("s3","s2", **switch_config)

    #peripheral links
    net.addLink("s1","s4", **switch_config)
    net.addLink("s2","s5", **switch_config)
    net.addLink("s3","s6", **switch_config)

    net.addLink("h1","s4", **host_config)
    net.addLink("h2","s4", **host_config)
    net.addLink("h3","s1", **host_config)

    net.addLink("h4","s5", **host_config)
    net.addLink("h5","s5", **host_config)
    net.addLink("h6","s2", **host_config)

    net.addLink("h7","s6", **host_config)
    net.addLink("h8","s6", **host_config)
    net.addLink("h9","s3", **host_config)

    net.build()

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

def addHost(net):
    host_config = dict(inNamespace=True)
    net.addHost("h10",**host_config)
    print("aggiunto")

if __name__ == '__main__':
    net = Mininet( 
        switch=OVSKernelSwitch,
        build=False,
        autoSetMacs=True,
        autoStaticArp=True,
        link=TCLink,)
    setLogLevel( 'info' )
    createNet(net)
    root = Tk() #finestra
    root.title("Test")
    root.geometry("250x250")#definizione grandezza finestra

    mainframe = ttk.Frame(root, padding="3 3 12 12") #simile ad un div
    mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Label(mainframe,text="ciao").grid(column=2,row=1, sticky=W)
    ttk.Button(mainframe,text="aggiungi host",command=addHost(net)).grid(column=2, row =2,sticky=W)
    root.mainloop()


