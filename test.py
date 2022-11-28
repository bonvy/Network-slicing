from ruy.api import get_switch, get_link, get_host

switches = get_switch(self.topology_api_app, dpid)
body = json.dumps([switch.to_dict() for switch in switches])