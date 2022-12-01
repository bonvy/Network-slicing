import os

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from webob.static import DirectoryApp

from ryu.app.wsgi import ControllerBase, WSGIApplication, route
from ryu.base import app_manager


PATH = os.path.dirname(__file__)

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


# Serving static files
class GUIServerApp(app_manager.RyuApp):
    _CONTEXTS = {
        'wsgi': WSGIApplication,
    }

    def __init__(self, *args, **kwargs):
        super(GUIServerApp, self).__init__(*args, **kwargs)

        wsgi = kwargs['wsgi']
        wsgi.register(GUIServerController)


class GUIServerController(ControllerBase):
    def __init__(self, req, link, data, **config):
        super(GUIServerController, self).__init__(req, link, data, **config)
        createNet()
        path = "%s/html/" % PATH
        self.static_app = DirectoryApp(path)

    @route('topology', '/{filename:[^/]*}')
    def static_handler(self, req, **kwargs):
        if kwargs['filename']:
            req.path_info = kwargs['filename']
        return self.static_app(req)


app_manager.require_app('ryu.app.rest_topology')
app_manager.require_app('ryu.app.ws_topology')
app_manager.require_app('ryu.app.ofctl_rest')
