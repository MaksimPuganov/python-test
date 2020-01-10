import netifaces
from pprint import pprint

def get_interfaces():

    interfaces = netifaces.interfaces()
    interfaces.remove('lo')

    out_interfaces = dict()

    for interface in interfaces:
        addrs = netifaces.ifaddresses(interface)
        out_addrs = dict()
        if netifaces.AF_INET in addrs.keys():
            out_addrs["ipv4"] = addrs[netifaces.AF_INET]
        if netifaces.AF_INET6 in addrs.keys():
            out_addrs["ipv6"] = addrs[netifaces.AF_INET6]
        out_interfaces[interface] = out_addrs

    return out_interfaces

def default_physical_interface(self):
    # When simulated interfaces are disabled, the interface names on nodes correspond to real
    # interfaces on the host platform.
    # When simulated interface are enabled, the interface names on nodes are "fake" i.e. they do
    # not correspond to real interfaces on the host platform. All these simulated interfaces
    # actually run on a single real interface, referred to as the physical interface. Traffic to
    # and from different simulated interfaces are distinguished by using different multicast
    # addresses and port numbers for each simulated interface.
    # Pick the first interface with a broadcast IPv4 address (if any) as the default.
    for intf_name in netifaces.interfaces():
        addresses = netifaces.ifaddresses(intf_name)
        if netifaces.AF_INET in addresses:
            ipv4_addresses = addresses[netifaces.AF_INET]
            for ipv4_address in ipv4_addresses:
                if 'broadcast' in ipv4_address:
                    return intf_name
    print("Cannot pick default physical interface: no broadcast interface found")
    sys.exit(1)

net=get_interfaces()
pprint(str(net['wlp3s0']['ipv4'][0]['addr']))
