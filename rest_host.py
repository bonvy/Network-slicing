import json

from ryu.app.wsgi import ControllerBase
from ryu.app.wsgi import Response
from ryu.app.wsgi import route
from ryu.app.wsgi import WSGIApplication
from ryu.base import app_manager

class HostAPI(app_manager.RyuApp):
    _CONTEXTS = {
        'wsgi': WSGIApplication
    }

    def __init__(self, *args, **kwargs):
        super(HostAPI, self).__init__(*args, **kwargs)

        wsgi = kwargs['wsgi']
        wsgi.register(HostController, {'host_api_app': self})


class HostController(ControllerBase):
    def __init__(self, req, link, data, **config):
        super(HostController, self).__init__(req, link, data, **config)
        self.topology_api_app = data['host_api_app']
    
    @route('topology', '/v1.0/topology/getHost',
           methods=['GET'])
    def getHost():
        body = json.dumps("prova")
        return Response(content_type='application/json', body=body)
