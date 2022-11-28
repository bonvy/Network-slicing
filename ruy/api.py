from ryu.base import app_manager
from ryu.topology import event
from ruy.api import get_switch, get_link, get_host


def get_switch(app, dpid=None):
    rep = app.send_request(event.EventSwitchRequest(dpid))
    return rep.switches


def get_all_switch(app):
    return get_switch(app)


def get_link(app, dpid=None):
    rep = app.send_request(event.EventLinkRequest(dpid))
    return rep.links


def get_all_link(app):
    return get_link(app)


def get_host(app, dpid=None):
    rep = app.send_request(event.EventHostRequest(dpid))
    return rep.hosts


def get_all_host(app):
    return get_host(app)


app_manager.require_app('ryu.topology.switches', api_style=True)