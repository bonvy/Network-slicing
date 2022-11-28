from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ruy.api import get_switch, get_link, get_host
from flask import Flask, url_for
app = Flask(__name__)

class test(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]
    def __init__(self, *args, **kwargs):
        super(test, self).__init__(*args, **kwargs)

    @app.route('/switch')
    def switch(self):
        print( get_switch(self))

     