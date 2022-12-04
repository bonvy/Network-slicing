import json

from ryu.app.wsgi import ControllerBase
from ryu.app.wsgi import Response
from ryu.app.wsgi import route
from ryu.app.wsgi import WSGIApplication
from ryu.base import app_manager
from ryu.ofproto import ofproto_v1_3
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.topology import event

class HostAPI(app_manager.RyuApp):
    _CONTEXTS = {
        'wsgi': WSGIApplication
    }

    def __init__(self, *args, **kwargs):
        super(HostAPI, self).__init__(*args, **kwargs)

        wsgi = kwargs['wsgi']
        wsgi.register(HostController, {'host_api_app': self})


class HostController(ControllerBase):

    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
    hosts=0
    def __init__(self, req, link, data, **config):
        super(HostController, self).__init__(req, link, data, **config)
        self.topology_api_app = data['host_api_app']
    
    @route('topology', '/v1.0/topology/getHost',
           methods=['GET'])
    def getHost(self, req, **kwargs):
        body = json.dumps(HostController.hosts)
        return Response(content_type='application/json', body=body)

    @set_ev_cls(event.EventHostAdd)
    def switch_features_handler(self, ev):
        HostController.hosts+=1
