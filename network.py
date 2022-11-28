#!/usr/bin/python3
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from test import test


def createNet():
    net = Mininet( 
        switch=OVSKernelSwitch,
        build=False,
        autoSetMacs=True,
        autoStaticArp=True,
        link=TCLink,)

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

if __name__ == '__main__':
    setLogLevel( 'info' )
    createNet()
    
 



