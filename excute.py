from flask import Flask
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.base import app_manager
from ryu.topology import event
app = Flask(__name__)

@app.route('/mio')
def tmp():
   return 'palle'

@app.route('/')
def hello_world():
   return '<a href="/switch">Prova</a>'
@app.route('/switch')
def get_switch(app, dpid=None):
    rep = app.send_request(event.EventSwitchRequest(dpid))
    return rep.switches

  



class L2Switch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(L2Switch, self).__init__(*args, **kwargs)
        app.run()
   
   
   

      

